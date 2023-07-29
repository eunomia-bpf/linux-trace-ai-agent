import platform
import time
import psutil
from pydantic import BaseModel, Field
from langchain.agents import Tool
from io import StringIO
from contextlib import redirect_stdout
from typing import List
from langchain.tools.base import BaseTool
from langchain.tools import ShellTool
from langchain.tools import DuckDuckGoSearchRun

from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

def get_agent_tools() -> List[BaseTool]:
    """Get the tools that will be used by the AI agent."""
    shell_tool = ShellTool()

    system = "MacOS" if platform.system()=="Darwin" else platform.system()
    shell_tool.description = f"Run shell commands on this {system} machine. " + \
    "It is useful when you need to monitor or collect resource usage information of a process, " + \
    "or when you need to perform file read/write operations and various terminal commands."
    tools: List[BaseTool] = [
        Tool(
            name="sample",
            func=sample,
            description="useful to get a dictionary that contains recorded metrics for the monitored process, "
                        "including CPU usage percentages, memory usage values (in bytes), I/O read and write bytes, "
                        "and the number of network connections over time",
            args_schema=SampleInput,
        ),
        Tool(
            name="analyse_process",
            func=analyse_process,
            description="Analyzes the resource usage of a process based on the provided statistical information.",
            # args_schema=AnalyseInput,
        ),
        shell_tool,
        DuckDuckGoSearchRun()

    ]
    return tools



def sample(pid: int):
    """
    Monitors the specified process identified by its PID and records its CPU usage, memory usage,
    I/O read/write bytes, and network connections.
    Args:
        pid (int): The process ID of the process to monitor.

    Returns:
        The `sample` function returns a dictionary that contains recorded metrics for 
        the monitored process, including CPU usage percentages, memory usage values (in bytes), 
        I/O read and write bytes, and the number of network connections within 2.5 seconds.
    """
    process = psutil.Process(pid)

    records = {
        "CPU Usage": [],
        "Memory Usage": [],
        "IO Read Bytes": [],
        "IO Write Bytes": [],
        "Network Connections": []
    }

    for _ in range(50):
        cpu_percent = process.cpu_percent(interval=0.1)
        memory_info = process.memory_info()
        io_counters = process.io_counters()
        connections = process.connections()
        records['CPU Usage'].append(cpu_percent)
        records['Memory Usage'].append(memory_info.rss)
        records['IO Read Bytes'].append(io_counters.read_bytes)
        records['IO Write Bytes'].append(io_counters.write_bytes)
        records['Network Connections'].append(len(connections))
        time.sleep(0.05)
    return records

class SampleInput(BaseModel):
    pid: int = Field(
        ...,
        description="The process ID (PID) of the process to monitor.",
    )


def analyse_process(arg: str) -> str:
    """
    Analyzes the resource usage of a process based on the provided statistical information.

    Args:
        arg (str): Statistical data of process resource usage.
        output_file(str): The file path corresponding to saving the analysis results.
    Returns:
        str: A detailed and insightful explanation of the process's resource usage during the
            specified period, generated using the GPT-3.5 turbo language model.
    """
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0)
    agent_chain = ConversationChain(llm=llm, verbose=False,
                    memory=ConversationBufferMemory())
    prompt = f"""The following statistical information records the process's resource usage 
    over a short period of time. I need you to analyze this data and provide a 
    detailed and insightful explanation of the process's resource usage during this period.
    The statistical information as following:
    {arg}

    """
    result = agent_chain.predict(input=prompt)
    return result

class AnalyseInput(BaseModel):
    arg: str = Field(
        ...,
        description="Statistical data of process resource usage.",
    ),
