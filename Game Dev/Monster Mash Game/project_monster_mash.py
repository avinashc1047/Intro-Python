#################################################
# Do not modify this section
# You must place 'monster_mash.json' in the same
# directory as this file.
from cisc108 import assert_equal
import json

with open('monster_mash.json') as data_file:
    MONSTER_MASH = json.load(data_file)

#################################################
# Your code goes below

## Party
'''
A Party is a dictionary with four fields:
* "type": The type of party that it is
* "werewolves": The number of werewolves in attendance
* "vampires": The number of vampires in attendance
* "witches": The number of witches in attendance
'''

Party = {"werewolves": int, "vampires": int, "witches": int,
         "type": str}


"""
P1. Define a function `sum_guests` that consumes a Party and
produces an integer representing the total number of
guests attending (including werewolves, vampires, and witches).
"""
def sum_guests(party: Party) -> int:
    '''
Description: Sums the total number of guests. Makes a variable of all the keys in the dictionary.
Then adds them up and returns them.
Argument: Takes in a dictionary with the Party types.
Return: Returns an integer, representing the sum of guests. 
    '''
    werewolves = party['werewolves']
    vampires = party['vampires']
    witches = party['witches']
    return werewolves + vampires + witches

assert_equal(sum_guests(MONSTER_MASH['party 1']), 20)
assert_equal(sum_guests(MONSTER_MASH['party 2']), 25)
assert_equal(sum_guests(MONSTER_MASH['party 3']), 19)
assert_equal(sum_guests(MONSTER_MASH['party 4']), 33)

# https://codebeautify.org/online-json-editor/cb58cc0b

"""
P2. Define a function `were_only_werewolves` that consumes a Party and
produces a boolean indicating whether or not the only guests were
werewolves.
"""
def were_only_werewolves(party: Party)->bool:
    '''
Description: Checks if the dictionary has only werewovles or not. Does this with the help
of if statements, that check if the keys are == 0 or not.
Argument: Takes in a dictionary with the Party types.
Return: Returns a boolean, representing if all are werewovles or not.
    '''
    if party['witches'] == 0:
        if party['vampires'] == 0:
            if party['werewolves'] != 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
assert_equal(were_only_werewolves(MONSTER_MASH['party 1']), True)
assert_equal(were_only_werewolves(MONSTER_MASH['party 2']), False)
assert_equal(were_only_werewolves(MONSTER_MASH['party 3']), False)
assert_equal(were_only_werewolves(MONSTER_MASH['party 4']), True)

'''
P3. Witches and vampires always bring a date, but werewolves prefer to
come to parties alone (because they're lone wolves). Define a function
`total_folks` that consumes a Party and produces an integer representing
the total number of folks who were present.
'''
def total_folks(party: Party)->int:
    '''
Description: Produces the total number of guests at the party, with vampires and witches being
allowed to bring a date. Makes variable with the keys, and multiplys the vampires and witches with 2.
Before adding them up and returning them.
Argument: Takes in a dictionary with the Party types.
Return: Returns an int, representing the total guests with their dates.
    '''
    werewolves = party['werewolves']
    vampires = party['vampires'] * 2
    witches = party['witches'] * 2
    return werewolves + vampires + witches

assert_equal(total_folks(MONSTER_MASH['party 1']), 20)
assert_equal(total_folks(MONSTER_MASH['party 2']), 45)
assert_equal(total_folks(MONSTER_MASH['party 3']), 38)
assert_equal(total_folks(MONSTER_MASH['party 4']), 33)

'''
P4. A "small" party has 20 or fewer guests, a "big" party has 40 or more,
and otherwise the party is "medium". Define a function `check_party_size`
that consumes a Party and produces a string indicating whether the party
is "small", "medium", or "big". Note that we're counting guests, not folks,
so don't include witches' and vampires' dates.
'''
def check_party_size(party: Party)->str:
    '''
Description: Checks if the party is small, big or medium. Uses the sum_guests(party)
to check the total guests and compares it with if statements and conditionals.
Argument: Takes in a dictionary with the Party types.
Return: Returns a str, indicating the size of the party.
    '''
    total_guest = sum_guests(party)
    if total_guest <= 20:
        return 'small'
    elif total_guest >= 40:
        return 'big'
    else:
        return 'medium'

assert_equal(check_party_size(MONSTER_MASH['party 1']), 'small')
assert_equal(check_party_size(MONSTER_MASH['party 2']), 'medium')
assert_equal(check_party_size(MONSTER_MASH['party 3']), 'small')
assert_equal(check_party_size(MONSTER_MASH['party 4']), 'medium')

