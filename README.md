# Agentic AI Deep Research Azure

🚀 An **Agentic AI pipeline** powered by **Azure OpenAI** for automated deep research, report generation, and email delivery.

This project demonstrates how to orchestrate multiple **AI agents** in a workflow to conduct comprehensive research and generate detailed reports automatically.

## 🎯 Overview

This agentic AI system consists of four specialized agents working together:

1. **🧠 Planner Agent** → Strategically decides what searches to run based on the research topic
2. **🔍 Search Agent** → Gathers insights and information (currently mocked for cost-free execution)
3. **✍️ Writer Agent** → Generates structured, comprehensive research reports using Azure OpenAI
4. **📧 Email Agent** → Formats and delivers reports (mocked with console preview for safety)

The system includes a user-friendly **Gradio UI** for seamless interaction and real-time monitoring of the research pipeline.

---

## 🏗️ Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│   Planner   │───▶│    Search    │───▶│   Writer    │───▶│    Email    │
│    Agent    │    │    Agent     │    │    Agent    │    │    Agent    │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
       │                   │                   │                   │
       ▼                   ▼                   ▼                   ▼
  Search Terms      Web Results        Markdown Report      Email Delivery
```

---

## 📂 Project Structure

```
Agentic-AI-Deep-Research-Azure/
├── deep_research/
│   ├── __init__.py
│   ├── azure_client.py          # Azure OpenAI client helper
│   ├── email_agent.py           # Mock email agent for report delivery
│   ├── planner_agent.py         # Strategic search planning agent
│   ├── research_manager.py      # Workflow orchestration manager
│   ├── search_agent.py          # Mock search agent for data gathering
│   └── writer_module.py         # Report generation + ReportData schema
├── main.py                      # Entry point (launches Gradio UI)
├── requirements.txt             # Project dependencies
├── .gitignore                   # Ignore .env, venv, cache files
├── .env.example                 # Template for environment variables
└── README.md                    # This documentation
```

---

## ⚙️ Prerequisites

### System Requirements
- **Python 3.11** or **3.12** (recommended)
  - ⚠️ Python 3.13 may have compatibility issues with some audio packages used by Gradio
- **Azure OpenAI** deployment with API access

### Azure OpenAI Requirements
- Valid Azure OpenAI resource
- Deployed model (e.g., `gpt-4o-mini` or `gpt-4`)
- API key and endpoint URL
- API version compatibility (`2024-06-01-preview` recommended)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Agentic-AI-Deep-Research-Azure.git
cd Agentic-AI-Deep-Research-Azure
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example environment file
# Linux / Mac
cp .env.example .env

# Windows
copy .env.example .env
```

Edit `.env` with your Azure OpenAI credentials:
```env
OPENAI_API_KEY=your-azure-api-key-here
OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
OPENAI_API_VERSION=2024-06-01-preview
OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
```

**🔒 Security Note:** Never commit your `.env` file. It's already included in `.gitignore`.

### 5. Launch the Application
```bash
python main.py
```

The application will start and display:
```
Running on local URL: http://127.0.0.1:7860
```

The Gradio UI should automatically open in your browser.

---

## 💡 How to Use

1. **Access the UI**: Navigate to `http://127.0.0.1:7860` in your browser
2. **Enter Research Topic**: Type your research question or topic in the text box
3. **Run Pipeline**: Click the submit button to start the agentic research process
4. **Monitor Progress**: Watch the console output for real-time pipeline status
5. **Review Results**: The generated report will appear in the UI output area

### Example Research Topics
- "Latest developments in quantum computing"
- "Impact of AI on healthcare industry"
- "Sustainable energy solutions for 2024"
- "Blockchain adoption in financial services"

---

## 🔄 Pipeline Workflow

When you submit a research topic, here's what happens:

### Stage 1: Planning 🧠
```
Planning searches...
```
The Planner Agent analyzes your topic and determines optimal search strategies.

### Stage 2: Research 🔍
```
Searching...
Finished searching
```
The Search Agent executes parallel searches (currently mocked) to gather relevant information.

### Stage 3: Report Generation ✍️
```
Writing report...
```
The Writer Agent uses Azure OpenAI to synthesize findings into a comprehensive Markdown report.

