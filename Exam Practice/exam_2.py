from cisc108 import assert_equal
# If statements and conditionals:
'''
Q1[easy] Define a function classify_age that consumes an age (an integer) and produces a string representing a
description of that age. If the age is 20 years or greater, produce "adult"; if the age is 13 years or greater,
produce "teen"; otherwise produce "child".
'''
def classify_age(age:int)->str:
    if age >= 20:
        return 'adult'
    elif 13 <= age <= 20:
        return 'teen'
    else:
        return 'child'

assert_equal(classify_age(21), 'adult')
assert_equal(classify_age(15), 'teen')
assert_equal(classify_age(9), 'child')

'''
Q2[easy] Define a function get_minimum_pages that consumes a book size (a string) and produces an integer representing
the minimum number of pages that will be in a book of that size. The book sizes are either "novel" (80 pages), "novella"
(20 pages), or "short story" (1 page). For anything else, return the special value None.
'''
def get_minimum_pages(size:str)->int:
    if size.lower() == 'novel':
        return 80
    elif size.lower() == 'novella':
        return 20
    elif size.lower() == 'short story':
        return 1
    else:
        None
        
assert_equal(get_minimum_pages('novel'), 80)
assert_equal(get_minimum_pages('novella'), 20)
assert_equal(get_minimum_pages('Short story'), 1)
assert_equal(get_minimum_pages('story'), None)

'''
Q3[easy] Define a function cuteify that consumes a string representing an animal and produces a string representing that
animal's name, but cuter. Turn the string "dog" into the string "doggo", the string "cat" into "kit", and the string
"snake" into "snek". These are the only strings that it can handle.
'''
def cuteify(txt:str)->str:
    if txt.lower() == 'dog':
        return 'doggo'
    elif txt.lower() == 'cat':
        return 'kit'
    elif txt.lower() == 'snake':
        return 'snek'

assert_equal(cuteify('dog'), 'doggo')

'''
Q4[medium] Define a function estimate_difficulty that consumes a message (a string) and whether you know its sender
(a boolean), and produces a string (either "good" or "bad"). If the message is "hi!" and you know the sender, produce
"good". If the message is "bye!" and you do not know the sender, also produce "good". Otherwise, produce "bad".
'''
def estimate_difficulty(msg: str, know_sender: bool)->str:
    if msg == 'hi!' and know_sender:
        return 'good'
    elif msg == 'bye!' and not know_sender:
        return 'good'
    else:
        return 'bad'
    
assert_equal(estimate_difficulty('hi!', True), 'good')

'''
Q5[hard] Define a function classify_capitals that consumes a string and produces a string representing whether the
string is "uppercase", "lowercase", or "mixed". Use the .lower() and .upper() methods to test whether the string is all
UPPERCASE, all lowercase, or otherwise is MiXeD.
'''
def classify_capitals(txt: str)->str:
    if txt.lower() == txt:
        return 'lowercase'
    elif txt.upper() == txt:
        return 'uppercase'
    else:
        return 'MiXeD'
    
assert_equal(classify_capitals('Leads'), 'MiXeD')

# Lists and list operators:
'''
Q6[easy] Define a function has_canines that consumes a list of strings (representing types of animals) and produces whether
or not any of the following strings is in the list: "dog", "doggo", or "pupper".
'''
def has_canines(animals: [str])->bool:
    if 'dog' in animals:
        return True
    elif 'doggo' in animals:
        return True
    elif 'pupper' in animals:
        return True
    else:
        return False 

assert_equal(has_canines(['cat', 'leopard', 'doggo']), True)

'''
Q7[easy] Define a function get_inner that consumes a list of integers and produces a list of integers not including the first
and last ones. So the list [1, 2, 3, 4] would become [2, 3].
'''
def get_inner(ints: [int])->[int]:
    return ints[1:-1]

assert_equal(get_inner([2, 3, 6, 7, 9]), [3, 6, 7])

'''
Q8[medium] Define a function are_ends_equal that consumes a non-empty list and produces whether the first and last values are equal.
'''
def are_ends_equal(ints: [int])->bool:
    if ints != []:
        return ints[0] == ints[-1]
    else:
        return None

assert_equal(are_ends_equal([0, 1, 3, 4]), False)