'''
P5. If a party has both werewolves and vampires, there should be
more werewolves than vampires. Define a function `check_party_ratio`
that consumes a Party and produces a float indicating the number of
werewolves divided by the number of vampires. If there are no vampires
or no werewolves, produce the value 0.
'''
def check_party_ratio(party: Party)->float:
    '''
Description: Used to find the ratios of the werewolves to vampires. Returns 0 if any
of the kinds are 0. Divides the werewolves and vampires, and returns them.
Argument: Takes in a dictionary with the Party types.
Return: Returns a float, representing the ration of werewolves and vampires.
    '''
    if party['werewolves'] == 0 or party['vampires'] == 0:
        return 0
    else:
        return party['werewolves']/party['vampires']

assert_equal(check_party_ratio(MONSTER_MASH['party 1']), 0)
assert_equal(check_party_ratio(MONSTER_MASH['party 2']), 0.25)
assert_equal(check_party_ratio(MONSTER_MASH['party 3']), 0)
assert_equal(check_party_ratio(MONSTER_MASH['party 5']), 3.0)

## Monsters
'''
A Monster is a dictionary with four fields:
* "name": The name of this particular monster (string)
* "kind": A str representing the type of the monster (e.g., "vampire", "werewolf")
* "spookyiness": An integer from 0-4 indicating its spookiness
* "undead?": A boolean indicating whether or not this monster is undead.
'''

Monster = {"name": str, "kind": str, "spookiness": int, "undead?": bool}


'''
M1. Define a function `count_monsters` that consumes a list of monsters and
produces an integer indicating how many monsters there are.
'''
def count_monsters(monsters: [Monster])->int:
    '''
Description: Counts the number of monsters in the list. Uses the count function, and a for
loop to count the times monsters are parsed.
Argument: Takes in a list of dictionaires with the Monster type.
Return: Returns an int, representing the number of monsters.
    '''
    count = 0
    for monster in monsters:
        count += 1
    return count

assert_equal(count_monsters(MONSTER_MASH['monsters 1']), 4)
assert_equal(count_monsters(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_monsters(MONSTER_MASH['monsters 3']), 5)
assert_equal(count_monsters(MONSTER_MASH['monsters 5']), 5)

'''
M2. Define a function `count_undead_monsters` that consumes a list
of monsters and produces an integer indicating how many undead
monsters there are.
'''
def count_undead_monsters(monsters: [Monster])->int:
    '''
Description: Counts the undead monsters. Uses a for loop to count the number of
undead monsters in the list.
Argument: Takes in a list of dictionaires with the Monster type.
Return: Returns an int, representing the number of undead monsters.
    '''
    count = 0
    for monster in monsters:
        if monster['undead?'] == True:
            count += 1
    return count

assert_equal(count_undead_monsters(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 3']), 2)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 5']), 3)

'''
M3. Define a function `average_spookiness` that consumes a list of monsters
and produces a float representing their average spookiness. If the list
is empty, produce the special value `None` instead.
'''
def average_spookiness(monsters: [Monster])->float:
    '''
Description: Finds the average spookiness of the monsters in the list. Uses the count
and total for loops, then divides the total/count to find the average.
Argument: Takes in a list of dictionaires with the Monster type.
Return: Returns an int, representing the average spookiness.
    '''
    if monsters != []:
        count = 0
        total = 0
        for monster in monsters:
            count += 1
            total += monster['spookiness']
        return total / count

assert_equal(average_spookiness(MONSTER_MASH['monsters 1']), 0.0)
assert_equal(average_spookiness(MONSTER_MASH['monsters 2']), 1.0)
assert_equal(average_spookiness(MONSTER_MASH['monsters 3']), 1.8)
assert_equal(average_spookiness(MONSTER_MASH['monsters 6']), None)

'''
M4. Define a function `average_undead_spookiness` that consumes a list of monsters
and produces a float representing the average spookiness of the undead monsters
in the list. If there are no undead monsters, produce the special value `None`
instead.
'''
def average_undead_spookiness(monsters: [Monster])->float:
    '''
Description: Finds the average spookines of the undead monsters. Counts the total
undead monsters and stores the total spookiness. The function divides the two and returns it.
Argument: Takes in a list of dictionaires with the Monster type.
Return: Returns a float, representing the average spookiness of the undead monsters.
    '''
    if count_undead_monsters(monsters) != 0:
        count_undead = count_undead_monsters(monsters)
        total_undead = 0
        for monster in monsters:
            if monster['undead?'] == True:
                total_undead += monster['spookiness']
        return total_undead/count_undead

assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 1']), None)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 2']), 1.0)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 3']), 1.5)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 6']), None)

