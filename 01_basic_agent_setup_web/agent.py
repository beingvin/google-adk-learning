from google.adk.agents.llm_agent import Agent



root_agent = Agent(
    model="gemini-2.5-flash-lite",          # The AI model to use
    name='basic_agent',                      # Agent identifier
    description="This a basic ai agent",    # What the agent does
    instruction="Your are a helpful assistant", # How the agent should behave
    tools=[],                               # List of tools the agent can use
)
