
from pdf_manager import *;
from embedder import *; 
from parsing_keys import *;
from rag_manager import *;





if __name__=="__main__":

    file_name="test_pdf.pdf"
    query="what is fuzz testing"
    key_manager= Key_parser()
    my_keys=key_manager.parsing_keys()

    pdf_manager= Data_Loader(file_name)
    text_tokens=pdf_manager.get_text_from_pdf()

    text_embedder=Text_embedder(text=text_tokens, keys=my_keys)

    index, index_name, embed =text_embedder.get_indexing(text_tokens)


    rag_manager=Rag_Manager(my_keys, index, embed )

    ans= rag_manager.answer_query(query)

    print(ans) 













