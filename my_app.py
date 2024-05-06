import funix

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


@funix.funix(
  argument_labels={
    "x": "The number to be squared"
  }
)

def Index_New_File(x: int) -> int:
    return x * x


