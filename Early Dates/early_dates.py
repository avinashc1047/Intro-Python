from cisc108 import assert_equal

def all_digit(date: str, due_date: str)->bool:
    date_list = date.split('/')
    due_date_list = due_date.split('/')
    
    '''Checks to see if each individual item in the list is an integer or not. Had to do it individually because .isdigit() does not work
with lists. Uses the count method to detect '/' in the arguments, returns false if there are none or more than 2. '''
    if date.count('/') == 2 and due_date.count('/') == 2:
        if date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
            return due_date_list[0].isdigit() and due_date_list[1].isdigit() and due_date_list[2].isdigit()
        else:
            return False
        # need to use return false, as having none will break the program
    else:
        return False
    
assert_equal(all_digit('01/23/2224','1/2/34'), True)
assert_equal(all_digit('01/23/2224', 'abc'), False)
assert_equal(all_digit('abc', 'abc'), False)
assert_equal(all_digit('//', 'a//'), False)
assert_equal(all_digit('0123/2224', 'abc'), False)


def fix_month(month: str)->int:
    '''Takes in the argument for the month, and checks if it has 0 in front or not. If it includes a 0 in front it changes the value by taking out the
0 in fornt of the number. Leaves all other numbers as the same. Returns the month numer as an int.'''
    if len(month) == 2 and month[0] != '0':
        return int(month)
    elif len(month) == 2 and month[0] == '0':
        return int(month[1])
    else:
        return int(month)

assert_equal(fix_month('02'),2)
assert_equal(fix_month('2'),2)
assert_equal(fix_month('23'),23)
assert_equal(fix_month('800'),800)
    
def fix_day(day: str)->int:
    '''Same function as the fix_month.'''
    if len(day) == 2 and day[0] != 0:
        return int(day)
    elif len(day) == 2 and day[0] == 0:
        return int(day[1])
    else:
        return int(day)

assert_equal(fix_day('02'),2)
assert_equal(fix_day('2'),2)
assert_equal(fix_day('23'),23)
assert_equal(fix_day('200'),200)

def fix_year(year: str)->int:
    '''Same function as the fix_month but here it adds 20 to two digit arguments and leaves the rest as the same. This converts "02" to 2002.''' 
    if len(year) == 2:
        return int('20' + year)
    else:
        return int(year)

assert_equal(fix_year('02'),2002)
assert_equal(fix_year('2004'),2004)
assert_equal(fix_year('0'),0)
assert_equal(fix_day('1999'),1999)

def is_date(date: str)->bool:
    '''Checks to see if the date is valid and return the bool value. Argument includes the entire date str, the function splits it and then stores the
following conditional-bool value in the respective variable. Later it checks to see if all variable are true and then returns the bool value.'''
    date_list = date.split('/')
    
    is_month = fix_month(date_list[0]) > 0 and fix_month(date_list[0]) < 13
    is_day = fix_day(date_list[1]) > 0 and fix_day(date_list[1]) < 32
    is_year = fix_year(date_list[2]) > 999 and fix_year(date_list[2]) < 10000
    
    return is_month and is_day and is_year

assert_equal(is_date('2/2/2004'), True)
assert_equal(is_date('2/2/870'), False)
assert_equal(is_date('23/2/2004'), False)
assert_equal(is_date('02/02/87'), True)

def parse_alphabet(date: str)->bool:
    character = 'abcdefghijklmnopqrstuvwxyz'
    if date not in character:
        return True
    else:
        return False

def parse_date_month(date: str)->int:
    '''Processes the month from the date str. Uses the respective fix function to fix the value. Returns month int value or -1.'''
    pull_month = date.split("/")
    month = fix_month(pull_month[0])
    if parse_alphabet(date):
        if month > 0 and month < 13:
            return month
        else:
            return -1

assert_equal(parse_date_month('02/21/2004'), 2)
assert_equal(parse_date_month('2/21/2004'), 2)
assert_equal(parse_date_month('14/21/2004'), -1)
assert_equal(parse_date_month('12/21/02'), 12)

def parse_date_day(date: str)->int:
    '''Processes the day from the date str. Uses the respective fix function to fix the value. Returns day int value or -1 depending on conditions'''
    pull_day = date.split("/")
    day = fix_day(pull_day[1])
    if day > 0 and day < 32:
        return day
    else:
        return -1

assert_equal(parse_date_day('2/2/2020'), 2)
assert_equal(parse_date_day('10/10/2020'), 10)
assert_equal(parse_date_day('10/35/2020'), -1)
assert_equal(parse_date_day('10/05/2020'), 5)

