from cisc108 import assert_equal

def parse_date_month(date: str)->int:
    
    '''arguments: date, is a string value that represents the date that is supposed to be processed.
       
       function: the function first uses the count method to check if the str has 2 '/' or not. If it does
       a list is made by splitting using the split method at all '/'. The first item on the list is stored in the month
       variable. The second if statement checks to see if the string has all digits or not. If it does it checks to see if
       the int month value is between 0 and 13, if it is then int(month) is printed. If any of the if statments are false
       the returned value is -1.'''
    
    if date.count('/') == 2:
        date_list = date.split('/')
        month = date_list[0]
        if month.isdigit():
            if 0 < int(month) < 13:
                return int(month)
            else:
                return -1
        else:
            return -1
    else:
        return -1

assert_equal(parse_date_month('7/1/16'), 7)
assert_equal(parse_date_month('08/21/20'), 8)
assert_equal(parse_date_month('00/5/2014'), -1)
assert_equal(parse_date_month('01/16/2004'), 1)
assert_equal(parse_date_month('13/23/1999'), -1)
assert_equal(parse_date_month('newark, de'), -1)

def parse_date_day(date: str)->int:
    
    '''arguments: date, is a string value that represents the date that is supposed to be processed.
       
       function: the function first uses the count method to check if the str has 2 '/' or not. If it does
       a list is made by splitting using the split method at all '/'. The second item on the list is stored in the day
       variable. The second if statement checks to see if the string has all digits or not. If it does it checks to see if
       the int day value is between 0 and 32, if it is then int(day) is printed. If any of the if statments are false
       the returned value is -1.'''
    
    if date.count('/') == 2:
        date_list = date.split('/')
        day = date_list[1]
        if day.isdigit():
            if 0 < int(day) < 32:
                return int(day)
            else:
                return -1
        else:
            return -1
    else:
        return -1

assert_equal(parse_date_day('7/1/16'), 1)
assert_equal(parse_date_day('2/05/2015'), 5)
assert_equal(parse_date_day('1/newar/due'), -1)
assert_equal(parse_date_day('01/16/2004'), 16)
assert_equal(parse_date_day('13/32/1999'), -1)
assert_equal(parse_date_day('newark, de'), -1)

def parse_date_year(date: str)->int:
    
    '''arguments: date, is a string value that represents the date that is supposed to be processed.
       
       function: the function first uses the count method to check if the str has 2 '/' or not. If it does
       a list is made by splitting using the split method at all '/'. The third item on the list is stored in the year
       variable. The second if statement checks to see if the string has all digits or not. the third if statement checks
       the length of the year variable is equal to 2, if it is year is added to 2000 and then returned. Else if length of year
       is 4, then it is simply returned. If any of the if statments are false the returned value is -1.'''
    
    if date.count('/') == 2:
        date_list = date.split('/')
        year = date_list[2]
        if year.isdigit():
            if len(year) == 2:
                return int(year) + 2000
            elif len(year) == 4:
                return int(year)
            else:
                return -1
        else:
            return -1
    else:
        return -1

assert_equal(parse_date_year('7/1/16'), 2016)
assert_equal(parse_date_year('2/21/200'), -1)
assert_equal(parse_date_year('05/19/99'), 2099)
assert_equal(parse_date_year('01/16/2004'), 2004)
assert_equal(parse_date_year('13/23/4'), -1)
assert_equal(parse_date_year('newark, de'), -1)

def is_date(date: str)->bool:
    
    '''arguments: date, is a string value that represents the date that is supposed to be processed.
       
       function: the function uses all the helper parse functions to check if any of the values are equal to -1 or not,
       if they aren't True is returned else False is returned.'''
    
    if parse_date_year(date) != -1:
        if parse_date_month(date) != -1:
            return parse_date_day(date) != -1
        else:
            return False
    else:
        return False 

assert_equal(is_date('2/12/2004'), True)
assert_equal(is_date('00/00/0000'), False)
assert_equal(is_date("Newark, de"), False)
assert_equal(is_date("13/32/2013"), False)
assert_equal(is_date("5//2020"), False)
assert_equal(is_date("5/2020"), False)

def earlier(sub_date: str, due_date: str)->str:
    
    '''arguments: sub_date is the submission date of the assignment in the form of a string. due_date is the
       final date of the assingment in the form of a string.
       
       function: the function is the main function. It uses the is_date functions to check if the dates are valid
       or not. It then uses the parse functions to check if the values equal each other or not. If the values
       aren't equal it checks for the lesser value, if the first is lower the sub_date is printed, if it is larger the
       due_date is printed. If the is_date function returns False, this function return 'error'.'''
    
    if is_date(sub_date) and is_date(due_date):
        if parse_date_year(sub_date) == parse_date_year(due_date):
            if parse_date_month(sub_date) == parse_date_month(due_date):
                if parse_date_day(sub_date) == parse_date_day(due_date):
                    return 'equal'
                elif parse_date_day(sub_date) < parse_date_day(due_date):
                    return sub_date
                else:
                    return due_date
            elif parse_date_day(sub_date) < parse_date_day(due_date):
                return sub_date
            else:
                return due_date
        elif parse_date_year(sub_date) < parse_date_year(due_date):
            return sub_date
        else:
            return due_date
    else:
        return 'error'

assert_equal(earlier('newark, de', '2/2/2004/'), 'error')
assert_equal(earlier('1/5/2004', '05/09/00'), '05/09/00')
assert_equal(earlier('02/02/2004', '2/2/2004'), 'equal')
assert_equal(earlier('3/21/2020', '3/21/2019'), '3/21/2019')
assert_equal(earlier('8/31/1979', '01/22/1980'), '8/31/1979')




