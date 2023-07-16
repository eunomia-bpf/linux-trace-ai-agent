import sys
from iminder.autogpt import AutoGPTAgent

if len(sys.argv) < 2:
    print("Please provide the PID as a command-line argument.")
    sys.exit(1)

pid = int(sys.argv[1])

bot = AutoGPTAgent(model="gpt-4", verbose=True)
bot.run(["analyse the pid {}".format(pid)])
