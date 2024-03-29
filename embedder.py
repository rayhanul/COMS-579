
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
import tiktoken
from pinecone import Pinecone 
from pinecone import ServerlessSpec
import time 
from tqdm.auto import tqdm
from uuid import uuid4

_demensionality_model=1536 

class Text_embedder():

    def __init__(self, text, keys):
        self.text=text
        self.keys=keys
        self.embedding_model_name='text-embedding-ada-002' 
        self.embed=self.get_embedding()
        self.pc = Pinecone(api_key=self.keys["_PINECONE_KEY_"])
        self.spec=ServerlessSpec(cloud="aws", region="us-west-2")
        self.index_name = 'coms-nlp-project'
        self.batch_limit = 100
        self.tokenizer = tiktoken.get_encoding('cl100k_base')
        self.text_splitter=self.get_text_splitter()


    def tiktoken_len(self,text):
        
        tokens = self.tokenizer.encode(
            text,
            disallowed_special=()
        )
        return len(tokens)


    def get_embedding(self):

        return OpenAIEmbeddings(
            model=self.embedding_model_name,
            openai_api_key=self.keys['_OPENAI_API_KEY_']
        )

    def get_text_splitter(self):
        return RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=20,
            length_function=self.tiktoken_len,
            separators=["\n\n", "\n", " ", ""]
        )

    def embed_text(self):
        existing_indexes = [index_info["name"] for index_info in self.pc.list_indexes()]

        if self.index_name not in existing_indexes:

            self.pc.create_index(
                self.index_name,
                dimension=1536,  # dimensionality of ada 002
                metric='dotproduct',
                spec=self.spec
            )

            while not self.pc.describe_index(self.index_name).status['ready']:
                time.sleep(1)


        index = self.pc.Index(self.index_name)
        time.sleep(1)

        index.describe_index_stats()
        return index 


    def get_indexing(self, data):
        index=self.embed_text()


        texts = []
        metadatas = []

        for i, record in enumerate(tqdm(data)):

            # first get metadata fields for this record
            metadata = {
                # 'id': str(i),
                'source': record,
                # 'title': record['title']
            }

            record_texts = self.text_splitter.split_text(record)

            record_metadatas = [{
                "chunk": j, "text": text, **metadata
            } for j, text in enumerate(record_texts)]

            texts.extend(record_texts)
            metadatas.extend(record_metadatas)

            if len(texts) >= self.batch_limit:
                ids = [str(uuid4()) for _ in range(len(texts))]
                embeds = self.embed.embed_documents(texts)
                index.upsert(vectors=zip(ids,embeds, metadatas))
                texts = []

        if len(texts) > 0:
            ids = [str(uuid4()) for _ in range(len(texts))]
            embeds = self.embed.embed_documents(texts)
            index.upsert(vectors=zip(ids, embeds, metadatas))

        return index, self.index_name, self.embed



    def remove_index(self, index_name):
        self.pc.delete_index(index_name)


        