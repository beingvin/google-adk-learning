# Google ADK Agents 🤖

A collection of agentic workflow examples built using **Google's Agent Development Kit (ADK)**. This repository is designed for learning, testing multi-agent systems, and experimenting with Gemini models.

---

## 📂 Project Structure

To comply with Python/Pydantic identifier requirements while maintaining chronological order, all project folders use an **underscore prefix**.

- **`_01_basic_agent_setup_web`** — A minimal web-ready agent definition.
- **`_02_basic_agent_setup_CLI`** — A lightweight CLI implementation using an in-memory session.

---

## 🚀 Quick Start

### 1. Prerequisites

- **Python:** 3.12+
- **API Key:** Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).
- **Environment:** Ensure you have a virtual environment activated.

### 2. Installation
```bash
pip install google-adk google-genai python-dotenv
```

### 3. Configuration

Each example folder requires its own `.env` file. Create one and add your credentials:
```env
GOOGLE_API_KEY=your_api_key_here
# Optional: Set to 'true' if using Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=false
```

---

## 🖥️ Running the Examples

### Web UI Mode (Recommended)

Launch the built-in Google ADK dashboard to interact with your agents visually.
```bash
# Option 1: Run on default port (8000)
adk web

# Option 2: Run on a custom port
adk web --port 5000
```

Access the UI at: `http://localhost:<port_number>`

### CLI Mode

For quick terminal-based testing without the web interface:
```bash
python _02_basic_agent_setup_CLI/agent.py
```

---

## 🧪 Technical Details

| Component | Specification |
|---|---|
| LLM Model | `gemini-2.0-flash` |
| Framework | Google ADK |
| Validation | Pydantic V2 |
| Environment | `python-dotenv` |

> [!IMPORTANT]
> **Naming Rule:** Folder names must start with a letter or underscore (e.g., `_01_name`) because ADK uses these names as internal Python identifiers. Starting with a digit will trigger a `ValidationError`.

---

## 📝 Roadmap

- [x] Basic Web & CLI Setup
- [ ] Multi-agent Collaboration
- [ ] Tool-calling (Function Calling)
- [ ] RAG (Retrieval Augmented Generation) implementation

---

## 🛡️ License

MIT License — Feel free to use this for your own learning and projects!