from google.adk.agents.llm_agent import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "basic_agent_CLI"
USER_ID = "user_001"
SESSION_ID = "session_001"


# step 1 : get the agent
async def get_agent (): 

    root_agent = Agent(
        model="gemini-2.5-flash-lite",          # The AI model to use
        name='basic_agent',                      # Agent identifier
        description="This a basic ai agent",    # What the agent does
        instruction="Your are a helpful assistant", # How the agent should behave
        tools=[],                               # List of tools the agent can use
    )
    return root_agent



# step 2 : run the agent
async def main(query): 
    
    # create memory session
    session_services = InMemorySessionService()
    await session_services.create_session(
        app_name=APP_NAME, 
        user_id=USER_ID, 
        session_id=SESSION_ID
        ) 
    
    # get the agent
    root_agent = await get_agent()
    
    # create runner instance
    runner = Runner(
        app_name=APP_NAME, 
        agent=root_agent, 
        session_service=session_services
        ) 
    
    # formate the query
    content = types.Content(
        role="user",
        parts=[types.Part(text=query)]
    )
    # run the agent
    events = runner.run_async(
        new_message= content ,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    
    # print the response
    async for event in events : 
        if event.is_final_response():
           final_response = event.content.parts[0].text 
           print( "Agent Response : ", final_response)
           
if __name__ == "__main__":
    asyncio.run(main("what are the advatages of using multi agent system"))