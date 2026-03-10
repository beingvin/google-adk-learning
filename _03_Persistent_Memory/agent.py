from google.adk.agents.llm_agent import Agent
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "database_session_agent"
USER_ID = "user_001"
SESSION_ID = "session_001"
DB_URL = "sqlite+aiosqlite:///agent_data.db"  # auto-created on first run

root_agent = Agent(
    model="gemini-2.0-flash",
    name="database_session_agent",
    description="An agent with persistent memory using SQLite.",
    instruction="You are a helpful assistant. Remember everything the user tells you across conversations.",
    tools=[],
)

async def main():

    # ✅ DatabaseSessionService instead of InMemorySessionService
    session_service = DatabaseSessionService(db_url=DB_URL)

    # check if session already exists, if not create one
    existing_session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    if existing_session is None:
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID,
            state={"user_name": "John"}  # initial state
        )
        print("✅ New session created")
    else:
        session = existing_session
        print("✅ Existing session loaded")

    print("Session State:", session.state)

    runner = Runner(
        app_name=APP_NAME,
        agent=root_agent,
        session_service=session_service
    )

    # --- chat loop ---
    print("\nType 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        async for event in runner.run_async(
            new_message=types.Content(
                role="user",
                parts=[types.Part(text=user_input)]
            ),
            user_id=USER_ID,
            session_id=SESSION_ID
        ):
            if event.is_final_response():
                if event.content and event.content.parts:
                    print("Agent:", event.content.parts[0].text)

    # --- show final state ---
    final_session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print("\nFinal Session State:", final_session.state)

if __name__ == "__main__":
    asyncio.run(main())