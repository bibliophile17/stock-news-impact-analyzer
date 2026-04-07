from pydantic import BaseModel

class NewsObservation(BaseModel):
    headline: str
    ticker: str

class SentimentAction(BaseModel):
    sentiment: str  # "positive", "negative", "neutral"

class EnvState(BaseModel):
    episode_id: str
    step_count: int