'''
M5. Define a function `count_spooky_monsters` that consumes a list of monsters
and produces an integer indicating how many monsters have a spookiness of
2 or more.
'''
def count_spooky_monsters(monsters: [Monster])->int:
    '''
Description: Counts the number of monsters who are more spooky than 2. Uses a for loop
and if statement with conditionals to see if the key vaue is bigger than 2 or not. If it
is then the 1 is added to the count and then the coutn is returned. 
Argument: Takes in a list of dictionaires with the Monster type.
Return: Returns an int, representing monster more spooky than 2.
    '''
    count_2spooky = 0
    for monster in monsters:
        if monster['spookiness'] >= 2:
            count_2spooky += 1
    return count_2spooky

assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 2']), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 3']), 3)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 4']), 3)

'''
M6. Define the function `count_vampires` that consumes a list of monsters
and produces an integer indicating how many monsters are of the kind
"vampire".
'''
def count_vampires(monsters: [Monster])->int:
    '''
Description: Counts the numebr of vampires. Does this by using a count loop and an if statement
that filters for the vampire kind.
Argument: Takes in a list of dictionaires with the Monster type.
Return: Returns an int value, representing the number of vampires.
    '''
    count_vampires = 0
    for monster in monsters:
        if monster['kind'] == 'vampire':
            count_vampires += 1
    return count_vampires

