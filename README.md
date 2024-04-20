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


## Upload a pdf file

- Run command `python upload.py --pdf_file file_name`, where file_name is any pdf file. 
- For Demo, visit: https://youtu.be/ZFAqBrj08CQ 



## Query 

- Run command `python query.py --question query`, where query is any question. 
- For Demo, visit: https://youtu.be/ZFAqBrj08CQ 

For example, when I ask "what is fuzzing? it answer: Fuzzing usually refers to automated test input generation for exposing potential software bugs or security vulnerabilities. It is a technique used to identify vulnerabilities in software by providing random or invalid data as input to the system. 