# Agentic-AI-Deep-Research-Azure

🚀 An **Agentic AI pipeline** powered by **Azure OpenAI** for automated deep research, report generation, and email delivery.

This project demonstrates how to orchestrate multiple **AI agents** in a workflow:

1. **Planner Agent** → decides what searches to run.
2. **Search Agent** → gathers insights (mocked for cost-free execution).
3. **Writer Agent** → generates a structured research report with Azure OpenAI.
4. **Email Agent** → formats & sends the report (mocked with a console preview).

It also includes a **Gradio UI** for easy interaction.

---

## 📂 Project structure

Agentic-AI-Deep-Research-Azure/
├── deep_research/
│ ├── init.py
│ ├── azure_client.py # Azure OpenAI client helper
│ ├── email_agent.py # Mock email agent
│ ├── planner_agent.py # Planner agent (decides searches)
│ ├── research_manager.py # Orchestrates workflow
│ ├── search_agent.py # Mock search agent
│ └── writer_module.py # Writer agent + ReportData schema
├── main.py # Entry point (launches Gradio UI)
├── requirements.txt # Project dependencies
├── .gitignore # Ignore .env, venv, cache files
├── .env.example # Template for environment variables
└── README.md # This file

---

## ⚙️ Requirements & recommended environment

- Python **3.11** or **3.12** (recommended).

  - Python 3.13 may have compatibility issues with some audio packages used by Gradio.
- A working Azure OpenAI deployment (deployment name, endpoint, API key).

  Example `requirements.txt` (suggested — pin versions if you like):

  ```text
  openai==1.43.0
  gradio==4.44.0
  python-dotenv==1.0.1
  pydantic
  nest_asyncio
  # If you use a local agents package, include it or ensure openai.agents is available

  ```

## 🔧 Setup (Step-by-Step)

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/Agentic-AI-Deep-Research-Azure.git
   cd Agentic-AI-Deep-Research-Azure
   ```
2. **Create a virtual environment**

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**

- Copy .env.example to .env:

  ```bash
  # Linux / Mac
  cp .env.example .env
  # Windows
  copy .env.example .env
  ```
- Edit .env and add your Azure OpenAI credentials:

  ```
  OPENAI_API_KEY=your-azure-api-key
  OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
  OPENAI_API_VERSION=2024-06-01-preview
  OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
  ```
- ⚠️ Do not commit .env – it’s already in .gitignore.

5. **Run the app**

- Run the app

  ```
  python main.py
  ```
- You’ll see output like:

  ```
  Running on local URL: http://127.0.0.1:7860
  ```

The UI may open in your browser automatically. Use the textbox to enter a research topic and run the pipeline.

## 🖥️ What happens when you run

1. Planner prepares search terms (mocked/fallback).
2. Search tasks run in parallel (mocked summaries).
3. Writer agent calls Azure OpenAI to generate a long Markdown report.
4. Email agent formats and (mock) sends the report — printed to console for safety.
5. Final report shows in the Gradio UI.

   Console output example:

   ```
   Planning searches...
   Searching...
   Finished searching
   Writing report...
   [MOCK EMAIL] Pretending to send email...
   Subject: Research Results
   [MOCK EMAIL] Success
   ```

## 🔁 Notes about mocks and tracing

* **Web search** and **email sending** are mocked by default to avoid external costs and accidental emails. Replace mocks with real integrations when you're ready.
* The repo disables OpenAI-hosted tracing by default (to avoid 401 trace errors when using Azure). If you want OpenAI trace dashboard integration, you would need a valid public OpenAI key for that service.

## ✅ Next steps / ideas to extend

* Replace `mock_web_search` with a real web-search tool or a cached search results source.
* Connect `send_email` to SendGrid or any SMTP service for real email delivery (take care with credentials).
* Add streaming responses from Azure OpenAI to display partial output in the UI.
* Containerize the app and deploy to Azure App Service / Container Apps.

## 📜 License

MIT License — feel free to use and adapt.

---
