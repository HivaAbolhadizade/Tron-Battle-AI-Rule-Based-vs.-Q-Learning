import sys
import random
import numpy as np

# Action definitions and movement mapping
ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
ACTION_MAP = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

# Parameters
ALPHA = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 0.1  # Probability for exploration

# Initialize Q-table
Q = {}

def get_state(x, y, grid):
    """Represent the state as a tuple of position and grid."""
    return (x, y, tuple(tuple(row) for row in grid))

def get_valid_actions(x, y, grid):
    """Get all valid actions from the current position."""
    actions = []
    for action, (dx, dy) in ACTION_MAP.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not grid[nx][ny]:
            actions.append(action)
    return actions

def choose_action(state, valid_actions):
    """Use epsilon-greedy policy to select an action."""
    if random.random() < EPSILON:
        return random.choice(valid_actions)  # Explore
    q_values = [Q.get((state, action), 0) for action in valid_actions]
    return valid_actions[np.argmax(q_values)]  # Exploit

def update_q_table(state, action, reward, next_state, next_valid_actions):
    """Update Q-value for the current state-action pair."""
    max_next_q = max([Q.get((next_state, a), 0) for a in next_valid_actions], default=0)
    Q[(state, action)] = Q.get((state, action), 0) + ALPHA * (reward + GAMMA * max_next_q - Q.get((state, action), 0))

# Grid dimensions
GRID_WIDTH = 30
GRID_HEIGHT = 20

# Initialize the game grid
grid = [[False] * GRID_HEIGHT for _ in range(GRID_WIDTH)]
agent_x, agent_y = 0, 0

# Main loop
while True:
    # Input reading
    n, p = map(int, input().split())
    positions = []
    for i in range(n):
        x_prev, y_prev, x_curr, y_curr = map(int, input().split())
        positions.append((x_curr, y_curr))
        if i == p:
            agent_x, agent_y = x_curr, y_curr

    # Update the grid based on positions
    for x, y in positions:
        if x != -1 and y != -1:
            grid[x][y] = True

    # Get the current state and valid moves
    state = get_state(agent_x, agent_y, grid)
    valid_actions = get_valid_actions(agent_x, agent_y, grid)

    if not valid_actions:
        # If no valid moves, end the game with a dummy action
        print("UP")
        continue

    # Decide the next action
    action = choose_action(state, valid_actions)
    dx, dy = ACTION_MAP[action]
    next_x, next_y = agent_x + dx, agent_y + dy

    # Assign reward (positive for valid moves, negative for invalid moves)
    reward = 1 if (0 <= next_x < GRID_WIDTH and 0 <= next_y < GRID_HEIGHT and not grid[next_x][next_y]) else -10

    # Update the grid and Q-table
    if reward > 0:
        grid[next_x][next_y] = True

    next_state = get_state(next_x, next_y, grid)
    next_valid_actions = get_valid_actions(next_x, next_y, grid)
    update_q_table(state, action, reward, next_state, next_valid_actions)

    # Output the chosen action
    print(action)
