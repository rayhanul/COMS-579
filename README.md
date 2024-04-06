# This project completed as a part of COMS-579: Natural Language Processing coursework

## This project is based on Retrieval-augmented generation (RAG) framework to give generative models knowledge without finetuning themselves.
## Team Members
- Md Rayhanul Islam
- Md Obaidul Kabir



## Experimental setup Instalation of the required packages
### Python environment creation (We assume you already have python and conda installed in your computer, and we tested the following command in Ubuntu OS) 
- Open a Linux Terminal
- `conda create -n "nlp" python==3.10`
- `conda activate nlp`

### Cloing repository and installing all required packages
- Clone the repo: `git clone https://github.com/rayhanul/COMS-579.git`
- Go to inside `COMS-579`
- `pip install -r requirements.txt`

if any package does not get installed, please run the following commands: 

`pip install -U langchain openai chromadb langchain-experimental`

`pip install "unstructured[all-docs]" pillow pydantic lxml pillow matplotlib chromadb tiktoken`

## Upload a pdf file

- Run command `python upload.py --pdf_file file_name`, where file_name is any pdf file. 

## Query 

