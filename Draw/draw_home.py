from designer import *

set_window_color('lightskyblue')

def handle_number(num_str: str)->str:
    if num_str.isnumeric():
        num = int(num_str)
    else:
        print("You did not enter a proper number. A number will be chosen for you.")
        num = 7
    if num < 5:
        color = 'lightgoldenrodyellow'
    elif 5 <= num <= 20:
        color = 'lightsalmon'
    else:
        print("You did not enter a number between 0 and 20. A number will be chosen for you. ")
        color = 'lavender'
    return color

def window_color(color:str)->str:
    if color.lower() == "blue":
        color = 'lightblue'
    elif color.lower() == "orange":
        color = 'orange'
    elif color.lower() == 'green':
        color = 'lightgreen'
    else:
        print("You did not enter an appropriate color. The color yellow will be chosen for you. ")
        color = 'yellow'
    return color

def door_color(color:str)->str:
    if color.lower() == "brown":
        color = 'brown'
    elif color.lower() == "white":
        color = 'white'
    elif color.lower() == 'gray':
        color = 'dimgray'
    else:
        print("You did not enter an appropriate color. The color beige will be chosen for you. ")
        color = 'beige'
    return color

def roof_window_color(color:str)->str:
    if color.lower() == "blue":
        color = 'lightblue'
    elif color.lower() == "orange":
        color = 'orange'
    elif color.lower() == 'green':
        color = 'lightgreen'
    else:
        print("You did not enter an appropriate color. The color yellow will be chosen for you. ")
        color = 'yellow'
    return color

def make_house(make_house_flag: bool):
    if make_house_flag:
        roof_1 = line('olive', 10, 400, 150, 500, 300)
        roof_2 = line('olive', 10, 500, 300, 300, 300)
        roof_3 = line('olive', 10, 300, 300, 400, 150)
        bottom_house = rectangle('tomato', 300, 300, 200, 200)
        call_window_color = input("What color do you want your window to be?")
        wcolor = window_color(call_window_color)
        window = rectangle(wcolor, 315, 400, 35, 35)
        color_input = input("What color do you want your door to be?")
        dcolor = door_color(color_input)
        door = rectangle(dcolor, 360, 350, 75, 150)
        door_handle = line('black', 3, 370, 400, 370, 450)
        
        want_window = input('What color do you want your roof window to be?')
        rwcolor = roof_window_color(want_window)
        r_window = rectangle(rwcolor, 380, 225, 35, 35)
        
        house = group(roof_1, roof_2, bottom_house, window, r_window, door, door_handle)
        draw(house)
    else: 
        border = rectangle('black', 200, 200, 400, 300)
        inside_rect = rectangle(back_color, 215, 215, 370, 270)
        empty_lot = text('red', 'Empty lot!', 40, 300, 300)
        draw(empty_lot)

number = input("What is your favorite number from 0 to 20? \n")
back_color = handle_number(number)
set_window_color(back_color)

draw_house = input("Do you want to build a house? Answer \"yes\" or \"no\": \n")
if draw_house.lower() == 'yes':
    make_house(True)
else:
    make_house(False) 
    





