
from langchain.vectorstores import Pinecone as vectorPineCone
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
import time 

class Rag_Manager():

    def __init__(self,my_keys):
        self.keys=my_keys
        self.index_name = 'coms-nlp-project'
        self.embedding_model_name='text-embedding-ada-002' 
        self.spec=ServerlessSpec(cloud="aws", region="us-west-2")
        self.embed=self.get_embedding()
        self.pc = Pinecone(api_key=my_keys["_PINECONE_KEY_"])
        self.index=self.embed_text() 
        


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
    
    def get_embedding(self):

        return OpenAIEmbeddings(
            model=self.embedding_model_name,
            openai_api_key=self.keys['_OPENAI_API_KEY_']
        )
    
    def get_llm(self):

        return ChatOpenAI(
            openai_api_key=self.keys["_OPENAI_API_KEY_"],
            model_name='gpt-3.5-turbo',
            temperature=0.0
        )
    
    def get_vector_store(self):
        text_field="text"

        vectorstore = vectorPineCone(
            self.index, self.embed.embed_query, text_field
        )

        return vectorstore


    def get_retrieval_qa(self, llm, vectorstore):

        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )
    def get_qa_with_source(self):

        llm=self.get_llm()
        vectorstore=self.get_vector_store()

        retrievalQA= RetrievalQAWithSourcesChain.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )
        return retrievalQA 



    def answer_query(self, query):



        qa_with_sources = self.get_qa_with_source()

        answer = qa_with_sources(query)

        return answer