### Stage 4: Delivery 📧
```
[MOCK EMAIL] Pretending to send email...
Subject: Research Results
[MOCK EMAIL] Success
```
The Email Agent formats and prepares the report for delivery (currently mocked for safety).

---

## 📋 Dependencies

### Core Dependencies
```text
openai==1.43.0              # Azure OpenAI integration
gradio==4.44.0              # Web UI framework
python-dotenv==1.0.1        # Environment variable management
pydantic                    # Data validation and parsing
nest_asyncio               # Async compatibility
```

### Optional Dependencies
Consider pinning specific versions in production environments.

---

## 🛠️ Configuration Options

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your Azure OpenAI API key | `sk-...` |
| `OPENAI_API_BASE` | Azure OpenAI endpoint URL | `https://myresource.openai.azure.com/` |
| `OPENAI_API_VERSION` | API version | `2024-06-01-preview` |
| `OPENAI_DEPLOYMENT_NAME` | Model deployment name | `gpt-4o-mini` |

### Customization Options

- **Model Selection**: Change `OPENAI_DEPLOYMENT_NAME` to use different models
- **API Version**: Update `OPENAI_API_VERSION` for newer API features
- **Output Format**: Modify `writer_module.py` to customize report structure

---

## 🔧 Development & Extension

### Current Limitations (By Design)
- **Web Search**: Uses mock data to avoid API costs during development
- **Email Delivery**: Mocked to prevent accidental email sends
- **Tracing**: OpenAI tracing disabled to avoid Azure compatibility issues

### Extension Ideas

#### 🌐 Real Web Integration
```python
# Replace mock_web_search with real implementation
def real_web_search(query):
    # Integrate with Bing Search API, Google Search API, etc.
    pass
```

#### 📧 Email Integration
```python
# Connect to real email services
def send_email_sendgrid(report):
    # Implement SendGrid integration
    pass

def send_email_smtp(report):
    # Implement SMTP integration
    pass
```

#### 📊 Enhanced Features
- **Streaming Responses**: Real-time report generation display
- **Multi-format Export**: PDF, Word, HTML report outputs
- **Research Templates**: Pre-configured research workflows
- **Citation Tracking**: Automatic source attribution
- **Report Versioning**: Track and compare research iterations

#### ☁️ Cloud Deployment
- **Azure App Service**: Deploy as a web application
- **Container Apps**: Containerized deployment
- **Function Apps**: Serverless research triggers
- **Logic Apps**: Workflow automation integration

---

## 🔍 Troubleshooting

### Common Issues

#### Azure OpenAI Connection
```bash
# Error: Unauthorized (401)
# Solution: Verify your API key and endpoint URL
```

#### Python Version Compatibility
```bash
# Error: Package installation fails
# Solution: Use Python 3.11 or 3.12
```

#### Gradio UI Issues
```bash
# Error: UI doesn't load
# Solution: Check if port 7860 is available
```

### Debug Mode
Enable verbose logging by modifying `main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📈 Performance Considerations

### Cost Optimization
- Mock services reduce Azure OpenAI API calls during development
- Consider implementing request caching for repeated research topics
- Monitor token usage for cost control

### Scalability
- Async processing supports parallel agent execution
- Stateless design enables horizontal scaling
- Consider implementing request queuing for high-volume usage

---

## 🧪 Testing

### Running Tests
```bash
# Unit tests
python -m pytest tests/

# Integration tests
python -m pytest tests/integration/

# Full pipeline test
python test_pipeline.py
```

### Test Coverage
- Agent functionality validation
- Azure OpenAI integration testing
- Pipeline orchestration verification
- Mock service behavior confirmation

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure backward compatibility

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Harsh Vardhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **Microsoft Azure** for OpenAI services
- **OpenAI** for the powerful language models
- **Gradio** team for the excellent UI framework
- **Python** community for the amazing ecosystem

---

## 🔗 Useful Links

- [Azure OpenAI Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Gradio Documentation](https://gradio.app/docs/)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/harshv2013/Agentic-AI-Deep-Research-Azure.git/issues) page
2. Create a new issue with detailed information
3. Join our [Discussions](https://github.com/harshv2013/Agentic-AI-Deep-Research-Azure.git/discussions) for community support

---

**⭐ Star this repo if you find it helpful!**