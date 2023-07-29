import sys
from iminder.autogpt import AutoGPTAgent

if len(sys.argv) < 2:
    print("Please provide the PID as a command-line argument.")
    sys.exit(1)

pid = int(sys.argv[1])
verbose = "-v" in sys.argv

bot = AutoGPTAgent(model="gpt-4", verbose=verbose)
bot.run([f"Obtain the resource usage of the process whose pid is {pid} over a period of time, "
         "then analyze the process's resource usage based on statistical information and save above statistical information and analyse result to the markdown file. "])

