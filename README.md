# Google ADK Agents

Collection of simple Google ADK agent examples for learning and experimentation.

## Included Examples

- `01_basic_agent_setup_web`: minimal web-oriented agent definition
- `02_basic_agent_setup_CLI`: minimal CLI runner using an in-memory session

## Requirements

- Python 3.12 or compatible version in your environment
- Google ADK installed
- A valid Google API key or model access configured for ADK

## Setup

1. Create and activate a virtual environment.
2. Install the required packages:

```bash
pip install google-adk google-genai python-dotenv
```

3. Create a `.env` file inside each example folder that needs it.

Example:

```env
GOOGLE_API_KEY=your_api_key_here
```

## Run The CLI Example

From the repo root:

```bash
python 02_basic_agent_setup_CLI/agent.py
```

## Web Example

The web example currently defines a root agent in:

- `01_basic_agent_setup_web/agent.py`

Use it as the starting point for an ADK web app or server integration.

## Notes

- `.env`, `.venv`, `.adk`, and Python cache files are excluded from git.
- These examples use `gemini-2.5-flash-lite` in the current agent configuration.
