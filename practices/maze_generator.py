#BZ 1st maze generator
#import libraries
import random as r
import turtle as t
#create empty maze list
maze = []
#create size variable
size = 15
#create function for neighbors choice
def find_neighbors(x, y):
    neighbors = []
    #create a list of all neighbor cells
    neighbors = [[x,y+1],[x-1,y],[x+1,y],[x,y-1]]
    loop_neighbors = [[x,y+1],[x-1,y],[x+1,y],[x,y-1]]
    #remove items that match an item in the visited list OR contain coords outside of the maze
    for i in loop_neighbors:
        if i in visited:
            neighbors.remove(i)
        elif i[0] < 0 or i[1] < 0:
            neighbors.remove(i)
        elif i[0] >= size or i[1] >= size:
            neighbors.remove(i)
    #return neighbors
    return neighbors
    
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
maze[size-1][0][0] = 0
#set x and y starting coords
x, y = 0, 0
#create an empty "visited" list
visited = []
#create an empty "stack" list
stack = []
#loop until visited list contains all cells
exit = False
while len(visited) < size ** 2:
    #add current x and y coordinate to the visited list and a "stack" list
    visited.append([x,y])
    neighbors = []
    #loop while we have no neighbors
    while not neighbors:
        #find neighbors
        neighbors = find_neighbors(x,y)
        #if there are neighbors
        if neighbors:
            #pick a random neighbor
            neighbor = r.choice(neighbors)
            #exit loop
            break
        #if there are no neighbors
        else:
            #if there are items in the stack
            if stack:
                #remove top item from stack and update our x and y coords to it
                x, y = stack.pop()
            else:
                #exit main loop
                exit = True
                break
    if exit:
        break
    
    stack.append(neighbor)
    print(neighbor)
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
    maze[neighbor[1]][neighbor[0]][neighbor_remove] = 0
    maze[y][x][self_remove] = 0
    #set x and y coordinate to that of the chosen neighbor
    x,y = neighbor
t.hideturtle()
t.penup()
t.speed(0)
t.goto(-10 * size,10 * size)
for row in maze:
    for cell in row:
        t.penup()
        if cell[0] == 1:
            t.pendown()
        t.forward(size*2)
    t.penup()
    t.goto(-10 * size,t.ycor()-size*2)
t.goto(-10 * size,12 * size)
t.right(90)
for row in maze:
    for cell in row:
        t.penup()
        if cell[3] == 1:
            t.pendown()
        t.forward(size*2)
        t.penup()
        t.backward(size*2)
        t.left(90)
        t.forward(size*2)
        t.right(90)
    t.goto(-10 * size,t.ycor()-size*2)
t.penup()
t.goto(10 * size,12 * size)
t.pendown()
t.forward(20 * size)
t.penup()
t.goto(-10*size,12*size)
t.left(90)
t.pendown()
t.forward(size * 18)

print(maze)
print(len(visited))
print(visited)
t.done()