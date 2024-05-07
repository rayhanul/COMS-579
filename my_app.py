import funix
import IPython
import fitz
import ipywidgets
from typing import List;
from funix.widget.builtin import BytesFile;
import time 

from pdf_manager import *;
from embedder import *; 
from parsing_keys import *;
from rag_manager import *;



messages= []



@funix.funix(
  print_to_web=True,
  direction="column-reverse",
  argument_labels={
    "query": "What's on your mind?"
  }
)

def Ask_Question(query: str) -> IPython.display.HTML:
    
    def print_messages_html(messages):
      printout = ""
      for message in messages:
          if message["role"] == "user":
              align, left, name = "left", "0%", "You"
          elif message["role"] == "assistant":
              align, left, name = "right", "30%", "ChatArticle"
          printout += f'<div style="position: relative; left: {left}; width: 70%"><b>{name}</b>: {message["content"]}</div>'
      return printout

    key_manager= Key_parser()
    my_keys=key_manager.parsing_keys()




    rag_manager=Rag_Manager(my_keys )

    ans= rag_manager.answer_query(query)


    current_message= ans["answer"] 
    current_message = current_message.strip()
    messages.append({"role": "user", "content": query})
    messages.append({"role": "assistant", "content": current_message})
    return print_messages_html(messages)


@funix.funix(
    title="Index a New File",
    print_to_web=True,
    description="Drag your pdf files"
) 

def Index_New_File( filepaths: List[BytesFile]) -> IPython.display.Markdown:

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
    

@funix.funix(print_to_web=True) 


def About ()-> str: 
    
    message= "This is a rag system developed by Md Rayhanul Islam and Md Obaidur kabir as a part of course project for COMS-579 at Iowa State University."
    print( message)