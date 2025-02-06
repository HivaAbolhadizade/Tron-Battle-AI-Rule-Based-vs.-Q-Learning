# Tron Battle AI: Rule-Based vs. Q-Learning

## Overview

This project is the final report for the Artificial Intelligence Course at Bahonar University of Kerman in the Fall 2024 semester. It compares two decision-making approaches in the Tron Battle game:

1. A Simple Rule-Based Algorithm

2. A Reinforcement Learning (Q-Learning) Approach

The study explores their strengths, weaknesses, and performance in different scenarios.

## Introduction

Tron Battle is a classic arcade game where players maneuver motorcyclists leaving light trails. The objective is to make opponents crash into obstacles. Due to its fast-paced nature, decision-making plays a crucial role in the game. This project examines two AI-driven strategies for making decisions in the game environment.

## Approaches

1. Rule-Based Algorithm

This approach follows predefined rules to determine the next move:

The game grid is represented as a 30x20 array.

The agent evaluates valid moves and picks a direction based on available space.

It is fast but lacks adaptability to complex situations.

2. Reinforcement Learning (Q-Learning)

Q-Learning is a reinforcement learning technique that allows an agent to learn optimal moves over time. It works by:

Assigning Q-values to state-action pairs.

Updating values using the Bellman equation.

Utilizing an epsilon-greedy policy for exploration and exploitation.

This approach allows the agent to learn from past decisions and improve performance dynamically.

Simple Algorithm: Works well in open environments but struggles with obstacles.

Q-Learning: Adapts and improves over time, handling dynamic environments better.

## Trade-offs
Q-Learning requires more computational resources and training time.

## Conclusion & Future Work

Rule-based AI is effective for basic problems.

Q-Learning AI is preferable for complex environments requiring adaptation.

## Future Improvements:

Hybrid approaches combining rule-based and Q-Learning.

Deep Q-Learning (DQN) to handle larger state spaces.
