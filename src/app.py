from fastapi import FastAPI, Request

app = FastAPI()

# Reset endpoint: returns initial observation/state
@app.get("/reset")
def reset():
    return {"observation": "environment reset", "state": "ready"}

# Step endpoint: accepts an action and returns reward + new state
@app.post("/step")
async def step(request: Request):
    data = await request.json()
    action = data.get("action", None)
    # Dummy reward logic for hackathon baseline
    reward = 0.5 if action else 0.0
    return {"reward": reward, "state": "running"}

# State endpoint: returns current episode state
@app.get("/state")
def state():
    return {"episode": "active", "progress": "baseline agent running"}

@app.get("/")
def home():
    return {"message": "Stock News Impact Analyzer API is running. Use /reset, /step, /state."}
