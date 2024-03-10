from langchain_text_splitters import CharacterTextSplitter

# from langchain.text_splitter import CharacterTextSplitter

from unstructured.partition.pdf import partition_pdf

import os 


class Data_Loader():

    def __init__(self, file_name):
        self.fname=file_name

    

    def extract_pdf_elements(self):
        """
        Extract images, tables, and chunk text from a PDF file.
        path: File path, which is used to dump images (.jpg)
        fname: File name
        """
        current_directory= os. getcwd()+"/"
        return partition_pdf(
            filename=current_directory+ self.fname,
            extract_images_in_pdf=False,
            infer_table_structure=True,
            chunking_strategy="by_title",
            max_characters=4000,
            new_after_n_chars=3800,
            combine_text_under_n_chars=2000,
            image_output_dir_path=current_directory
        )
    
    def categorize_elements(self, raw_pdf_elements):
        """
        Categorize extracted elements from a PDF into tables and texts.
        raw_pdf_elements: List of unstructured.documents.elements
        """
        tables = []
        texts = []
        images=[]
        for element in raw_pdf_elements:
            if "unstructured.documents.elements.Table" in str(type(element)):
                tables.append(str(element))
            elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
                texts.append(str(element))
        return texts, tables


    def get_text_from_pdf(self):
        
        raw_pdf_elements = self.extract_pdf_elements()

        # Get text, tables
        texts, tables = self.categorize_elements(raw_pdf_elements)

        # Optional: Enforce a specific token size for texts
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000, chunk_overlap=0
        )
        joined_texts = " ".join(texts)
        texts_tokens = text_splitter.split_text(joined_texts)
        return texts_tokens 
        

# if __name__=="__main__":

#     print("I am here")
#     fpath = "/home/rayhanul/Documents/GitHub/COMS-579/"
#     fname = "test_pdf.pdf"

#     data_loader=Data_Loader(fpath, fname)
#     # Get elements
#     # raw_pdf_elements = data_loader.extract_pdf_elements(fpath, fname)

#     # # Get text, tables
#     # texts, tables = data_loader.categorize_elements(raw_pdf_elements)

#     # # Optional: Enforce a specific token size for texts
#     # text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     #     chunk_size=1000, chunk_overlap=0
#     # )
#     # joined_texts = " ".join(texts)
#     # texts_4k_token = text_splitter.split_text(joined_texts)

#     texts_tokens=data_loader.get_text_from_pdf()


#     print(texts_tokens)

