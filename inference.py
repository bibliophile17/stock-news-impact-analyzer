from src.models import NewsObservation, SentimentAction
from src.environment import NewsEnv

def baseline_agent(obs: NewsObservation):
    # Naive baseline: always predict neutral
    return SentimentAction(sentiment="neutral")

if __name__ == "__main__":
    env = NewsEnv()
    obs = env.reset()
    action = baseline_agent(obs)
    obs, reward, done, _ = env.step(action)
    print("Headline:", obs.headline)
    print("Predicted:", action.sentiment)
    print("Reward:", reward)
