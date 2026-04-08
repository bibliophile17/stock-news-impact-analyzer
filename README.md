---
title: Stock News Impact Analyzer
emoji: 📈
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "1.0.0"
python_version: "3.10"
app_file: src/app.py
pinned: false
license: mit
---

## Problem Statement

Chosen track: **Financial markets react instantly to news, but traders struggle to measure its true impact. The Stock News Impact Analyzer creates a clear, testable environment where agents classify headlines by sentiment and receive rewards based on market impact. This bridges the gap between raw news and actionable trading insights, enabling smarter, sentiment‑aware decision making.**  
The goal is to design a clear, testable environment where agents can analyze stock news and respond with sentiment actions.

---

## Environment Design

- **Observation**: A stock news headline and ticker symbol.
- **Action**: Sentiment choice (`positive`, `negative`, `neutral`).
- **Reward**:
  - Positive → +1
  - Negative → -1
  - Neutral → 0
- **Episode State**: Tracks episode ID and step count.

---

## API Endpoints (OpenEnv Standard)

- `GET /reset` → Returns initial observation.
- `POST /step` → Accepts sentiment action, returns observation, reward, done.
- `GET /state` → Returns current episode state.

These endpoints comply with the OpenEnv interface and are validator‑ready.

---

## Gradio Interface

Judges can interact with the environment visually:

- **Reset button** → Starts a new episode.
- **State button** → Shows current episode state.
- **Step button** → Takes sentiment input and returns reward + observation.
- **Output panel** → Displays JSON results.

---

## How to Run Locally

```bash
uv run server
```