assert_equal(count_vampires(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_vampires(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_vampires(MONSTER_MASH['monsters 3']), 0)
assert_equal(count_vampires(MONSTER_MASH['monsters 5']), 2)

## Costumes
'''
A Costume is a dictionary with 3 keys:
* 'label': A string representing the name of the costume.
* 'price': An integer representing the cost of the costume in dollars.
* 'sizes': A list of strings representing the available sizes ('S', 'M', 'L').
'''

Costume = {'label': str, 'price': int, 'sizes': [str]}


'''
C1. Define a function `count_costumes` that consumes a list of costumes
and produces an integer representing the number of costumes in the list.
'''
def count_costumes(costumes: [Costume])->int:
    '''
Description: Counts the total number of costumes in the list. Uses a simple count
loop to do this.
Argument: Takes in a list of dictionaries with the Costume type.
Return: An int value representing the total number of costumes.
    '''
    count = 0
    for coustume in costumes:
        count += 1
    return count

assert_equal(count_costumes(MONSTER_MASH['costumes 1']), 4)
assert_equal(count_costumes(MONSTER_MASH['costumes 2']), 3)
assert_equal(count_costumes(MONSTER_MASH['costumes 4']), 5)
assert_equal(count_costumes(MONSTER_MASH['costumes 5']), 4)

'''
C2. Define a function `total_price` that consumes a list of costumes
and produces an integer representing the total price of all the
costumes in the list.
'''
def total_price(costumes: [Costume])->int:
    '''
Description: Uses a simple count function to count the total price of all the costumes.
Argument: Takes in a list of dictionaries with the Costume type.
Return: An int value representing the total price of costumes.
    '''
    total_price = 0
    for costume in costumes:
        total_price += costume['price']
    return total_price

assert_equal(total_price(MONSTER_MASH['costumes 1']), 180)
assert_equal(total_price(MONSTER_MASH['costumes 2']), 105)
assert_equal(total_price(MONSTER_MASH['costumes 4']), 340)
assert_equal(total_price(MONSTER_MASH['costumes 5']), 120)

'''
C3. Define a function `count_sizes` that consumes a list of costumes and
produces an integer indicating the total number of sizes that are
available across all the costumes.
'''
def count_sizes(costumes: [Costume])->int:
    '''
Description: Counts the total sizes of all the costumes. Uses a count loop to add
1 to total_sizes for every available size.
Argument: Takes in a list of dictionaries with the Costume type.
Return: An int value representing the total number of sizes across all costumes.
    '''
    total_sizes = 0
    for costume in costumes:
        for size in costume['sizes']:
            total_sizes += 1
    return total_sizes

assert_equal(count_sizes(MONSTER_MASH['costumes 1']), 9)
assert_equal(count_sizes(MONSTER_MASH['costumes 2']), 0)
assert_equal(count_sizes(MONSTER_MASH['costumes 4']), 9)
assert_equal(count_sizes(MONSTER_MASH['costumes 5']), 4)

'''
C4. Define a function `max_price` that consumes a list of costumes
and produces an integer indicating the price of the most expensive
costume. If there are no costumes in the list, produce the special
value `None`.
'''
def max_price(costumes: [Costume])->int:
    '''
Description: Finds the max price of a costume in the dictionary. Uses a for and if
loop to do this and stores the highest value in the highest variable.
Argument: Takes in a list of dictionaries with the Costume type.
Return: An int value representing the max price of all the costumes.
    '''
    if costumes != []:
        highest = costumes[0]['price']
        for costume in costumes:
            if costume['price'] >= highest:
                highest = costume['price']
        return highest

assert_equal(max_price(MONSTER_MASH['costumes 1']), 90)
assert_equal(max_price(MONSTER_MASH['costumes 2']), 50)
assert_equal(max_price(MONSTER_MASH['costumes 4']), 80)
assert_equal(max_price(MONSTER_MASH['costumes 6']), None)

'''
C5. Define a function `most_expensive_costume` that consumes
a list of costumes and produces a string representing the label
of the costume with the highest price. In the event of a tie,
give the label of the item later in the list. If there are no
costumes, return the special value None.
'''
def most_expensive_costume(costumes: [Costume])->str:
    '''
Description: Finds the most expensive costume name in the dictionary. Does this with by
a for loop and if statement to find the hihgest price and then associating it with their name.
Argument: Takes in a list of dictionaries with the Costume type.
Return: A str value, representing the most expensive costume name.
    '''
    if costumes != []:
        highest_price = costumes[0]['price']
        highest_label = ''
        for costume in costumes:
            if costume['price'] >= highest_price:
                highest_price = costume['price']
                highest_label = costume['label']
        return highest_label

assert_equal(most_expensive_costume(MONSTER_MASH['costumes 1']), 'Pirate Zombie Ghost')
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 2']), 'Wardrobe')
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 4']), 'Thor')
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 6']), None)

'''
C6. Define a function `find_last_medium` that consumes a list of costumes
and produces the label of the last costume that is available in a medium.
If no medium costumes are found, produce the special value `None`.
'''
def find_last_medium(costumes: [Costume])->str:
    '''
Description: Finds the last medium costume available. Uses a for loop to first check if there
are mediums or not. If mediums are not available None is returned, if more than 0 medums exists
a combination of for and if loop to serch for the last M size costume, and then returns its name.
Argument: Takes in a list of dictionaries with the Costume type.
Return: A str value, representing the name of the last m sized costume.
    '''
    last_medium_name = ''
    mediums = 0
    for costume in costumes:
        if 'M' in costume['sizes']:
            mediums += 1
    if mediums > 0:
        for costume in costumes:
            if 'M' in costume['sizes']:
                last_medium_name = costume['label']
        return last_medium_name

assert_equal(find_last_medium(MONSTER_MASH['costumes 1']), 'Ghost')
assert_equal(find_last_medium(MONSTER_MASH['costumes 2']), None)
assert_equal(find_last_medium(MONSTER_MASH['costumes 4']), 'Captain America')
assert_equal(find_last_medium(MONSTER_MASH['costumes 5']), 'Rogue')

'''
C7. Define a function `find_first_small` that consumes a list of costumes
and produces the label of the first costume that is available in a small.
If no small costumes are found, produce the special value `None`.
'''
def find_first_small(costumes: [Costume])->str:
    '''
Description: Finds the name of the first small sized costumes. First checks to see
if there are small sizes or not. If there are it uses a for loop and if statement to filter
out the last small costume's name.
Argument: Takes in a list of dictionaries with the Costume type.
Return: A str value representing the name of the smallest costume.
    '''
    first_small = ''
    smalls = 0
    for costume in costumes:
        if 'S' in costume['sizes']:
            smalls += 1
    if smalls > 0:
        for costume in costumes:
            if 'S' in costume['sizes']:
                first_small = costume['label']
                break
        return first_small

assert_equal(find_first_small(MONSTER_MASH['costumes 1']), 'Pirate')
assert_equal(find_first_small(MONSTER_MASH['costumes 2']), None)
assert_equal(find_first_small(MONSTER_MASH['costumes 4']), 'Spiderman')
assert_equal(find_first_small(MONSTER_MASH['costumes 5']), 'Knight')

## Tombstones

'''
A Grave is a dictionary with two keys:
* 'Name': A string value with the grave's occupant's name
* 'Message': A string value with the grave's message
'''

Grave = {'name': str, 'Message': str}


'''
G1. Define the function `count_grave_all` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Include spaces and new lines.
'''
def count_grave_all(graves: [Grave])->int:
    '''
Description: Counts the total number of graves, using a for loop.
Argument: Takes in a list of dictionaries with the Grave type.
Return: An int val, representing the total graves. 
    '''
    total_characters = 0
    for grave in graves:
        total_characters += len(grave['message'])
    return total_characters

assert_equal(count_grave_all(MONSTER_MASH['graves 1']), 149)
assert_equal(count_grave_all(MONSTER_MASH['graves 2']), 105)
assert_equal(count_grave_all(MONSTER_MASH['graves 4']), 0)
assert_equal(count_grave_all(MONSTER_MASH['graves 3']), 108)

'''
G2. Define the function `count_grave_characters` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Do not count spaces and new lines.
'''
def count_grave_characters(graves: [Grave])->int:
    '''
Description: Counts the number of characters on the grave message. Uses the len
function and two for loops to find the total number of message characters.
Argument: Takes in a list of dictionaries with the Grave type.
Return: An int val, representing the total characters on the grave messages.
'''
    total_chars = 0
    for grave in graves:
        words_clean = grave['message'].split()
        for word in words_clean:
            total_chars += len(word)
    return total_chars

assert_equal(count_grave_characters(MONSTER_MASH['graves 1']), 120)
assert_equal(count_grave_characters(MONSTER_MASH['graves 2']), 90)
assert_equal(count_grave_characters(MONSTER_MASH['graves 4']), 0)
assert_equal(count_grave_characters(MONSTER_MASH['graves 3']), 95)

'''
G3. Define a function named `estimate_grave_cost` that consumes a list of graves
and produces an integer representing the total estimate lettering cost by
multiplying the number of letters on the grave (ignoring spaces and newlines) by
the cost of writing a letter ($2).
'''
def estimate_grave_cost(graves: [Grave])->int:
    '''
Description: Estimates the graves cost, by multiplying the total characters in the message
with 2. Uses the count_grave_characters() to find the total characters and then * 2.
Argument: Takes in a list of dictionaries with the Grave type.
Return: An int val, representing the price of the grave.
'''
    total_chars = count_grave_characters(graves)
    return int(total_chars * 2)

assert_equal(estimate_grave_cost(MONSTER_MASH['graves 1']), 240)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 2']), 180)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 4']), 0)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 3']), 190)