'''
Q9[medium] Define a function get_fourth that consumes a list and produces the fourth value in the list. If the list has less
than 4 values, produce the integer 4. You may use the built-in len function that consumes a list and produces its length as an integer.
'''
def get_fourth(ints: [int])->int:
    if len(ints) >= 4:
        return ints[3]
    else:
        return 4
    
assert_equal(get_fourth([1,2,3,5]), 5)
assert_equal(get_fourth([1,2]), 4)

# Loops and loop patterns:
'''
Q10[easy] Define a function count_hearts that consumes a list of strings and produces the number of times that the string "heart"
appears. You may NOT use the built-in .count() method.
'''
def count_hearts(txt: [str])->int:
    count = 0
    for item in txt:
        if item == 'heart':
            count += 1
    return count

assert_equal(count_hearts(['heart', 'banan', 'apple', 'heart']), 2)

'''
Q11[easy] Define a function has_100_dollars that consumes a list of dollar amounts (floats) that represents a wallet full of money,
and produces whether or not the wallet has more than $100. You may NOT use the built-in sum() function.
'''
def has_100_dollars(dollars: [float])->bool:
    total = 0
    for dollar in dollars:
        total += dollar
    return total >= 100

assert_equal(has_100_dollars([1, 2, 3, 4]), False)
assert_equal(has_100_dollars([15, 50, 40, 20]), True)

'''
Q12[easy] Define a function negate that consumes a list of integers and produces a new list where each number has been multiplied
by -1 (i.e., negated).
'''
def negate(ints: [int])->[int]:
    negated = []
    for num in ints:
        negated.append(num*-1)
    return negated

assert_equal(negate([1,2,3,4,5]), [-1,-2,-3,-4,-5])

'''
Q13[medium] Define a function remove_lies that consumes a list of boolean values and produces a new list without any of the False values.
'''
def remove_lies(bools: [bool])->[bool]:
    new = []
    for state in bools:
        if state:
            new.append(state)
    return new

assert_equal(remove_lies([True, False, True]), [True, True])

'''
Q14[medium] Define a function count_docx that consumes a list of strings (representing filenames) and produces the number that end
in ".docx". Use the built-in .endswith(pattern) method of strings that consumes a pattern and returns whether the string ends with
that pattern.
'''
def count_docx(files: [str])->int:
    docx = 0
    for file in files:
        if file.endswith('.docx'):
            docx += 1
    return docx

assert_equal(count_docx(['file', 'file.docx']), 1)

'''
Q15[hard] Define a function get_increments that consumes a list of numbers and produces a number by checking whether each element is
adjacent to the current highest value. Whenever a new value is exactly one more than the current value (initially 0), choose that
as the new highest value. Example: the list [1, 5, 3, 2, 7, 3, 6, 4, 9] would produce the value 4. If an empty list is given,
you may produce 0.
'''


# Disctionaries:
'''
Q16[easy] Define a function get_temperature that consumes a Weather forecast and produces the current temperature (an integer).
A weather forecast will be a dictionary with the keys "temperature" (int), "humidity" (float), and "is sunny" (boolean). So you
just need to return the value associated with the temperature key.
'''
def get_temperature(forecast: dict)->int:
    return forecast['temperature']

assert_equal(get_temperature({'temperature': 57, 'humidity': 10.0, 'is sunny': True}), 57)

'''
Q17[easy] Define a function should_see that consumes a Movie and produces a boolean indicating whether or not you want to see it.
A movie will be a dictionary with the keys "name" (string), "genre" (string), and "rating" (float). Your function should produce
True when either the genre is "comedy", or when the "rating" is greater than 3.0. Otherwise, it should produce False.
'''
def should_see(movie: dict)->bool:
    return movie['genre'] == 'comedy' or movie['rating'] > 3.0

assert_equal(should_see({'name': 'Titanic', 'genre': 'comedy', 'rating': 4.1}), True)    
    
'''
Q18[easy] Define a function is_valid_dog that consumes a dictionary and produces whether or not the dictionary has the following
keys: "name", "breed", and "is_fluffy".
'''
def is_valid_dog(animal: dict)->bool:
    if 'name' in animal:
        if 'breed' in animal:
            return 'is_fluffy' in animal
        else:
            return False
    else:
        return False
        
