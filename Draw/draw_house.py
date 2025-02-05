from designer import *

# number of if statements: 5
# number of elif statements: 3
# number of else statements: 5

# Logic - handle_color: Asks the user for a color name, then it turns it into lowercase and then it uses the IF statment and conditionals
#                       to match the color to either blue, orange, green. After matching it changes the variable coor to a different color.
#                       If the user does not input blue, orange, or green, then the else statement prints out a string and picks purple.
#                       handle_color returns the respective color after going through the if statemnts.

# Logic - handle_number: Asks the user for a number, and checks if it is a number or not. If it is not a number it prints a string
#                        and gives you the number 7. In the second if statement the program uses conditionals to check the number. If number
#                        is lower than 5 then the color is set to lightblue, if it is between 5 and 10 then color is lightcoral, else the
#                        color is purple. The function returns the color variable. 


def handle_color(color: str):
    if color.lower() == "blue":
        color = 'lightblue'
    elif color.lower() == "orange":
        color = 'orange'
    elif color.lower() == 'green':
        color = 'lightgreen'
    else:
        print("You did not enter an appropriate color. A color will be chosen for you. ")
        color = 'purple'
    return color


def handle_number(num_str: str):
    if num_str.isnumeric():
        num = int(num_str)
    else:
        print("You did not enter a proper number. A number will be chosen for you.")
        num = 7
    if num < 5:
        color = 'lightblue'
    elif 5 <= num <= 20:
        color = 'lightcoral'
    else:
        print("You did not enter a number between 0 and 20. A number will be chosen for you. ")
        color = 'lavender'
    return color

def make_house(make_house_flag: bool):
    if make_house_flag:
        roof_1 = line('lightyellow', 10, 400, 150, 500, 300)
        roof_2 = line('lightyellow', 10, 500, 300, 300, 300)
        roof_3 = line('lightyellow', 10, 300, 300, 400, 150)
        bottom_house = rectangle('firebrick', 300, 300, 200, 200)
        door = rectangle('black', 360, 350, 75, 150)
        door_handle = line('white', 3, 370, 400, 370, 450)
        house = group(roof_1, roof_2, bottom_house, door, door_handle)
        draw(house)
    else: 
        border = rectangle('black', 200, 200, 400, 300)
        inside_rect = rectangle(back_color, 215, 215, 370, 270)
        empty_lot = text('black', 'Empty lot!', 40, 300, 300)
        draw(empty_lot)
number = input("What is your favorite number from 0 to 20? \n")
back_color = handle_number(number)
set_window_color(back_color)

draw_house = input("Do you want to build a house? Answer \"yes\" or \"no\": \n")
if draw_house.lower() == 'yes':
    make_house(True)
else:
    make_house(False) 
    