"""
G4. Define a function named `count_shouters` that consumes a list of graves
and produces an integer representing the number of graves that had their
messages in all capital letters. Hint: use the `.upper()` method.
"""
def count_shouters(graves: [Grave])->int:
    '''
Description: Finds the graves that have all words in uppercase. Does this with a for
loop and if statement that checks if all words are uppercase or not.
Argument: Takes in a list of dictionaries with the Grave type.
Return: A str value, representing the graves with all uppercase messages.
'''
    shout_count = 0
    for grave in graves:
        if grave['message'] == grave['message'].upper():
            shout_count += 1
    return shout_count

assert_equal(count_shouters(MONSTER_MASH['graves 1']), 3)
assert_equal(count_shouters(MONSTER_MASH['graves 2']), 1)
assert_equal(count_shouters(MONSTER_MASH['graves 4']), 0)
assert_equal(count_shouters(MONSTER_MASH['graves 3']), 1)

## Treats

'''
A Treat is a dictionary with the following keys
* "name": A string value indicating the name of the treat
* "chocolate?": A boolean indicating whether the treat involves chocolate
* "calories": An integer representing how many calories are in the treat
* "quantity": An integer indicating the typical serving size of the treat.
'''

Treat = {'name': str, 'chocolate?': bool, 'calories': int, 'quantity': int}

'''
T1. You are going through a series of houses and you get a treat from
each one. Define a function `eat_candy` that consumes a list of treats and
produces the total number of calories in all the treats.
'''
def eat_candy(treats: [Treat])->int:
    '''
Description: Finds the total calories in all the candies. Does this with a simple for
loop that adds up the total in th total_cal variable.
Argument: Take in a list of dictionaries with the Treat type.
Return: An int val, representing the total calories in the candies.
    '''
    total_cal = 0
    for treat in treats:
        total_cal += treat['calories']
    return total_cal

assert_equal(eat_candy(MONSTER_MASH['treats 1']), 563)
assert_equal(eat_candy(MONSTER_MASH['treats 2']), 280)
assert_equal(eat_candy(MONSTER_MASH['treats 4']), 464)
assert_equal(eat_candy(MONSTER_MASH['treats 6']), 0)


'''
T2. Define a function `find_most_calorific_ratio` that consumes a list
of treats and produces a float representing the treat with the
highest calories per quantity. If the list is empty, return
the special value None.
'''
def find_most_calorific_ratio(treats: [Treat])->float:
    '''
Description: Finds the most calorieper weight filled candy. Does this using a for loop
and if statements. Divides the first values and stores them and then checks them using the
conditional.
Argument: Take in a list of dictionaries with the Treat type.
Return: A float value representing the highest calorie to weight ratio.
    '''
    if treats != []:
        highest_ratio = treats[0]['calories'] / treats[0]['quantity']
        for treat in treats:
            ratio = treat['calories']/treat['quantity']
            if ratio >= highest_ratio:
                highest_ratio = ratio
        return highest_ratio

assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 1']), 35.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 2']), 35.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 4']), 214.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 6']), None)

'''
T3. Define a function `find_most_calorific` that consumes a list
of treats and produces a string representing the name of the treat with the
highest calories per quantity. If the list is empty, return
the special value None. In the event of a tie, give the name of the
treat later in the list.
'''
def find_most_calorific(treats: [Treat])->str:
    '''
Description: Finds the name of the most calorific ratio candy. Does this by calling the
find_most_calorific_ratio(), and then comapring the value with a for loop and if statement
to find and return the name.
Argument: Take in a list of dictionaries with the Treat type.
Return: A str val, representing the name of the most calorie to weight ratio.
    '''
    highest_name = ''
    highest_cal = find_most_calorific_ratio(treats)
    if treats != []:
        for treat in treats:
            if highest_cal == treat['calories']/treat['quantity']:
                highest_name = treat['name']
        return highest_name

assert_equal(find_most_calorific(MONSTER_MASH['treats 1']), 'Snickers')
assert_equal(find_most_calorific(MONSTER_MASH['treats 2']), 'Snickers')
assert_equal(find_most_calorific(MONSTER_MASH['treats 4']), 'Candy Apple')
assert_equal(find_most_calorific(MONSTER_MASH['treats 6']), None)

'''
T4. Define a function named `count_chocolates` that consumes a list of treats
and produces the number of treats that are made of chocolate.
'''
def count_chocolates(treats: [Treat])->int:
    '''
Description: Counts the number of chocolates in the dictionary. Does this with the count
loop and then returns it.
Argument: Take in a list of dictionaries with the Treat type.
Return: An int val, representing the total chocolates.
    '''
    choco_count = 0
    for treat in treats:
        if treat['chocolate?']:
            choco_count += 1
    return choco_count

assert_equal(count_chocolates(MONSTER_MASH['treats 1']), 2)
assert_equal(count_chocolates(MONSTER_MASH['treats 2']), 4)
assert_equal(count_chocolates(MONSTER_MASH['treats 4']), 0)
assert_equal(count_chocolates(MONSTER_MASH['treats 6']), 0)

'''
T5. Define a function named `get_choco_quantity` that consumes a list
of treats and produces an integer representing the total quantities
of all the chocolate treats.
'''
def get_choco_quantity(treats: [Treat])->int:
    '''
Description: Finds the total treats that are made with chocolates. Uses a for loop and if
statement, to filter out the treats and adding the treats that are made with chocolates.
Argument: Take in a list of dictionaries with the Treat type.
Return: An int val, representing the total treats made with chocolates.
    '''
    choco_quant = 0
    for treat in treats:
        if treat['chocolate?']:
            choco_quant += treat['quantity']
    return choco_quant

assert_equal(get_choco_quantity(MONSTER_MASH['treats 1']), 19)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 2']), 8)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 4']), 0)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 6']), 0)

## Media

'''
A Media is a dictionary with the following keys:
* "name": The name of this media
* "kind": Either "movie", "song", or "game"
* "duration": The length of this media in minutes
'''

Media = {'name': str, 'kind': str, 'duration': int}

'''
E1. Define a function `total_duration` that consumes a list of Media
and produces their total duration.
'''
def total_duration(medias: [Media])->int:
    '''
Description: Finds the total duration of the types. Uses a for loop to count the
total time and returns it.
Argument: Takes in a list with dictionaries that takes the Media type.
Return: An int val, representing the total duration of the items.
    '''
    total_time = 0
    for media in medias:
        total_time += media['duration']
    return total_time

assert_equal(total_duration(MONSTER_MASH['media 1']), 383)
assert_equal(total_duration(MONSTER_MASH['media 2']), 146)
assert_equal(total_duration(MONSTER_MASH['media 4']), 216)
assert_equal(total_duration(MONSTER_MASH['media 5']), 0)

'''
E2. Define the function `count_not_long` that consumes a list of media
and produces the number of items that are less than 100 minutes long.
'''
def count_not_long(medias: [Media])->int:
    '''
Description: Checks the number of items that are less than 100 minutes long. Uses a for and if
loop to find items under 100 minutes long. 
Argument: Takes in a list with dictionaries that takes the Media type.
Return: An int val, representing the total items that are lower than a 100.
    '''
    below_100 = 0
    for media in medias:
        if media['duration'] < 100:
            below_100 += 1
    return below_100

assert_equal(count_not_long(MONSTER_MASH['media 1']), 2)
assert_equal(count_not_long(MONSTER_MASH['media 2']), 4)
assert_equal(count_not_long(MONSTER_MASH['media 4']), 2)
assert_equal(count_not_long(MONSTER_MASH['media 5']), 0)

