import os
import sys
from openai import OpenAI

# Required environment variables with defaults
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    print("HF_TOKEN not set", file=sys.stderr)
    sys.exit(1)

# Initialize OpenAI client
client = OpenAI(api_key=HF_TOKEN, base_url=API_BASE_URL)

def main():
    try:
        # START
        print("[START]")
        obs = {"headline": "Company X reports record profits", "ticker": "COMPX"}
        print(obs)

        # STEP
        print("[STEP]")
        # Example LLM call
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "Analyze sentiment: Company X reports record profits"}],
        )
        sentiment = response.choices[0].message.content
        reward = 1.0 if "positive" in sentiment.lower() else 0.0
        print({"observation": obs, "reward": reward, "done": True})

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    finally:
        # END
        print("[END]")

if __name__ == "__main__":
    main()
