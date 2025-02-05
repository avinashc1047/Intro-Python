today = "Tuesday"
def is_early(day_of_week: int) -> bool: 
    return day_of_week < 2 
 
def is_late(day_of_week: int) -> bool: 
    return day_of_week >= 4 
 
def convert_date(date: str) -> int: 
    if date.lower() == 'monday': 
        return 0 
    elif date.lower() == 'tuesday': 
        return 1 
    elif date.lower() == 'wednesday': 
        return 2 
    elif date.lower() == 'thursday': 
        return 3 
    elif date.lower() == 'friday': 
        return 4 
    else: 
        return 5 
      
def is_valid_day(date: str) -> bool: 
    return date.endswith('day') 
 
def get_today() -> str: 
    date = input("What is the current day of the week?") 
    if not is_valid_day(date): 
        return "Unknown day" 
    return date.title() 
 
def main(): 
    today = get_today() 
    print("Today is", today) 
    day_of_week = convert_date(today) 
    if is_early(day_of_week): 
        print("You have plenty of time, relax!") 
    elif is_late(day_of_week): 
        print("Well, it's too late now. Better give up!") 
    else: 
        print("It's not even due yet! It can wait.") 
      
main()
status = is_early(convert_date(today))
print(status)