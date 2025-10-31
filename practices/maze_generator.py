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
        #add "1111" to row list. This represents the sides, with 1 being wall and 0 being no wall, starting at the top and moving clockwise
        row.append('1111')
    #add row list to maze list
    maze.append(row)
#pick a random x coordinate from the maze
x = r.randint(1,size)
#pick a random y coordinate from the maze
y = r.randint(1,size)
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
    #remove items that match an item in the visited list
    #pick a random item from the neighbors list
    #remove wall between current cell and chosen neighbor cell
    #set x and y coordinate to that of the chosen neighbor
    