# InsightMinder

`InsightMinder` is an agent for automatic monitoring of system performance. It leverages a combination of available monitoring tools and the power of GPT (Generative Pre-trained Transformer) to analyze the resource utilization of a specific process identified by its PID. The project aims to provide detailed insights and recommendations by collecting and analyzing process statistical information.


### Features ✨

- 🧠 Automated Task Planning: GPT plans and executes monitoring and analysis tasks for the process seamlessly until completion.
- 🛠 Multi-tool Support: InsightMinder optimally utilizes available resources with monitoring, terminal, and network search capabilities.
- 🔄 One-Click Operation: Simplify your workflow using our user-friendly interface. Just provide the PID, and InsightMinder handles the entire process analysis.


### how to use

1. Set up your [OpenAI API Keys](https://platform.openai.com/account/api-keys) and add OPENAI_API_KEY env variable.
2. Install Python requirements via `pip install -r requirements.txt`
3. Use tools such as `ps` and `top` to obtain the PID of the target process.
4. Run InsightMinder via `python -m iminder pid`