def parse_date_year(date: str)->int:
    '''Processes the year value from the date str. Uses the respective fix function to fix the value. Returns the year int value or -1.'''
    pull_year = date.split("/")
    year = fix_year(pull_year[2])
    if year > 999 and year < 10000:
        return year
    else:
        return -1

assert_equal(parse_date_year('2/2/2020'), 2020)
assert_equal(parse_date_year('2/2/02'), 2002)
assert_equal(parse_date_year('2/2/999'), -1)

def is_equal(date: str, due_date: str)->bool:
    '''Checks to see if the date and due_date are equa or not. Returns a bool value. Uses if statements and sorts the date value into a list and then
checks to see if the lists are of equal value or not.'''
    list_date = date.split("/")
    list_due_date = due_date.split('/')
    if fix_year(list_date[2]) == fix_year(list_due_date[2]):
        if fix_month(list_date[0]) == fix_month(list_due_date[0]):
            return fix_day(list_date[1]) == fix_day(list_due_date[1])
        else:
            return False
    else:
        return False
    
assert_equal(is_equal("2/2/2020", "10/10/2020"), False)
assert_equal(is_equal("2/2/2020", "2/2/2020"), True)
assert_equal(is_equal("01/01/02", "1/1/2002"), True)
assert_equal(is_equal("01/01/02", "01/01/02"), True)

def first_date(date: str, due_date: str)->bool:
    '''Decides which value goes is earlier. Returns in bool. Checks to see if each date components are smaller than due_date components.
Starts with year, then month and then day.'''
    list_date = date.split("/")
    list_due_date = due_date.split('/')
    
    '''Comple cluster of if statements. This essentailly gives defiente bool value for certain conditions, and continues if they are not met.
The code that I used before did not return True for date values that were smaller in years instead it return true, so this fixes that.'''
    if fix_year(list_date[2]) < fix_year(list_due_date[2]):
        return True
    elif fix_year(list_date[2]) == fix_year(list_due_date[2]):
        if fix_month(list_date[0]) < fix_month(list_due_date[0]):
            return True
        elif fix_month(list_date[0]) == fix_month(list_due_date[0]):
            return fix_day(list_date[1]) < fix_day(list_due_date[1])
        else:
            return False
    else:
        return False
    
assert_equal(first_date("09/03/2020", "10/04/2020"),True)
assert_equal(first_date("11/03/2020", "10/04/2020"),False)
assert_equal(first_date("01/1/1980", "1/01/1989"),True)
assert_equal(first_date("11/03/2020", "10/04/2019"),False)

def earlier(date: str, due_date: str)->str:
    date_list = date.split('/')
    due_date_list = due_date.split('/')
    alphabet = '''abcdefghijklmnopqrstuwxyz'''
    '''The main function. This is where everything is processed and the main information is returned. First if statement uses the is_valid function to
check if the date and due_date are even valid. The second if statement checks if both the arguemnts are equal or not using the is_equal function.
If they are not equal the third if statement uses the first_date function to return date if the date is smaller than due_date or due_date if date is
larger than due_date. Usign bool functions in the external functions was a good idea because then I didn't have to use conditionals in the main earlier
function to return specific values.'''    
    if date.lower() not in alphabet and due_date.lower() not in alphabet:
        if all_digit(date, due_date):
            if is_date(date) and is_date(due_date):
                if is_equal(date, due_date):
                    return 'equal'
                else:
                    if first_date(date, due_date):
                        return date
                    else:
                        return due_date
            else:
                return 'error'
        else:
            return 'error'
    else:
        return 'error'

assert_equal(earlier("10/3/2020", "10/3/2020"), "equal")
assert_equal(earlier("01/06/23", "1/6/2023"), "equal")
assert_equal(earlier("Newark, De", "10/3/2020"), "error")
assert_equal(earlier("10/3/2020", "0/0/0000"), "error")
assert_equal(earlier("09/03/2020", "10/04/2020"), "09/03/2020")
assert_equal(earlier("10/03/2020", "10/04/2020"), "10/03/2020")
assert_equal(earlier("10/3/2020", "10/2/2020"), "10/2/2020")
assert_equal(earlier("2/2/2020", "10/10/2020"), "2/2/2020")
assert_equal(earlier("12/1/2019", "1/1/2020"), "12/1/2019")
assert_equal(earlier("12/1/2019", "1/1/2020"), "12/1/2019")
assert_equal(earlier("01/4/67", "1/5/68"), "01/4/67")
assert_equal(earlier("abc", "1/5/66"), "error")