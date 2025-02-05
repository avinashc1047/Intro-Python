# Project 3- Turtle Alphabet
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

###############################################################
# Part 1) Setup
# Load turtle module, move it to left side, make turtle faster
import turtle
turtle.reset()
turtle.color('red')
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed(0)
turtle.pensize(10)

###############################################################
# Part 2) Drawing
# Write the code for each letter below

# First letter
# ...
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)

# Leave space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Second letter
turtle.left(90)
turtle.forward(50)
turtle.right(135)
turtle.forward(60)
turtle.setheading(0)
turtle.left(90)
turtle.forward(50)

#leave
turtle.penup()
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)
turtle.pendown()

#third letter
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)
turtle.backward(50)

#leave
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

#fourth letter
turtle.left(90)
turtle.forward(50)
turtle.backward(20)
turtle.right(90)
turtle.forward(30)

#leave
turtle.penup()
turtle.setheading(270)
turtle.forward(25)
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

#fifth
turtle.circle(16)

#leave
turtle.penup()
turtle.forward(40)
turtle.pendown()

#6
turtle.left(90)
turtle.forward(30)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.circle(1)

#leave
turtle.penup()
turtle.backward(50)
turtle.right(90)
turtle.forward(30)
turtle.pendown()

#7
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)
turtle.backward(50)
turtle.left(90)
turtle.forward(50)
turtle.backward(50)

#leave
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(150)
turtle.pendown()

#8
turtle.setheading(315)
turtle.forward(50)
turtle.setheading(45)
turtle.forward(50)
turtle.penup()
turtle.setheading(270)
turtle.forward(35)
turtle.pendown()
turtle.circle(2)

#leave
turtle.penup()
turtle.setheading(270)
turtle.forward(100)
turtle.pendown()

#9
turtle.setheading(0)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)

#leave
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

#10
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)

#leave
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.setheading(0)
turtle.forward(70)
turtle.pendown()

#11
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.penup()

#leave
turtle.setheading(0)
turtle.forward(70)
turtle.pendown()

#12
turtle.left(90)
turtle.forward(50)
turtle.backward(50)
turtle.right(90)
turtle.forward(40)
turtle.penup()

#leave
turtle.forward(30)
turtle.pendown()

#13
turtle.forward(40)
turtle.backward(40)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.setheading(0)
turtle.forward(40)
turtle.backward(40)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(40)

#leave
turtle.penup()
turtle.forward(30)

###############################################################
# Part 3) Wrap-up
# Start the turtles!
turtle.mainloop()
