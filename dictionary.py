from cisc108 import assert_equal

# Address
Address = {'street': str, 'number': int, 'zipcode': str, 'state': str}

'''
Define a function last_house_on_street that consumes a list of Addresses and the name of a desired street (a string),
and produces a string representing the street with the desired name that has the highest number. The string should be
the street's number followed by its number, with a space between (e.g., "18 Amstel").
'''
def last_house_on_street(addresses: [Address], desired_street: str)->str:
    desired = []
    for address in addresses:
        if address['street'] == desired_street:
            desired.append(address)
    
    highest = desired[0]['number']
    name = desired[0]['street']
    for desire in desired:
        if desire['number'] >= highest:
            highest = desire['number']
            name = desire['street']
    return str(highest) + ' ' + name

assert_equal(last_house_on_street([{'street': 'Aikens', 'number': 9, 'zipcode': '19808', 'state': 'de'},
                                   {'street': 'crossfolk', 'number': 1000, 'zipcode': '19702', 'state': 'de'},
                                   {'street': 'Aikens', 'number': 816, 'zipcode': '19808', 'state': 'de'}], 'Aikens'), '816 Aikens')
'''
Define first_house_on_street where you find the minimum instead.
'''
def first_house_on_street(addresses: [Address], desired_street: str)->str:
    desired = []
    for address in addresses:
        if address['street'] == desired_street:
            desired.append(address)
    
    lowest = desired[0]['number']
    name = desired[0]['street']
    for desire in desired:
        if desire['number'] <= lowest:
            lowest = desire['number']
            name = desire['street']
    return str(lowest) + ' ' + name

assert_equal(first_house_on_street([{'street': 'Aikens', 'number': 9, 'zipcode': '19808', 'state': 'de'},
                                   {'street': 'crossfolk', 'number': 1000, 'zipcode': '19702', 'state': 'de'},
                                   {'street': 'Aikens', 'number': 816, 'zipcode': '19808', 'state': 'de'}], 'Aikens'), '9 Aikens')

'''
Define find_houses_in_state which consumes a list of addresses and a state (string), and returns a list of the addresses
with the given state.
'''
def find_houses_in_state(addresses: [Address], desired_state: str)->[Address]:
    desired = []
    for address in addresses:
        if address['state'].upper() == desired_state.upper():
            desired.append(address)
    return desired
    
assert_equal(find_houses_in_state([{'street': 'Aikens', 'number': 9, 'zipcode': '19808', 'state': 'de'},
                                   {'street': 'crossfolk', 'number': 1000, 'zipcode': '19702', 'state': 'de'},
                                   {'street': 'Aikens', 'number': 816, 'zipcode': '19808', 'state': 'de'}], 'dE'),
                                     [{'street': 'Aikens', 'number': 9, 'zipcode': '19808', 'state': 'de'},
                                   {'street': 'crossfolk', 'number': 1000, 'zipcode': '19702', 'state': 'de'},
                                   {'street': 'Aikens', 'number': 816, 'zipcode': '19808', 'state': 'de'}])

'''
Define get_house_numbers which consumes a list of addresses and returns just their numbers as a list of integers
'''
def get_house_numbers(addresses: [Address])->[int]:
    numbers = []
    for address in addresses:
        numbers.append(address['number'])
    return numbers

assert_equal(get_house_numbers([{'street': 'Aikens', 'number': 9, 'zipcode': '19808', 'state': 'de'},
                                   {'street': 'crossfolk', 'number': 1000, 'zipcode': '19702', 'state': 'de'},
                                   {'street': 'Aikens', 'number': 816, 'zipcode': '19808', 'state': 'de'}]), [9, 1000, 816])

# Grocery
Item = {'name': str, 'price': float, 'kind': str}
Grocery_store = {'freezer section': [Item], 'fruits and vegetables': [Item], 'unsorted': [Item]}

'''
Define a function named most_expensive_freezer_item that consumes a Grocery Store and produces a string representing the
name of the most expensive item from the Freezer Section.
'''


'''
Define a function named biggest_section that consumes a Grocery Store, and produces a string (either, "Freezer",
"Fruits and Veggies", or "Equal") that indicates which of those sections has more items in it (or are equal).
'''



# Email
Email = {'header': str, 'body': str, 'from': str}
e1 = [{'header': 'Goodmorning!', 'body': 'I welcome you to join our special festival today.', 'from': 'avinash'},
    {'header': 'bonjour', 'body': 'thank you forc coming', 'from': 'john'},
    {'header': 'hi', 'body': 'im happy', 'from': 'aksy'}]
e2 = [{'header': 'Goodnight!', 'body': 'today was wonderful lets meet agin, we hada good ite mlets meet again', 'from': 'avi'},
    {'header': 'bad', 'body': 'you were terrible todya. your acting was teash dont evern come here in your lfie', 'from': 'evil'},
    {'header': 'money', 'body': 'join this investignf group for more information check out the link down bwlo', 'from': 'bcoin marekr sdjjd'}]

'''
Define a function biggest_inbox that consumes two parameters (a list of emails and another list of emails) and produces a
string (either "bigger" or "not bigger"). The function returns "bigger" if the total number of characters of all the emails
in the body and header of the first list is more than the total of the second list. Otherwise, return "not bigger".
'''
def biggest_inbox(emails1: [Email], emails2: [Email])->str:
    total_1 = 0
    total_2 = 0
    
    for email in emails1:
        total_1 += len(email['header'])
        total_1 += len(email['body'])
        total_1 += len(email['from'])
    
    for email in emails2:
        total_2 += len(email['header'])
        total_2 += len(email['body'])
        total_2 += len(email['from'])
        
    if total_1 > total_2:
        return 'Bigger'
    else:
         return 'not bigger'
        
assert_equal(biggest_inbox(e1, e2), 'not bigger')

'''
Define a function most_popular_sender that consumes three parameters (a list of emails, another list of emails, and a string
representing a given sender) and produces a string (either "first", "second", or "equal"). The function returns "first" if the
number of emails with the given sender in the first list is more than the number of emails with the given sender in the
second list; if they're equal, return "equal", and otherwise return "second".
'''


