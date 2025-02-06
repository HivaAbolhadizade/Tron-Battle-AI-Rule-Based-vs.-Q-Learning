import sys

# Grid dimensions
GRID_WIDTH = 30
GRID_HEIGHT = 20

# Directions
DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

# Initialize the grid
grid = [[False] * GRID_HEIGHT for _ in range(GRID_WIDTH)]

# Check if a move is valid
def is_valid_move(x, y):
    return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT and not grid[x][y]

# Determine the next move
def decide_next_move(x, y):
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny):
            return direction
    return "UP"  # Default move if no valid options

# Main game loop
while True:
    n, p = map(int, input().split())
    positions = []

    for i in range(n):
        x_prev, y_prev, x_curr, y_curr = map(int, input().split())
        positions.append((x_prev, y_prev, x_curr, y_curr))

        if x_prev != -1:  # Only update the grid if the player is still active
            grid[x_prev][y_prev] = True
            grid[x_curr][y_curr] = True

    _, _, x, y = positions[p]

    # Decide and output the next move
    print(decide_next_move(x, y))
