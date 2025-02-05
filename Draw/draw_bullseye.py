from designer import *

def bullseye(input_color: str, x_center: int):
    half_height = get_height()/2
    circ_1 = circle(input_color, 100, x_center, half_height)
    circ_2 = circle('white', 75, x_center, half_height)
    circ_3 = circle(input_color, 50, x_center, half_height)
    bullseye = group(circ_1, circ_2, circ_3)
    
    # 3.1 The fucntion is used to create objects using designer,
    # creating a circle with the specified parameter and then grouping it with the group() function.
    # 3.2 The bullseye function asks for the input_color and x_center argumetns when calling the function.
    # 3.3 The function returns a designer object as it draws the circles and groups them together. 
    
    return bullseye

half_width = get_width() / 2
sixth_width = get_width() / 6
five_sixth_width = get_width() * 5 / 6
red_bullseye = bullseye('red', half_width)
yellow_bullseye = bullseye('yellow', sixth_width)
draw(red_bullseye, yellow_bullseye)