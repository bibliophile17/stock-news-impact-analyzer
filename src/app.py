from fastapi import FastAPI
from src.environment import NewsEnv
from src.models import SentimentAction

app = FastAPI()
env = NewsEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: SentimentAction):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
def state():
    return env.state()
