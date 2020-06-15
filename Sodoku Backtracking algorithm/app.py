import turtle
from time import sleep
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

topLeft_x = -150
topLeft_y = 150
myPen = turtle.Turtle()


def erase(x,y, name, font, align='left', reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(x,y)
    eraser.write(name, font=('Arial', 18, 'normal'), align=align)
    return eraser

def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)

    # A procedure to draw the grid on screen using Python Turtle


def drawGrid(grid):
    intDim = 35
    for row in range(0, 10):
        if (row % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y - row * intDim)
        myPen.pendown()
        myPen.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)
    for col in range(0, 10):
        if (col % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x + col * intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)

    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] != 0:
                text(grid[row][col], topLeft_x + col * intDim + 9, topLeft_y - row * intDim - intDim + 8, 18)





def solve(bo):
    intDim = 35
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find


    for i in range(1,10):
        eraseble = 0
        if valid(bo, i, (row, col)):
            eraseble = erase(topLeft_x + col * intDim + 9, topLeft_y - row * intDim - intDim + 8, i,
                             font=("Arial", 20, "normal"), align="left")
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
        if eraseble != 0:
            eraseble.clear()
    return False


def valid(bo, num, pos):
    # Check row
    intDim = 35
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            text(' ', topLeft_x + pos[1] * intDim + 9, topLeft_y - pos[0] * intDim - intDim + 8, 18)
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            text(' ', topLeft_x + pos[1] * intDim + 9, topLeft_y - pos[0] * intDim - intDim + 8, 18)
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def main():

    myPen.speed(0)
    myPen.color("#000000")
    myPen.hideturtle()
    drawGrid(grid)
    myPen.getscreen().update()
    solve(grid)
    sleep(2)

if __name__ == '__main__':
    main()