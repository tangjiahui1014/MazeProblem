# Describe: The definition of the maze map
# Author: Jiahui Tang
# Date: 2017-1-3

# define the directions
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# define the help functions
def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
	return maze[pos[0]][pos[1]] == 0

# define the start position and the end position
start = (1, 1)
end = (18, 18)

# define marks on the map
# 0 ---------- can pass
# 1 ---------- wall
# 2 ---------- invalid(through)
maze1 = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1],
  [1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1],
  [1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
  [1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1],
  [1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1],
  [1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1],
  [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
  [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
  [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
  [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
  [1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
  [1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
  [1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# You can also add more maps
