<<<<<<< HEAD
# Stock Market News Impact Analyzer

## Description

Classifies financial news headlines into sentiment categories (positive, negative, neutral).

## Action Space

- sentiment: "positive", "negative", "neutral"

## Observation Space

- headline: string
- ticker: string

## Tasks

- Easy: clear sentiment headlines
- Medium: mixed language headlines
- Hard: sarcasm or indirect impact

## Reward

- 1.0 for correct classification
- 0.5 partial credit (neutral case in medium task)
- 0.0 otherwise

## Baseline

Naive agent always predicts "neutral". Produces reproducible scores.

## Deployment

Runs on Hugging Face Spaces with Docker.
=======
---
title: Stock News Impact Analyzer
emoji: 💻
colorFrom: red
colorTo: pink
sdk: docker
pinned: false
license: apache-2.0
short_description: 'OpenEnv environment for financial news sentiment analysis '
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> 913030aff6e9d0f2bd8f854f316a2306fa47bf44
