"""
# Ada's Stats Module
A collection of functions for doing some basic statistics on your data.

# When You Are Done
When you pass all tests, remember to clean and document your code.
Be sure to unit test and document your functions.
"""

from cisc108 import assert_equal

# 1) count
def count(results: [int])->int:
    '''This is the count function that counts the elements in the list using
       the for loop by adding 1 everytime a value is called from the list.'''
    count = 0
    for result in results:
        count += 1
    return count

assert_equal(count([3,5,6,2,5]), 5)
assert_equal(count([3,5]), 2)
assert_equal(count([]), 0)

# 2) summate
def summate(results: [int])->int:
    '''This is the summate function that adds all the values in the given list.
       Uses a for loop and addas the called value to a variable that is = 0.'''
    total = 0
    for result in results:
        total += result
    return total

assert_equal(summate([1,2,3,4,5]), 15)
assert_equal(summate([1,2,3]), 6)
assert_equal(summate([0]), 0)

# 3) mean
def mean(numbers: [int])->float:
    '''This is the mean function, that takes the mean of the give list.
       It calls on the summate and count functions and divides them to
       get the mean. It also uses an if statement to return if there
       is an empty list.'''
    if numbers == []:
        return None
    else:
        return summate(numbers) / count(numbers)

assert_equal(mean([1,2,3]), 2.0)
assert_equal(mean([100,50,15,35]), 50.0)
assert_equal(mean([]), None)

# 4) square
def square(numbers: [int])->[int]:
    '''This is the square function, it squares all the values in the list
       and then adds the squared values to a new list, in the squared variable.'''
    squared = []
    for number in numbers:
        squared.append(number**2)
    return squared

assert_equal(square([1,2,3,4]), [1,4,9,16])
assert_equal(square([0]), [0])
assert_equal(square([]), [])

# 5) diff
def diff(numbers: [int], subtract: int)->[int]:
    '''This is the diff function, it takes the difference of each element on the list
       with the give argument. It also adds the subtracted values to a new list and then
       returns it.'''
    subtracted = []
    for number in numbers:
        subtracted.append(number-subtract)
    return subtracted

assert_equal(diff([2,5], 2), [0,3])
assert_equal(diff([0], 2), [-2])
assert_equal(diff([], 2), [])

# 6) standard_deviation
def standard_deviation(numbers: [int])->float:
    '''This is the standard deviation function. It takes the stdv of the given list.
       It makes a new list of the mean subtracted from the original list. Then squares
       the numbers and adds them to a new list. Then it summs all the squared numbers
       and then divides it by the number of elements minus 1. In the end it takes the square
       root of the total/count number ad returns the value in the form of a float with
       2 decimal places. There is an if statement that checks if the list is bigger than
       2 elemnts or not, if it is not None is returned.'''
    if count(numbers) >= 2:
        mean_val = mean(numbers)
        subtract_mean = diff(numbers, mean_val)
        squared = []
        total = 0
        for value in subtract_mean:
            squared.append(value**2)
        for value in squared:
            total += value
        square_root = (total/(count(numbers)-1))**0.5
        return  int((square_root*100))/100
    else:
        return None
    
assert_equal(standard_deviation([6,2,3,1]), 2.16)
assert_equal(standard_deviation([8,10,25,15,50]), 17.18)    
assert_equal(standard_deviation([0]), None)
assert_equal(standard_deviation([0,10]), 7.07)    

# 7) main function
# The following code can be used to try out your functions.
# Comment them out now.
# Uncomment each line as you implement the functions to try them out.
def main(question, results):
    '''The main function that, tells us about the results and the questions
       from the research.'''
    print("We asked", count(results), "people the following question.")
    print(' "'+question+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(results))
    print("\tMean:", mean(results))
    print("\tStandard Deviation:", standard_deviation(results))
    
# 8) Question and Results
# Comment these out until you are ready to define them
QUESTION = "How many courses do you want to take next semester?"
ANSWERS = [4,5,4,6,3,5,5,7,6,4,5,4,6,5,5,4,6,6,5,5]
ANALYSIS = '''We asked 20 people the following question.
                 "How many courses do you want to take next semester?"
              Here are the statistical results:
                Sum: 100
                Mean: 5.0
                Standard Deviation: 0.94'''

main(QUESTION, ANSWERS)