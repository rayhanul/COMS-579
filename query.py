import argparse
import sys 
from pdf_manager import *;
from embedder import *; 
from parsing_keys import *;
from rag_manager import *;





if __name__=="__main__":


    

    parser = argparse.ArgumentParser(
        description="COMS 579 Project",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--question",
        type=str,
        help="Question...",
        required=True
    )

    # sys.argv=[os.path.basename(__file__), "--pdf_file=~/Documents/"]


    args = parser.parse_args()

    if args.question is None or args.question.strip() == '':
        print("Error: No Question provided. Please ask a question.")
        sys.exit(1)

    question=args.question
        

    key_manager= Key_parser()
    my_keys=key_manager.parsing_keys()




    rag_manager=Rag_Manager(my_keys )

    ans= rag_manager.answer_query(question)



    print(ans["answer"]) 















