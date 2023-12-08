import turtle
from random import randint
import time

myPen = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)

myPen.speed(0)
myPen.hideturtle()


def text(pesan, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(pesan, align="left", font=FONT)

# This function draws a box by drawing each side of the square and using the fill function


def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


# Here is an example of how to draw a box
# box(boxSize)


# Here are some instructions on how to move "myPen" around before drawing a box.
# myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()

# membuat labirin dengan pixelart (using a "list of lists")
palette = ["#FFFFFF", "#000000", "#00ffff", "#ff00ff", "#AAAAAA"]
labirin = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
labirin.append([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1])
labirin.append([1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
labirin.append([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1])
labirin.append([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1])
labirin.append([1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1])
labirin.append([1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1])
labirin.append([1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1])
labirin.append([1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1])
labirin.append([1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1])
labirin.append([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1])
labirin.append([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1])
labirin.append([1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1])
labirin.append([1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin.append([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2])
labirin.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

labirin1 = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
labirin1.append([1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin1.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
labirin1.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
labirin1.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

labirin2 = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
labirin2.append([1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
labirin2.append([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
labirin2.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2])
labirin2.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


def drawMaze(labirin):
    boxSize = 15
    # posisi myPen di atas kiri layar
    myPen.penup()
    myPen.goto(-130, 130)
    myPen.setheading(0)
    for i in range(0, len(labirin)):
        for j in range(0, len(labirin[i])):
            myPen.color(palette[labirin[i][j]])
            box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize*len(labirin[i]))
        myPen.setheading(0)
        myPen.pendown()

# backtracking yang mencoba satu satu kemungkinan hingga berhasil menemukan exit


def exploreMaze(labirin, row, col):
    if labirin[row][col] == 2:
        # telah menemukan exit
        return True
    elif labirin[row][col] == 0:  # jalan buntu
        labirin[row][col] = 3
        myPen.clear()
        drawMaze(labirin)
        myPen.getscreen().update()

        if row < len(labirin)-1:
            # menelusuri jalan di bawah
            if exploreMaze(labirin, row+1, col):
                return True

        if row > 0:
            # menelusuri jalan di atas
            if exploreMaze(labirin, row-1, col):
                return True

        if col < len(labirin[row])-1:
            # menelusuri jalan di kanan
            if exploreMaze(labirin, row, col+1):
                return True

        if col > 0:
            # menelusuri jalan di kiri
            if exploreMaze(labirin, row, col-1):
                return True

        # runut baliknya
        labirin[row][col] = 4
        myPen.clear()
        drawMaze(labirin)
        myPen.getscreen().update()
        time.sleep(0.25)
        print("Backtrack")


# Labirin 1
drawMaze(labirin)

# Labirin 2
drawMaze(labirin1)

# Labirin 3
drawMaze(labirin2)

solved = exploreMaze(labirin, 0, 1)
if solved:
    print("Labirin 1 selesai")
    text("Labirin 1 selesai", -100, -150, 20)
else:
    print("Labirin 1 tidak bisa diselesaikan")
    text("Labirin 1 tidak bisa diselesaikan", -130, -150, 20)
time.sleep(2)
solved = exploreMaze(labirin1, 0, 1)
if solved:
    print("Labirin 2 selesai")
    text("Labirin 2 selesai", -100, -150, 20)
else:
    print("Labirin 2 tidak bisa diselesaikan")
    text("Labirin 2 tidak bisa diselesaikan", -130, -150, 20)
time.sleep(2)
solved = exploreMaze(labirin2, 0, 1)
if solved:
    print("Labirin 3 selesai")
    text("Labirin 3 selesai", -100, -150, 20)
else:
    print("Labirin 3 tidak bisa diselesaikan")
    text("Labirin 3 tidak bisa diselesaikan", -130, -150, 20)


myPen.hideturtle()
turtle.done()
