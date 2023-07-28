import sys
from iminder.autogpt import AutoGPTAgent

if len(sys.argv) < 2:
    print("Please provide the PID as a command-line argument.")
    sys.exit(1)

pid = int(sys.argv[1])

bot = AutoGPTAgent(model="gpt-4", verbose=True)
bot.run(["Firstly, create a markdown file to save the data and analysis results."
         f"Obtain the resource usage of the process whose pid is {pid} over a period of time, "
         "then analyze the process's resource usage based on statistical information, "
         "and finally, save all the detailed statistical information and analysis results to a markdown file.\n"
         "If possible, present the statistical data in the form of graphs or images and consolidate all the information "
         "into a Markdown file, providing a detailed analysis of the usage of each type of resource."
         "IMPORT: During this process, all valid information should be saved to the same markdwon file!!!"])

