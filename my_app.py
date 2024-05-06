import funix
import IPython
import fitz
import ipywidgets
from typing import List;
from funix.widget.builtin import BytesFile;


from pdf_manager import *;
from embedder import *; 
from parsing_keys import *;
from rag_manager import *;

@funix.funix(
  argument_labels={
    "query": "What's on your mind?"
  }
)

def Ask_Question(query: str) -> str:
    key_manager= Key_parser()
    my_keys=key_manager.parsing_keys()




    rag_manager=Rag_Manager(my_keys )

    ans= rag_manager.answer_query(query)



    
    return ans["answer"]


# @funix.funix(
#   argument_labels={
#     "x": "The number to be squared"
#   }
# )

# def Index_a_New_File(x: int) -> int:
#     return x * x


@funix.funix(
    title="Index a New File",
    print_to_web=True,
    description="Drag your pdf files"
) 

def Index_New_File(               
    filepaths: List[BytesFile]
    ) -> IPython.display.Markdown:

    try:
        texts = []
        for i, file in enumerate(filepaths):
            with fitz.open(stream=file, filetype="pdf") as doc:
                text_list = [page.get_text() for page in doc]
                
                texts.extend(text_list)


        key_manager= Key_parser()
        my_keys=key_manager.parsing_keys()


        text_embedder = Text_embedder(texts, my_keys)

        texts=[ text.replace("\n", " ") for text in texts]
        index, indexname, embed = text_embedder.get_indexing(texts)

        return "Indexing is completed successfully."

    except Exception as e:
      return "Exception encounted! Indexing failed. "