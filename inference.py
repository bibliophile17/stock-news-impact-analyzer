import os
from src.environment import NewsEnv
from src.models import SentimentAction

# Mandatory environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

env = NewsEnv()

def main():
    # START log
    print("[START]")
    obs = env.reset()
    print(obs.model_dump())   # use model_dump instead of dict()

    # STEP log
    action = SentimentAction(sentiment="positive")
    obs, reward, done, _ = env.step(action)
    print("[STEP]")
    print({"observation": obs.model_dump(), "reward": reward, "done": done})

    # END log
    print("[END]")

if __name__ == "__main__":
    main()
