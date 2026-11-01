Here is a complete, professional `README.md` for your AI Python Code Review & Fix Agent, covering LangGraph, Ollama, Human-in-the-Loop approval, streaming, and automated code correction.

Writing

# AI Python Code Review & Fix Agent

An AI-powered Python code review and correction agent built using **LangGraph, LangChain, and Ollama (Qwen 2.5 Coder)**.

The agent analyzes Python source files, identifies bugs and potential security issues, generates a detailed code review report, and asks for human approval before applying AI-generated code fixes.

It uses **Human-in-the-Loop (HITL)** to ensure that code modifications only happen after explicit human authorization.

## Features

- **AI Code Review:** Reviews Python source code for bugs, logical errors, security vulnerabilities, performance issues, and code quality.
- **Human-in-the-Loop (HITL):** Pauses workflow execution and requests human approval before fixing code.
- **AI Code Fix Tool:** Generates corrected Python source code based on the review report.
- **Streaming Support:** Streams AI review output and workflow events.
- **LangGraph Workflow:** Uses a state-based graph architecture with conditional routing.
- **Checkpointing:** Uses LangGraph's `InMemorySaver` to preserve execution state during approval interruptions.
- **Original File Protection:** Saves corrected code into a separate file instead of overwriting the original.
- **CLI Interface:** Runs directly from the terminal.

## Architecture

text

```text
                 START
                   |
                   v
             LOAD CODE NODE
                   |
                   v
             AI CODE REVIEW
                   |
                   v
          HUMAN-IN-THE-LOOP
                   |
             Approval?
              /       \
             /         \
           YES          NO
            |            |
            v            v
       CODE FIX TOOL    END
            |
            v
       SAVE FIXED FILE
            |
            v
           END
```

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Core programming language |
| LangGraph | Agent workflow orchestration |
| LangChain | LLM integration |
| Ollama | Local LLM inference |
| Qwen 2.5 Coder 7B | Code review and correction |
| AsyncIO | Asynchronous execution |
| InMemorySaver | Graph checkpointing |

## Project Structure

text

```text
ai-code-review-agent/
│
├── agent.py
├── README.md
│
├── example.py
│
└── example_fixed.py
```

`example_fixed.py` is generated automatically when human approval is granted.

## Requirements

- Python 3.10+
- Ollama installed
- Qwen 2.5 Coder 7B model downloaded
- Required Python packages

## Installation

### 1\. Clone the repository

bash

```bash
git clone <your-repository-url>
```

bash

```bash
cd ai-code-review-agent
```

### 2\. Create a virtual environment

bash

```bash
python -m venv venv
```

Activate it:

**Windows**

bash

```bash
venv\Scripts\activate
```

**Linux / macOS**

bash

```bash
source venv/bin/activate
```

### 3\. Install dependencies

bash

```bash
pip install -U langgraph langchain-ollama langchain-core
```

### 4\. Install and start Ollama

Download Ollama:

[https://ollama.com/](<https://ollama.com/>)

Pull the required model:

bash

```bash
ollama pull qwen2.5-coder:7b
```

Make sure the Ollama service is running before starting the agent.

## Usage

Run the agent by providing a Python file path:

bash

```bash
python agent.py example.py
```

The agent will:

1. Read and validate the Python source file.
2. Send the source code to the Qwen model.
3. Generate a detailed code review report.
4. Display the report in the terminal.
5. Request human approval.
6. Generate corrected code if approved.
7. Save the corrected code in a separate file.

## Human-in-the-Loop

After completing the code review, the agent pauses execution and asks:

text

```text
Do you want AI to fix this code? (yes/no):
```

### Approve

text

```text
yes
```

The workflow resumes and invokes the code fix node.

### Reject

text

```text
no
```

The workflow ends without generating a corrected file.

This ensures that AI-generated code modifications require explicit human authorization.

## Code Fix Tool

The `fix_code` node uses Qwen 2.5 Coder to:

- Analyze the original source code.
- Interpret the AI code review report.
- Correct identified bugs and issues.
- Preserve intended program functionality.
- Generate the complete corrected Python source code.

The generated code is saved separately.

For example:

text

```text
example.py
example_fixed.py
```

The original source file remains unchanged.

## LangGraph Components

### StateGraph

Defines the agent's workflow and node connections.

### interrupt()

Pauses execution at the human approval node.

### Command(resume=...)

Resumes graph execution with the human's decision.

### InMemorySaver

Stores graph state and checkpoint information while the process is running.

### Conditional Routing

Routes execution according to human approval:

- Approved → `fix_code`
- Rejected → `END`

### Streaming

Uses `astream()` with multiple streaming modes:

- `messages` – AI-generated token streaming.
- `updates` – Graph node updates.
- `custom` – Custom workflow events.

## Configuration

The model and file size limit can be configured in `agent.py`.

python

```python
MODEL_NAME = "qwen2.5-coder:7b"
MAX_FILE_SIZE = 100_000
```

The default Ollama connection uses the local Ollama service configuration.

## Example Output

text

```text
=================================================
       AI PYTHON CODE REVIEW AND FIX AGENT
=================================================

[WORKFLOW] Starting execution...

[EVENT] Reading source code...

[GRAPH] Completed node: load_code

[EVENT] Starting AI code review...

# Code Review Report

## Summary
Potential issues identified.

## Bugs
...

[GRAPH] Completed node: review_code

[HUMAN-IN-THE-LOOP]

Do you want AI to fix this code? (yes/no): yes

[WORKFLOW] Resuming graph...

[APPROVED] AI code fixing was authorized.

[FIXED FILE] example_fixed.py

=================================================
              EXECUTION COMPLETED
=================================================
```

## Security Considerations

- Source files are checked for file type and maximum size.
- Source code and embedded instructions are treated as untrusted input by the model.
- Original files are not overwritten.
- AI-generated code is not automatically executed.
- Human approval is required before code correction.
- Generated code should be reviewed and tested before production use.

**Note:** Prompt instructions are not a complete security boundary. AI-generated corrections may still contain bugs or unsafe code.

## Future Enhancements

- Automated Python syntax validation using `ast`.
- Automated unit test execution.
- Static code analysis using Ruff and Bandit.
- Persistent checkpointing using SQLite or PostgreSQL.
- Web-based human approval interface.
- Multiple LLM provider support.
- Diff-based code correction and review.
- Automatic re-review after code correction.

## License

This project is available under the MIT License. Add a `LICENSE` file to the repository if you intend to distribute it under that license.

## Author

AI Python Code Review & Fix Agent

**Built with Python, LangGraph, LangChain, and Ollama.**

Suggested GitHub repository description:

> AI-powered Python Code Review & Fix Agent using LangGraph and Qwen 2.5 Coder, featuring streaming responses, Human-in-the-Loop approval, and automated code correction.

  