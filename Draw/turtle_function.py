# Project 3- Turtle Alphabet
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

###############################################################
# Part 1) Setup
# Load turtle module, move it to left side, make turtle faster
import turtle
turtle.reset()
turtle.speed(0)
turtle.penup()
turtle.goto(-400, 0)
turtle.speed(0)
turtle.pensize(5)
turtle.color('red')

###############################################################
# Part 2)
# Write the code for each letter below

'''template -
def draw_d(x:int, y:int):
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading()
    
    turtle.penup()
    turtle.goto(x, y)
    #calc
    pos = x + 80
    return print(pos)
    '''


#A
def draw_a(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#D
def draw_d(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(55)
    turtle.right(120)
    turtle.forward(55)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#E
def draw_e(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(0)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#i
def draw_i(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(0)
    turtle.forward(50)
    turtle.backward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#l
def draw_l(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(0)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#n
def draw_n(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(130)
    turtle.forward(71)
    turtle.left(130)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#o
def draw_o(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#p
def draw_p(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#r
def draw_r(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(155)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x, y)
    #calc
    return x + 80

#v
def draw_v(x:int, y:int)->int:
    #set
    turtle.goto(x, y)
    turtle.pendown()
    #draw
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(50)
    turtle.right(145)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(110)
    turtle.forward(60)
    turtle.penup()
    turtle.goto(x, y)
    #calc

    return x+100



#call ADNROID V APPLE
x_position = draw_a(-600,200)
x_position = draw_n(x_position,200)
x_position = draw_d(x_position,200)
x_position = draw_r(x_position,200)
x_position = draw_o(x_position,200)
x_position = draw_i(x_position,200)
x_position = draw_d(x_position,200)
x_position = draw_v(x_position,100)
x_position = draw_a(x_position,0)
x_position = draw_p(x_position,0)
x_position = draw_p(x_position,0)
x_position = draw_l(x_position,0)
x_position = draw_e(x_position,0)

#call driven
x_position = draw_d(-700,500)
x_position = draw_r(x_position,500)
x_position = draw_i(x_position,500)
x_position = draw_v(x_position,500)
x_position = draw_e(x_position,500)
x_position = draw_n(x_position,500)

#call varied
x_position = draw_v(120,500)
x_position = draw_a(x_position,500)
x_position = draw_r(x_position,500)
x_position = draw_i(x_position,500)
x_position = draw_e(x_position,500)
x_position = draw_d(x_position,500)


# Part 3) Wrap-up
# Start the turtles!
turtle.mainloop()
    