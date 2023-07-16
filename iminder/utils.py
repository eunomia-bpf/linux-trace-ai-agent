from typing import List

from langchain.agents import Tool
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.tools.base import BaseTool
from langchain.vectorstores import FAISS
import faiss

from iminder.tools import (
    sample,
    SampleInput
)


def get_agent_tools() -> List[BaseTool]:
    """Get the tools that will be used by the AI agent."""
    tools: List[BaseTool] = [
        Tool(
            name="sample",
            func=sample,
            description="useful to get a dictionary that contains recorded metrics for the monitored process, "
                        "including CPU usage percentages, memory usage values (in bytes), I/O read and write bytes, "
                        "and the number of network connections over time",
            args_schema=SampleInput,
        ),
    ]
    return tools


def get_vectorstore() -> FAISS:
    # Define your embedding model
    embeddings_model = OpenAIEmbeddings()  # type: ignore
    # Initialize the vectorstore as empty

    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
    return vectorstore
