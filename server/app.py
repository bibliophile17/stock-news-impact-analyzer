import os
from fastapi import FastAPI
from src.environment import NewsEnv
from src.models import SentimentAction

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

app = FastAPI()
env = NewsEnv()

@app.post("/reset")
def reset():
    print("START")   # structured log
    obs = env.reset()
    print("END")     # structured log
    return obs.dict()

@app.post("/step")
def step(action: SentimentAction):
    print("STEP")    # structured log
    obs, reward, done, _ = env.step(action)
    return {"observation": obs.dict(), "reward": reward, "done": done}

@app.get("/state")
def state():
    return env.state().dict()

# -------------------------------
# Main entry point
# -------------------------------
def main():
    """Entry point required by OpenEnv and Hugging Face"""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
