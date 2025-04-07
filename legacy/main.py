import sys
from dotenv import load_dotenv

from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# load any api keys
load_dotenv()

# get the file path and define the llm to be used
def get_usage():

    if len(sys.argv) == 3 and sys.argv[1] == "local":
        #local model
        llm = ChatOllama(model="llama3",temperature=0)
        path = sys.argv[2]
                  
    elif len(sys.argv) == 2:
        #OpenAI model
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        path = sys.argv[1]

    else:
        print("Usage:")
        print("python main.py PDFpath")
        print("python main.py local PDFpath")
        sys.exit()

    return (path, llm)

# use the langchain framework to summarise the pdf
def summarise(path, llm):

    loader = PyPDFLoader(path)
    docs = loader.load_and_split()
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.invoke(docs)

    return summary


if __name__ == '__main__':

    path, llm = get_usage()
    summary = summarise(path, llm)

    print("Summary:")
    print(summary['output_text'])