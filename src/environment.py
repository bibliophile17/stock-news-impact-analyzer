import random
from src.models import NewsObservation, SentimentAction, EnvState

class NewsEnv:
    def __init__(self):
        self.step_count = 0
        self.episode_id = "ep1"
        self.headlines = [
            {"headline":"Company X reports record profits","ticker":"COMPX","label":"positive"},
            {"headline":"Company Y faces bankruptcy","ticker":"COMPY","label":"negative"},
            {"headline":"Company Z beats earnings but warns of layoffs","ticker":"COMPZ","label":"neutral"},
            {"headline":"Competitor B launches new product, Company C stock dips","ticker":"COMPZ","label":"negative"},
            {"headline":"Company D finally delivers a product that works","ticker":"COMPD","label":"positive"}
        ]
        self.current = None

    def reset(self):
        self.step_count = 0
        self.current = random.choice(self.headlines)
        return NewsObservation(**self.current)

    def step(self, action: SentimentAction):
        self.step_count += 1
        reward = self._reward(action)
        done = self.step_count >= 1
        return NewsObservation(**self.current), reward, done, {}

    def state(self):
        return EnvState(episode_id=self.episode_id, step_count=self.step_count)

    def _reward(self, action):
        label = self.current["label"]
        if action.sentiment == label:
            return 1.0
        elif action.sentiment == "neutral" and label in ["positive","negative"]:
            return 0.5
        else:
            return 0.0
