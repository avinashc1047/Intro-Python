from cisc108 import assert_equal

def is_date(date: str)->bool:
    return date.count('/') == 2

assert_equal(is_date('02/32/2004'), True)
assert_equal(is_date('abc'), False)
assert_equal(is_date('abc//'), True)
assert_equal(is_date('abc/'), False)

def parse_date_month(date: str)->int:
    date_list = date.split('/')
    if is_date(date):
        if 0 < int(date_list[0]) < 13:
            return int(date_list[0])
        else:
            return -1
    else:
        return -1

assert_equal(parse_date_month('Newark,De'),-1)

def parse_date_day(date: str)->int:
    date_list = date.split('/')
    if is_date(date):
        if 0 < int(date_list[1]) < 32:
            return int(date_list[1])
        else:
            return -1
    else:
        return -1

assert_equal(parse_date_day('Newark,De'),-1)

def parse_date_year(date: str)->int:
    date_list = date.split('/')
    if is_date(date):
        if len(date_list[2]) == 2:
            date_list[2] = int(date_list[2]) + 2000
            if 999 < int(date_list[2]) < 10000:
                return int(date_list[2])
            else:
                return -1
        elif len(date_list[2]) == 4:
            if 999 < int(date_list[2]) < 10000:
                return int(date_list[2])
            else:
                return -1
        else:
            return -1
    else:
        return -1

assert_equal(parse_date_year('Newark,De'),-1)

def equal(sub_date: str, due_date: str)->bool:
    if parse_date_year(sub_date) == parse_date_year(due_date):
        if parse_date_month(sub_date) == parse_date_month(due_date):
            if parse_date_day(sub_date) == parse_date_day(due_date):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def first(sub_date: str, due_date: str)->bool:
    if parse_date_year(sub_date) == parse_date_year(due_date):
        if parse_date_month(sub_date) == parse_date_month(due_date):
            return parse_date_month(sub_date) < parse_date_month(due_date)
        else:
            return parse_date_month(sub_date) < parse_date_month(due_date)
    elif parse_date_year(sub_date) < parse_date_year(due_date):
        return True
    else:
        return False

def earlier(sub_date: str, due_date: str)->str:
    if parse_date_year(sub_date) != -1 and parse_date_year(due_date) != -1:
        if parse_date_month(sub_date) != -1 and parse_date_month(due_date) != -1:
            if parse_date_day(sub_date) != -1 and parse_date_day(due_date) != -1:
                if equal(sub_date, due_date):
                    return 'equal'
                else:
                    if first(sub_date, due_date):
                        return sub_date
                    else:
                        return due_date
            else:
                return 'error'
        else:
            return 'error'
    else:
        return 'error'
    
