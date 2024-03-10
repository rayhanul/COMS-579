
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain


class Rag_Manager():

    def __init__(self,my_keys, index, embed):
        self.keys=my_keys
        self.index=index 
        self.embed=embed 



    def get_llm(self):

        return ChatOpenAI(
            openai_api_key=self.keys["_OPENAI_API_KEY_"],
            model_name='gpt-3.5-turbo',
            temperature=0.0
        )
    
    def get_vector_store(self):
        text_field="text"

        vectorstore = Pinecone(
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