'''
E3. Define the function `take_until_long` that consumes a list of media
and counts elements until it encounters something that is 100 minutes
longer or more, and then stops and returns the number counted so far.
'''
def take_until_long(medias: [Media])->int:
    '''
Description: Counts the number of items until an item is above a 100 minutes long.
Uses for and if loops to check if the next item is longer than a 100 or not, if it is the
loop breaks and returns the count so far.
Argument: Takes in a list with dictionaries that takes the Media type.
Return: An int val, representing the number of items until an item is above a 100 minutes long.
    '''
    number = 0
    for media in medias:
        if media['duration'] < 100:
            number += 1
        else:
            break
    return number

assert_equal(take_until_long(MONSTER_MASH['media 1']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 2']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 4']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 5']), 0)

'''
E4. Define the function `longest_kind` that consumes a list of Media
and produces a string value representing the kind that had the highest
duration. If the list is empty, return the value None.
'''
def longest_kind(medias: [Media])->str:
    '''
Description: Finds the kind of media that has the highest duration. Uses a for
loop and if statement, to find the name of the highest duration.
Argument: Takes in a list with dictionaries that takes the Media type.
Return: A str val, representing the type of media with the hihgest duration.
    '''
    if medias != []:
        kind = ''
        high_time = medias[0]['duration']
        for media in medias:
            if media['duration'] >= high_time:
                kind = media['kind']
        return kind

assert_equal(longest_kind(MONSTER_MASH['media 1']), 'movie')
assert_equal(longest_kind(MONSTER_MASH['media 2']), 'song')
assert_equal(longest_kind(MONSTER_MASH['media 4']), 'game')
assert_equal(longest_kind(MONSTER_MASH['media 5']), None)

'''
E5. Define the function `same_kind_of_media` that consumes a list
of Media and produces a boolean indicating whether all of the
kinds of media are the same as each other. If the list is empty,
the result is True.
'''
def same_kind_of_media(medias: [Media])->bool:
    '''
Description: Finds if all the media is the same type or not. Uses for loops and
if statements to compare the value to the previous one stored in the same variable.
If it's still True then all media types are the same.
Argument: Takes in a list with dictionaries that takes the Media type.
Return: A boolean val, representing if all media type are the same or not.
    '''
    same = True
    if medias != []:
        first_kind = medias[0]['kind']
        for media in medias:
            if first_kind != media['kind']:
                same = False
        return same
    else:
        return same

assert_equal(same_kind_of_media(MONSTER_MASH['media 1']), True)
assert_equal(same_kind_of_media(MONSTER_MASH['media 2']), True)
assert_equal(same_kind_of_media(MONSTER_MASH['media 4']), False)
assert_equal(same_kind_of_media(MONSTER_MASH['media 5']), True)

## Brewing Potions

'''
An Ingredient has the following keys:
* 'name': The name of the ingredient
* 'rare?': Whether the ingredient is rare

A Potion has the following keys:
* 'effect': The effect of the potion
* 'ingredients': The required ingredients of the potion
* 'time required': How many minutes it takes to brew the potion
'''

Ingredient = {'name': str, 'rare?': bool}
Potion = {'effect': str, 'ingredients': [Ingredient], 'time required': int}

'''
B1. Define the function `total_ingredients` that consumes a list
of potions and produces the total number of required ingredients.
Include duplicates in your total.
'''
def total_ingredients(potions: [Potion])->int:
    '''
Description: Finds the total ingredients in the potions. Uses a simple count loop
to find the total ingredients.
Argument: Takes in a list of dictionaries with the Potion type.
Return: An int val, representing the total number of ingredients in the list.
    '''
    ingredients = 0
    for potion in potions:
        for item in potion['ingredients']:
            ingredients += 1
    return ingredients

assert_equal(total_ingredients(MONSTER_MASH['brewing 1']), 9)
assert_equal(total_ingredients(MONSTER_MASH['brewing 2']), 5)
assert_equal(total_ingredients(MONSTER_MASH['brewing 3']), 8)
assert_equal(total_ingredients(MONSTER_MASH['brewing 4']), 0)

'''
B2. Define the function `count_rare_ingredients` that consumes a list
of potions and produces the total number of required ingredients that
are rare.
'''
def count_rare_ingredients(potions: [Potion])->int:
    '''
Description: Counts the number of rare ingredients in the list. Uses a two for loops
and an if statement to find the inner list and filter through to check if the
ingredient is rare or not. It counts the total and then returns it.
Argument: Takes in a list of dictionaries with the Potion type.
Return: An it val, representing the total rare ingredients in the list.
    '''
    rare_count = 0
    for potion in potions:
        for item in potion['ingredients']:
            if item['rare?']:
                rare_count += 1
    return rare_count

assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 1']), 1)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 2']), 4)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 3']), 4)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 4']), 0)

