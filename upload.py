


import os 
import sys 
import argparse
from pdf_manager import *;
from embedder import *; 
from parsing_keys import *;

if __name__=="__main__":

    parser = argparse.ArgumentParser(
        description="COMS 579 Project",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--pdf_file",
        type=str,
        help="file to upload...",
        required=True
    )
    # sys.argv=[os.path.basename(__file__), "--pdf_file=test_pdf.pdf"]
    args = parser.parse_args()

    if args.pdf_file is None or args.pdf_file.strip() == '':
        print("Error: No file provided. Please specify a file with --pdf_file.")
        sys.exit(1)

    if not args.pdf_file.lower().endswith('.pdf'):
        print("Error: The file provided is not a PDF.")
        sys.exit(1)
        
    file_path = os.path.expanduser(args.pdf_file)
    file_name = os.path.abspath(file_path)

    key_manager= Key_parser()
    my_keys=key_manager.parsing_keys()

    pdf_manager= Data_Loader(file_name)
    text_tokens=pdf_manager.get_text_from_pdf()

    text_tokens=[ text.replace("\n", " ") for text in text_tokens]

    text_embedder=Text_embedder(text=text_tokens, keys=my_keys)

    index, index_name, embed =text_embedder.get_indexing(text_tokens)