assert_equal(is_valid_dog({'name': 'hel', 'breed':'shit', 'ao': 'pkt'}), False)

'''
Q19[medium] Define a function map_cuteness that consumes nothing and produces a dictionary associating a kind of animal (a string)
with the animal's name, but cuter. The dictionary should associate the string "dog" with the string "doggo", the string "cat" with
"kit", and the string "snake" with "snek".
'''
def map_cuteness()->dict:
    return {'dog':'doggo', 'cat': 'kit', 'snake': 'snek'}

assert_equal(map_cuteness(), {'dog':'doggo', 'cat': 'kit', 'snake': 'snek'})

'''
Q20[medium] Define a function estimate_time that consumes a course and your workload (an integer), and produces a number indicating
how many hours you should spend on it. A course is a dictionary with the keys "name" (a string), "rating" (integer), "for majors"
(boolean). If the course is for majors, produce the rating multiplied by 20 minus your workload. Otherwise produce the rating
multiplied by 10 minus your workload.
'''
Course = {'name': str, 'rating':int, 'for majors': bool}
def estimate_time(course: Course, workload: int)->int:
    if  course['for majors']:
        return (course['rating'] * 20) - workload
    else:
         return (course['rating'] * 10) - workload

assert_equal(estimate_time({'name': 'CISC', 'rating': 5, 'for majors': True}, 10), 90)

# Nested loops:
'''
Q21[medium] Define a function summate_books that consumes a list of Books and produces an integer representing the total page count
of all the books. A Book will be a dictionary with the keys "title" (string), "author" (string), "page count" (int), and "is paperback?"
(boolean).
'''
Book = {'title': str, 'author': str, 'page count': int, 'is paperback?': bool}
def summate_books(books: [Book])->int:
    page_count = 0
    for book in books:
        page_count += book['page count']
    return page_count

assert_equal(summate_books([{'title': 'lord', 'author': 'Jean', 'page count': 200, 'is paperback?': True},
                            {'title': 'Hung', 'author': 'Larc', 'page count': 40, 'is paperback?': False}]), 240)

'''
Q22[medium] Define a function count_red_cars that consumes a list of Cars and produces an integer representing the total number of
cars that were "red". A Car will be a dictionary with the keys "model" (string), "year" (int), and "color" (str).
'''
Car = {'model': str, 'year': int, 'color': str}
def count_red_cars(cars: [Car])->int:
    red_count = 0
    for car in cars:
        if car['color'] == 'red':
            red_count += 1
    return red_count

assert_equal(count_red_cars([{'model': 'Ferrari', 'year': 2009, 'color': 'red'}, {'model': 'Ford', 'year': 2100, 'color': 'blue'}]), 1)

'''
Q23[hard] Define a function filter_big_boxes that consumes a list of Boxes and produces a new list of those Boxes without any boxes
that were big. A Book will be a dictionary with the keys "width" (int), "length" (int), "height" (int). A box is considered big if
its "length" multiplied by its "width" is more than 10.
'''
Boxes = {'width': int, 'length': int, 'height': int}
def filter_big_boxes(boxes: [Boxes])->[Boxes]:
    no_big = []
    area = 0
    for box in boxes:
        area = box['length'] * box['width']
        if area < 10:
            no_big.append(box)
    return no_big

assert_equal(filter_big_boxes([{'width': 5, 'length': 5, 'height': 5}, {'width': 1, 'length': 2, 'height': 1}]), [{'width': 1, 'length': 2, 'height': 1}])

'''
Q24[hard] Define a function biggest_winner that consumes a list of game winners and produces the name of the winner who won the
most money. A winner is dictionary with the keys "name" (str), "winnings" (int), "from" (str). Note that your function must produce
the *name* of the person, so it should return a string.
'''
Winner = {"name": str, "winnings": int, "from": str}
def biggest_winner(game_winners: [Winner])->str:
    most_wins = game_winners[0]['winnings']
    name_winner = ''
    for winner in game_winners:
        if winner['winnings'] >= most_wins:
            most_wins = winner['winnings']
            name_winner = winner['name']
    return name_winner
    
assert_equal(biggest_winner([{"name": 'Avi', "winnings": 10, "from": 'India'}, {"name": 'John', "winnings": 15, "from": 'America'}]), 'John')