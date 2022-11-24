import time
import turtle

turtle.shape('turtle')
turtle.bgcolor('aqua')
turtle.color('light green')
turtle.turtlesize(outline=3)
turtle.pencolor('green')
turtle.turtlesize(5, 5, 1)
turtle.back(250)
turtle.right(90)
turtle.forward(200)

for i in range(3, 15):
	turtle.left(90)
	turtle.forward(500)

time.sleep(5)