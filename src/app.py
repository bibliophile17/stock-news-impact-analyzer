from fastapi import FastAPI
from src.environment import NewsEnv
from src.models import SentimentAction
import gradio as gr

# Initialize FastAPI and environment
app = FastAPI()
env = NewsEnv()

# Root route
@app.get("/")
def home():
    return {"message": "Stock News Impact Analyzer API is running. Use /reset, /step, /state."}

# Reset endpoint
@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

# Step endpoint
@app.post("/step")
def step(action: SentimentAction):
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

# Launch Gradio on the same port Hugging Face expects
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
