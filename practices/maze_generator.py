#BZ 1st maze generator
#import libraries
import random as r
#create empty maze list
maze = []
#create size variable
size = 10
#loop through y coordinates of the maze
for y in range(0,size):
    #empty row list
    row = []
    #loop through x coordinates of the maze
    for x in range(0,size):
        #add [1,1,1,1] to row list. This represents the sides, with 1 being wall and 0 being no wall, starting at the top and moving clockwise
        row.append([1,1,1,1])
    #add row list to maze list
    maze.append(row)
#pick a random x coordinate from the maze
x = r.randint(0,size-1)
#pick a random y coordinate from the maze
y = r.randint(0,size-1)
#create an empty "visited" list
visited = []
#create an empty "stack" list
stack = []
#loop until visited list contains all cells
while len(visited) < size ** 2:
    #add current x and y coordinate to the visited list and a "stack" list
    visited.append([x,y])
    stack.append([x,y])
    #create a list of all neighbor cells
    neighbors = [[x,y+1],[x-1,y],[x+1,y],[x,y-1]]
    #remove items that match an item in the visited list OR contain coords outside of the maze
    for i in neighbors:
        if i in visited:
            neighbors.remove(i)
        elif -1 in i:
            neighbors.remove(i)
        elif size in i:
            neighbors.remove(i)
    #pick a random item from the neighbors list
    neighbor = r.choice(neighbors)
    
    #remove wall between current cell and chosen neighbor cell
    if neighbor[0] == x - 1:
        neighbor_remove = 1
        self_remove = 3
    elif neighbor[0] == x+1:
        neighbor_remove = 3
        self_remove = 1
    elif neighbor[0] == x:
        if neighbor[1] == y-1:
            neighbor_remove = 0
            self_remove = 2
        elif neighbor[1] == y+1:
            neighbor_remove = 2
            self_remove = 0
    maze[y][x][neighbor_remove] = 0
    maze[y][x][self_remove] = 0
    #set x and y coordinate to that of the chosen neighbor
    x,y = neighbor
print(visited)