'''
B3. Define the function `get_ingredients` that consumes a list of
potions and produces a list of strings (representing ingredient names)
in the order that the ingredients are listed in the potions.
Do not include duplicate ingredients.
'''
def get_ingredients(potions: [Potion])->[str]:
    '''
Description: Finds the list of ingredients and returns their names. Appends the ingredient
names into an empty list, checks if there are duplicates and removes it if there are.
Argument: Takes in a list of dictionaries with the Potion type.
Return: A list of strings, representing the names of the ingredients.
    '''
    ingredients = []
    for potion in potions:
        for item in potion['ingredients']:
            if item['name'] not in ingredients:
                ingredients.append(item['name'])
    return ingredients

assert_equal(get_ingredients(MONSTER_MASH['brewing 1']), ['Spider Webs', 'Ant Hill', 'Dragon Egg',
                                                          'Moon Blooms', 'Candy Leaf'])
assert_equal(get_ingredients(MONSTER_MASH['brewing 2']), ['Dream Petal', 'Hens Teeth', 'Ant Hill'])
assert_equal(get_ingredients(MONSTER_MASH['brewing 3']), ['Candy Leaf', 'Moon Blooms', 'Red Nightshade',
                                                          'Werewolf Heart'])
assert_equal(get_ingredients(MONSTER_MASH['brewing 4']), [])

'''
B4. Define the function `get_brewing_time` that consumes a list of
potions and produces an integer representing the total time required
to brew all the potions.
'''
def get_brewing_time(potions: [Potion])->int:
    '''
Description: Finds the total time to brew the potions. Adds up the time of preperation
from the list and totals it up. Uses a for loop to simply add the ints.
Argument: Takes in a list of dictionaries with the Potion type.
Return: An int val, representing the total time of preperation.
    '''
    total_time = 0
    for potion in potions:
        total_time += potion['time required']
    return total_time

assert_equal(get_brewing_time(MONSTER_MASH['brewing 1']), 15)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 2']), 16)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 3']), 12)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 4']), 0)

'''
B5. Define the function `brew_time_per_ingredient` that consumes a list
of potions and produces a float representing the average amount of
time spent brewing overall. To do so, add up the time spent brewing
and divide it by the number of ingredients. If there are no ingredients,
return the value None.
'''
def brew_time_per_ingredient(potions: [Potion])->float:
    '''
Description: Finds the brew time by dividing the number of potions with the total times.
Uses both the total_ingredients() and get_brewing_time(), and divides them to find the val.
Argument: Takes in a list of dictionaries with the Potion type.
Return: A float val, representing the brew time/total ingredients.
    '''
    ingredients = total_ingredients(potions)
    brew_time = get_brewing_time(potions)
    if ingredients != 0:
        return brew_time/ingredients

assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 1']), 15/9)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 2']), 16/5)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 3']), 12/8)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 4']), None)

'''
B6. Define the function `get_rarest_potion` that consumes a list of potions
and returns the effect of the potion that requires the most rare ingredients.
If there are no rare ingredients in any of the potions, then return None instead.
'''
def get_rarest_potion(potions: [Potion])->str:
    '''
Description: Finds the effect of the potion with the most rarest potions. Uses a for and if
loop to makes a dicitoanry, rare_potions with the effect as the key and the amount of rare potions as the value.
Then it stores the first value in the dictionary in the highest variable using a simple for loop.
Then it compares the value in the highest variable to each value in rare_potions using a for loop.
It stores the associated name of the highest value in the name variable. Then uses an if statement to check
if the highest value is 0 or not, if it isn't name variable is returned. If it is 0, None is returned. 
Argument: Takes in a list of dictionaries with the Potion type.
Return: A str val, representing the the effect of the most rarest potion.
    '''
    rare_potions = {}
    for potion in potions:
        rare_count = 0
        name = potion['effect']
        for item in potion['ingredients']:
            if item['rare?']:
                rare_count += 1
        rare_potions[rare_count] = name


    # {1: 'Bones', 3: 'Cold', 4: 'High', 0: 'Stink'}
    highest = 0
    for count in rare_potions:
        highest = count
        break
    
    name_effect = ''
    for count, effect in rare_potions.items():
        if count >= highest:
            highest = count
            name_effect = effect
    
    if highest != 0:
        return name_effect
        
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 1']), 'Sweet Breathing Potion')
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 1']), "Sweet Breathing Potion")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 2']), "Embiggening Potion")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 3']), "Delirious Tea")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 4']), None)
