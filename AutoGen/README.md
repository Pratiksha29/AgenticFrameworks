# AutoGen: TLDR AI → Latest GenAI Research Workflow

This workflow uses [AutoGen](https://microsoft.github.io/autogen/) to read the [TLDR AI](https://tldr.tech/ai) newsletter and return the **latest research article on Generative AI (GenAI)**.

## What it does

1. **Fetches** the latest TLDR AI edition from `https://tldr.tech/api/latest/ai`.
2. **Parses** the HTML for research-oriented sections (e.g. "Engineering & Research", "Deep Dives & Analysis") and GenAI-related links (e.g. arxiv, LLM/agent articles).
3. An **AutoGen AssistantAgent** uses a tool that returns this parsed content, then selects and summarizes the single best "latest GenAI research" article for you (title, URL, short summary).

## Setup

1. **Create a virtual environment** (recommended):

   ```bash
   cd AutoGen
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**:

   - Option A: export in shell  
     `export OPENAI_API_KEY=sk-...`
   - Option B: create a `.env` in the `AutoGen` folder (or project root) with:
     ```
     OPENAI_API_KEY=sk-...
     ```
     `python-dotenv` is included so the script will load `.env` if present.

## Run

```bash
python tldr_genai_workflow.py
```

The script will:

- Call the TLDR AI fetcher tool to get the latest research-style articles.
- Use the LLM to pick the latest/most relevant GenAI research article and print its title, link, and a brief summary.

## Project layout

- **`tldr_genai_workflow.py`** – AutoGen workflow: `AssistantAgent` + TLDR tool and task.
- **`tldr_fetcher.py`** – Fetches and parses TLDR AI HTML; used by the tool.
- **`requirements.txt`** – Python dependencies (AutoGen, OpenAI, requests, BeautifulSoup, python-dotenv).

## Requirements

- **Python 3.10+** (required by `autogen-ext`; the workflow will not install on 3.9)
- OpenAI API key (for the AutoGen assistant model, e.g. `gpt-4o-mini`).


cd AutoGen
python3.10 -m venv .venv   # or python3 if it’s 3.10+
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...   # or use a .env file
python tldr_genai_workflow.py