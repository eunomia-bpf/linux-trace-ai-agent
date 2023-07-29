import sys
from iminder.autogpt import AutoGPTAgent

if len(sys.argv) < 2:
    print("Please provide the PID as a command-line argument.")
    sys.exit(1)

pid = int(sys.argv[1])

bot = AutoGPTAgent(model="gpt-4", verbose=False)
bot.run([f"Obtain the resource usage of the process whose pid is {pid} over a period of time, "
         "then analyze the process's resource usage based on statistical information and save above statistical information and analyse result to the markdown file. "
         "Review the previous analysis process to determine whether it is comprehensive, if not, use the appropriate command to obtain more information, and repeat the above process.\n"])

