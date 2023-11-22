import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Board dim
rows, cols = 600, 600

# Random board
def random_board():
    return np.random.choice([0, 1], size=(rows, cols))

# Function to evolve the board to the next step
def evolve(board):
    new_board = board.copy()
    for i in range(rows):
        for j in range(cols):
            # Count the number of live neighbors
            neighbors = np.sum(board[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - board[i, j]
            # Apply the rules of the game
            if board[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_board[i, j] = 0
            elif board[i, j] == 0 and neighbors == 3:
                new_board[i, j] = 1
    return new_board

# Initialize the board
board = random_board()

# Function to update the visualization at each step
def update(data):
    global board
    new_board = evolve(board)
    mat.set_data(1 - new_board)  # Invert colors
    board = new_board
    return [mat]

# Configure the visualization
fig, ax = plt.subplots(figsize=(6, 6))  
mat = ax.matshow(1 - board[:600, :600], cmap='plasma')  # Change the colormap to 'plasma'
ax.set_axis_off()  # Remove axes

def update(data):
    global board
    new_board = evolve(board)
    mat.set_data(1 - new_board[:600, :600])  
    board = new_board
    return [mat]

ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)

ani.save('conway_game_of_life.gif', writer='imagemagick', fps=20, dpi=100)  

plt.show()
