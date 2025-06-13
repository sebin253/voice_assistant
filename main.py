from dotenv import load_dotenv
from livekit import agents
from session_handler import entrypoint

load_dotenv()

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
