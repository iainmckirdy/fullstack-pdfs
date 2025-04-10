from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()  # Load API keys from .env

def summarise_pdf(path: str, use_local: bool = False) -> str:
    """
    Summarise a PDF file using a specified LLM.
    
    :param path: Path to the PDF file.
    :param use_local: Whether to use a local LLM (True) or OpenAI (False).
    :return: Summary as a string.
    """
    # Choose model
    if use_local:
        llm = ChatOllama(model="llama3", temperature=0)
    else:
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Load and split document
    loader = PyPDFLoader(path)
    docs = loader.load_and_split()

    # Summarize
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.invoke(docs)

    return summary['output_text']