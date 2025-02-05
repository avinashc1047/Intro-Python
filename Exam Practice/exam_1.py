from cisc108 import assert_equal

''' Q1: You are hosting a party. Create a function named "plan_party" that consumes a number of attendees (an integer)
and a number of pizzas (an integer), and then produces whether you have enough pizza (a boolean), by multiplying
the number of attendees by 2 and testing if the result is less than or equal to the number of pizzas. You are encouraged to
unit test your function.'''

def plan_party(num_attends: int, num_pizza:int)->bool:
    return (num_attends*2)<=num_pizza

assert_equal(plan_party(2,4), True)
assert_equal(plan_party(2,2), False)
assert_equal(plan_party(0,2), True)

'''Q2: Define a function "make_past_tense" that consumes a string representing a verb and produces a new string with "ed" added
to the end. So the string "enter" becomes "entered".'''

def make_past_tense(verb: str)->str:
    return verb+'ed'

assert_equal(make_past_tense('enter'), 'entered')
assert_equal(make_past_tense('hover'), 'hovered')
assert_equal(make_past_tense('suck'), 'sucked')

'''Q3: You are creating a banking program. Create a function named "bank_print" that takes in a dollar amount (like '$100'),and then
returns just the number (100) by removing the first character.'''

def bank_print(money: str)->int:
    return int(money[1:])

assert_equal(bank_print('$400'),400)
assert_equal(bank_print('$1000'),1000)
assert_equal(bank_print('$0'),0)

'''Q4: Define a function named "is_valid_time" that takes in a time (like "04:00" or "12:30") and produces a boolean indicating whether
this is a valid time or not. A valid time must always have 5 characters, with the first and last two being digits (0-9) and the third
character being a colon. You may use the built-in "len" function to determine the length of a string.'''

def is_valid_time(time:str)->bool:
    if len(time) == 5:
        if time[0] in ('0123456789') and time[4] in ('0123456789'):
            if time[2] == ':':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

assert_equal(is_valid_time('04:00'), True)
assert_equal(is_valid_time('12.30'), False)
assert_equal(is_valid_time('a2:3i'), False)

'''Q5: The string method .upper() produces a new string that is an UPPERCASE version of the original string.
The string method .count(pattern) consumes a pattern (a string) and produces an integer indicating how often that pattern
appears in the original string. Use these to implement a new function named count_without_case that consumes a word (a string)
and a letter (a string) and produces an integer representing the number of times that the letter appears in the word, ignoring
capitalization.'''

def count_without_case(word: str, letter: str)->int:
    return word.upper().count(letter.upper())

assert_equal(count_without_case('aaa', 'a'), 3)
assert_equal(count_without_case('Banana', 'b'), 1)
assert_equal(count_without_case('misissipi', 's'), 3)

'''Q6: Define the function half_shouting that consumes a string and produces a new string where the first half of the letters are all
upper case and the second half of the letters are all lower case. You will need to use the built-in "len" and "int" functions to find
the midpoint of the string, and the built-in .upper() and .lower() methods of strings to change their case. For example, the string
"Awesome" would become "AWEsome".'''

def half_shouting(txt: str)->str:
    m_point = int(len(txt)/2)
    upper = txt[:m_point].upper()
    lower = txt[m_point:].lower()
    return upper + lower

assert_equal(half_shouting('awesome'), 'AWEsome')
assert_equal(half_shouting('AVINASH'), 'AVInash')
assert_equal(half_shouting('Sky'), 'Sky')

'''Q7: Define a function classify_age that consumes an age (an integer) and produces a string representing a description of that age.
If the age is 20 years or greater, produce "adult"; if the age is 13 years or greater, produce "teen"; otherwise produce "child".'''

def classify_age(age: int)->str:
    if age >= 20:
        return 'adult'
    elif age >= 13 and age < 20:
        return 'teen'
    else:
        return 'child'

assert_equal(classify_age(20), 'adult')
assert_equal(classify_age(15), 'teen')
assert_equal(classify_age(1), 'child')

'''Q8: Define a function get_minimum_pages that consumes a book size (a string) and produces an integer representing the minimum number
of pages that will be in a book of that size. The book sizes are either "novel" (80 pages), "novella" (20 pages), or "short story"
(1 page). For anything else, return the special value None.'''

def get_minimum_pages(book_type: str)->int:
    if book_type == 'novel':
        return 80
    elif book_type == 'novella':
        return 20
    elif book_type == 'short story':
        return 1
    else:
        return None

assert_equal(get_minimum_pages('novel'), 80)
assert_equal(get_minimum_pages('novella'), 20)
assert_equal(get_minimum_pages('story'), None)

'''Q9: Define a function cuteify that consumes a string representing an animal and produces a string representing that animal's name,
but cuter. Turn the string "dog" into the string "doggo", the string "cat" into "kit", and the string "snake" into "snek".'''

def cuteify(animal: str)->str:
    if animal == 'dog':
        return 'doggo'
    elif animal == 'cat':
        return 'kit'
    elif animal == 'snake':
        return 'snek'
    else:
        return None

assert_equal(cuteify('dog'),'doggo')
assert_equal(cuteify('cat'),'kit')
assert_equal(cuteify('ost'),None)

'''Q10: Define a function estimate_difficulty that consumes a message (a string) and whether you know its sender (a boolean),
and produces a string (either "good" or "bad"). If the message is "hi!" and you know the sender, produce "good". If the message
is "bye!" and you do not know the sender, also produce "good". Otherwise, produce "bad".'''

def estimate_difficulty(msg: str, know_sender: bool)->str:
    if msg == 'hi!' and know_sender:
        return 'good'
    elif msg == 'bye!' and not know_sender:
        return 'good'
    else:
        return 'bad' 

assert_equal(estimate_difficulty('hi!', True), 'good')
assert_equal(estimate_difficulty('bye!', False), 'good')
assert_equal(estimate_difficulty('!', False), 'bad')


'''Q11: [hard] Define a function classify_capitals that consumes a string and produces a string representing whether the string
is "uppercase", "lowercase", or "mixed". Use the .lower() and .upper() methods to test whether the string is all UPPERCASE, all
lowercase, or otherwise is MiXeD.'''

def calssify_capitals(txt: str)->str:
    pass


