from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings

from langchain.vectorstores import FAISS
import faiss


def get_vectorstore() -> FAISS:
    # Define your embedding model
    embeddings_model = OpenAIEmbeddings()  # type: ignore
    # Initialize the vectorstore as empty

    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
    return vectorstore
