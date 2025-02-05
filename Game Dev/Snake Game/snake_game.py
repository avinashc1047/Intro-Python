from designer import *
from random import randint
from random import choice

# The initial dictionary types.
'''
This defiens the values for the worlds, like the snake which is the head,
the body which is a list of body segments, and much more.
'''
World = {'snake': DesignerObject,
         'body': [DesignerObject],
         'speed': int,
         'direction': str,
         'food': DesignerObject,
         'score': int,
         'counter': DesignerObject,
         'game': DesignerObject,
         'timer': int}

# The values of the world.
'''
Creates the initial world and holds all the standard World values.
'''
def create_world()->World:
    return {'snake': create_snake(),
            'body': [],
            'speed': s_speed,
            'direction': ' ',
            'food': [],
            'score': 0,
            'counter': text('black', '', 50, 500, 100),
            'game': text('black', '', 50, 500, 500),
            'timer': 0}
     
# Sets the window size to 1000 x 1000
set_window_size(1000,1000)

# random number generator between 2 and 998 for the window width & height.
def random()->int:
    return randint(2,998)

# The constant speed of the snake, how fast the snake moves.
s_speed = 8

# Create snake
# Creates the snake image and scales it appropriately
def create_snake()->DesignerObject:
    snake = image('snake.png')
    snake['scale'] = 0.08
    return snake

# Creates the body of the snake, which is a square
# Uses the choice() to choose between 3 colors from colors.
def create_body()->DesignerObject:
    # olivedrab yellowgreen darkolivegreen
    colors = ['olivedrab', 'yellowgreen', 'darkolivegreen']
    body = rectangle(choice(colors), 30, 30)
    return body

# Creates food for the snake.
# Uses the random function from before to create
# it at a random place in the window.
def create_food(world: World)->DesignerObject:
    food = image('apple.png')
    food['scale'] = 0.04
    food['x'] = random()
    food['y'] = random()
    world['food'] = food
    return food

# Changes the 'counter' value of the world with the 'score'
def counter(world: World):
    world['counter']['text'] = str(world['score'])
    
# If there is no food in the word, this creates a food.
# This ensures that when the world begins there is food in it.
# Uses the create_food function to make the food. 
def check_food(world: World):
    if world['food'] == []:
        create_food(world)

# Checks if the food and the snake has collided.
# Uses the colliding() to check the collision.
# If this is true then the food is relocated to another position.
# This also adds 1 to world['score'] as that counts the food eaten.
def collision(world: World):
    food = world['food']
    if colliding(world['snake'], world['food']):
        world['food']['x'] = random()
        world['food']['y'] = random()
        world['food'] = food
        world['score'] += 1
        # make more body
        new_body(world)

# In charge of making a new body segment.
# When this is called it calls the create_body(), stores its value
# in a variable and adds the variable using the .append() to world['body']
def new_body(world: World):
    body = create_body()
    world['body'].append(body)

# Incharge of controlling the body segment movements.
'''
First te function adds one to the counter.
The if statement controls the speed of the movement for body parts.
if the remainder of the timer / 8 is 0 then the functions creates
variables prev x and y and sets them to the snake x and y positions.
Then for every body in world['body'] and then it sets the position values
of different parts to different variables, essentally making a chain where
the snake gives its opstion to the previous and that to one previous to it.
'''
def body_follow(world: World):
    world['timer'] += 1
    if world['timer'] % 8 == 0:
        prev_x = world['snake']['x']
        prev_y = world['snake']['y']
        for body in world['body']:
            temp_x = body['x']
            temp_y = body['y']
            body['x'] = prev_x
            body['y'] = prev_y
            prev_x = temp_x
            prev_y = temp_y

# Checks to see if the snake head is hitting the body.
# Let's the first 2 and last 2 pass as they can corssover and break the function.
# creates a variable 'a' that stores false, for every body in the list of bodies,
# if the collidinng function is true with the snake and body then a is true.
# return a boolean value in the a variable.
def body_collision(world: World)->bool:
    a = False
    for body in world['body'][2:-2]:
        if colliding(world['snake'], body):
            a = True
    return a

# Same function as body_collision except here they check if the snake head and
# side of the wind collide. Thich checks if the snake is in between the window or not.
# If its not true is returned.
def side_collision(world: World)->bool:
    stop = False
    if not 0 <= world['snake']['x'] <= 1000 or not 0 <= world['snake']['y'] <= 1000:
        stop = True
    return stop

# Move snake
# Changes the direction key in world to whatever the key the user inputed.
def flip_snake(world: World, key: str):
    world['direction'] = key

# Updated direction
# Uses the direction key from world to change the direction of the snake.
# At the beginning the snake starts with the direction key value of ' ' and moves right.
# This function checks the direction key value and changes the snake's x or y by adding
# or subtracting as the user inputs.
# Also turns the snake image to point to the moving direction. 
def direction(world: World):
    snake = world['snake']
    if world['direction'] == ' ':
        snake['x'] += world['speed']
        snake['angle'] = 90
    elif world['direction'] == 'right':
        snake['x'] += world['speed']
        snake['angle'] = 90
    elif world['direction'] == 'left':
        snake['x'] -= world['speed']
        snake['angle'] = 270
    elif world['direction'] == 'down':
        snake['y'] += world['speed']
        snake['angle'] = 0
    elif world['direction'] == 'up':
        snake['y'] -= world['speed']
        snake['angle'] = 180

# game status
# changes the text value to Game over when called upon.
def game_status(world: World):
    world['game']['text'] = 'Game Over!'

when('starting', create_world)
when('updating', counter)
when('updating', check_food)
when('updating', direction)
when('updating', collision)
when('updating', body_follow)
when('typing', flip_snake)
when(body_collision, game_status, pause)
when(side_collision, game_status, pause)
start()