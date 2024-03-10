
from pdf_manager import *;
from embedder import *; 
from parsing_keys import *;





if __name__=="__main__":

    file_name="test.pdf"

    key_manager= Key_parser()
    my_keys=key_manager.parsing_keys()

    pdf_manager= Data_Loader(file_name)
    text_tokens=pdf_manager.get_text_from_pdf()

    text_embedder=Text_embedder(text=text_tokens, keys=my_keys)

    index_name=text_embedder.get_indexing(text_tokens)

    






