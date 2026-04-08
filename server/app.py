from fastapi import FastAPI
import gradio as gr
from src.environment import NewsEnv
from src.models import SentimentAction

# Initialize FastAPI and environment
app = FastAPI()
env = NewsEnv()

# Root route
@app.get("/")
def home():
    return {"message": "Stock News Impact Analyzer API is running. Use /reset, /step, /state."}

# Reset endpoint (POST required by validator)
@app.post("/reset")
def reset():
    print("START")
    obs = env.reset()
    print("END")
    return obs.dict()

# Step endpoint
@app.post("/step")
def step(action: SentimentAction):
    print("STEP")
    obs, reward, done, _ = env.step(action)
    return {"observation": obs.dict(), "reward": reward, "done": done}

# State endpoint
@app.get("/state")
def state():
    return env.state().dict()

# -------------------------------
# Gradio UI for hackathon judges
# -------------------------------
def reset_env():
    return env.reset().dict()

def step_env(sentiment):
    action = SentimentAction(sentiment=sentiment)
    obs, reward, done, _ = env.step(action)
    return {"observation": obs.dict(), "reward": reward, "done": done}

def state_env():
    return env.state().dict()

with gr.Blocks() as demo:
    gr.Markdown("# 📈 Stock News Impact Analyzer")
    gr.Markdown("Interact with the environment using Reset, Step, and State.")

    with gr.Row():
        reset_btn = gr.Button("Reset")
        state_btn = gr.Button("State")

    sentiment = gr.Radio(["positive", "negative", "neutral"], label="Choose sentiment")
    step_btn = gr.Button("Step")

    output = gr.JSON(label="Output")

    reset_btn.click(fn=reset_env, outputs=output)
    state_btn.click(fn=state_env, outputs=output)
    step_btn.click(fn=step_env, inputs=sentiment, outputs=output)

# -------------------------------
# Main entry point
# -------------------------------
def main():
    """Entry point required by OpenEnv"""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
