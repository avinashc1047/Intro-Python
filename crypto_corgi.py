"""
# Crypto Corgi Company
Build some simple functions that encrypt, decrypt, and hash text
for cryptography purposes.
Date: Spring 2020
Course: CISC108
School: University of Delaware

# When You Are Done
When you pass all tests, remember to clean and document your code.
But we will be reviewing your documentation and code quality!
Yes, you have to unit test all your functions.
"""
from cisc108 import assert_equal

def rotate(character: int, rotation_amount: int)->int:
    '''Function: Rotates the character values using the formula and then returns it.
       
       Arguments: character(int)-the value of the character,
       rotation_amount(int)-the value to rotate the character with.
       
       Returns: integer, after the rotation is complete.'''
    
    return (character + rotation_amount - 32) % 94 + 32

assert_equal(rotate(65, 1), 66)
assert_equal(rotate(66, 25), 91)
assert_equal(rotate(50, -30), 114)

def encrypt_text(plain_txt: str, rotation_amount: int)->str:
    '''Function: Encrypts a message. Creates a variable int_list and then uses a for loop
       to convert individual values in the message to integers and add to the int_list. Then
       creates a new variable new_list, uses a for loop with if statements to check if a value
       from the int_list is greater than 48 or not. If the value is greater it uses the helper
       function rotate and adds the rotated number to the newlist, else it adds the rotated number
       and 126 to the list at the same time. In the end it uses a for loop to convert the rotated
       integer list to a list of str and adds all of them together to print em out.
       
       Arguments: plain_txt(str)-the message that someone wants to encrypt,
       rotation_amount(int)-the amount that the value will rotate by.
       
       Returns: str value of the encrypted message.'''
    
    int_list = []
    for character in list(plain_txt):
        int_list.append(ord(character))
    
    new_list = []
    for value in int_list:
        if rotate(value, rotation_amount) > 48:
            new_list.append(rotate(value, rotation_amount))
        else:
            new_list.append(rotate(value, rotation_amount))
            new_list.append(126)
    
    str_list = []
    txt = ''
    for value in new_list:
        str_list.append(chr(value))
    
    return txt.join(str_list)

assert_equal(encrypt_text('A', 1), 'B')
assert_equal(encrypt_text('Hello', 29), 'e$~+~+~.~')
assert_equal(encrypt_text('Aa', 1), 'Bb')

def decrypt_text(encrypt_txt: str, rotation_amount: int)->str:
    '''Function: Decrypt an ecrypted message. Creates a new variable int_list, then uses
       a for loop to create integers and add them to new_list using the ord() function.
       Creates another variable rotated_list and uses a for loop to rotate the individual values
       from the new_list and add then to the rotated_list. If the value in the new_list is 126 then
       it skips over it however if it's not then it adds the rotated value to the rotated_list. In the
       end it converts the rotated_list into a str using chr() and joins it together to print the
       decrypted message. 
    
       Arguments: encrypt_txt(str)-the encrypted str of text that the user has,
       rotation_amount(int)-the amount of rotatuon that was used while encrypting the text.
       
       Returns: The decrypted text message in the form of a string.'''
    
    int_list = []
    for value in list(encrypt_txt):
       int_list.append(ord(value))
    
    rotated_list = []
    for value in int_list:
        if value == 126:
            pass
        else:
            rotated_list.append(rotate(value, (rotation_amount * -1)))
    
    str_list = []
    txt = ''
    for value in rotated_list:
        str_list.append(chr(value))
    
    return txt.join(str_list)

assert_equal(decrypt_text('B', 1), 'A')
assert_equal(decrypt_text('e$++.', 29), 'Hello')
assert_equal(decrypt_text('Bb', 1), 'Aa')

def hash_text(txt: str, base: int, hash_size: int)->int:
    '''Function: Creates an int_list using a for loop from the txt argument and the ord().
       Uses the count loop and the for loop to find the new_value using the (count+base**value),
       and then add this value to the new_list. Later uses a total loop to create a sum of all the
       values in the new_list. In the end it returns the total value % the hash_size.
       
       Arguments: txt(str)-the encrypted message that neesds to be turned into a manageable int,
       base(int)-the base number which is used in the equation ot find new_value, 
       hash_size(int)-the value with which the total sum is divided and returned. 
       
       Returns: The remainder of the total/hash_size, this is a manageable number compared to
       the large numebr we would usually get.'''
    
    int_list = []
    for character in list(txt):
        int_list.append(ord(character))
    
    count = 0
    new_list = []
    for value in int_list:
        new_value = (count + base) ** (value)
        new_list.append(new_value)
        count += 1
        
    total = 0
    for value in new_list:
        total += value
    
    return total % hash_size

assert_equal(hash_text('A', 11, 100), 51)
assert_equal(hash_text('ABC', 11, 100), 52)
assert_equal(hash_text('Hello', 31, 1000000000), 590934605)
    

def main():
    '''Function: the main function. Asks the user what they want to do, encrypt or decrypt a msg.
       If the user type encrypt it asks the user for their txt message and encrypts it using
       encrypt() and also creates a unique hash value, using hash_text(). Elif the user type decrypt,
       it asks the user for the encrypted msg and the unique hash. It decrypts the added text and then
       compares its hash with the user's unique hash. If the two hash vals are equal then it prints the
       decrypted msg and if not it lets the user know that the hash is differnent, therefore someone
       messed with the message. If the user doesn't type anything other than encrypt and decrypt, an error
       msg is returned. 
       
       Arguments: No arguments as all the information is collected when the function is run.
       
       Returns: Depending on the input of the user. If the user types encrypt, the decrypted text is printed
       with its unique hash value. Elif decryted is type in, the decrypted msg is printed out. Else an error
       is printed. '''
    
    decision = input("Type your desired action: ")
    
    if decision.lower() == 'encrypt':
        txt = input('Type your text message: ')
        encrypted = encrypt_text(txt, 21)
        hash_val = hash_text(txt, 31, 1000000000)
        print(encrypted)
        print(hash_val)
    elif decision.lower() == 'decrypt':
        encrypt_txt = input('Type your encrypted text message: ')
        decrypted = decrypt_text(encrypt_txt, 21)
        expected_hash = input('Type your unique hash value: ')
        
        if hash_text(decrypted, 31, 1000000000) == int(expected_hash):
                print(decrypted)
        else:
            print('error. The decrypted message was intercepted and changed!')
    else:
        print('An error occured. You did not input the correct action.')

main()

#Extra-Credit
'''
1. Security through obscurity essentialy means, being secure as you don't have any information.
In a company this could mean that secure information is exchanged through only certain people, as none
except them know how to access or interpret it. This would be bad for a company that wants to send encrypted
messages to all its members as everyone would need to have a special way of access and when you tell so many
people about an acces point it is likely to leak. 

2. Integrity refers to the security of the information as its being sent between two people, and making sure
that the information is not changed in any way. Authentication refers to a person actually sending
the information to the person that they want. Whereas confientiality is where we make sure that nobody
except the two people read the sent information. Given these terms when sending the hashvalue you should 
prioritize authentication and confidentiality, and not integrity as we would instantly know if someone
changed the value and this would not affect the actual encrypted value. As for sending the encrypted message
you want to make sure that you prioritize authentication and integrity, and not confidentiality as even if
someone gets the encrypted message they won't understand it. 

3. SKIP

4.
!~>RcWRHNW=><H=>=WMA>W?BKLMWEBG>cWMA:M^LWK>:EERW@K>:MX = Hey, you decoded the first line, that's really great!
55 was the rotation amount.

d;(~+~,~4;1%~&~0;&~0;|;1,~2$~%~;0"~*~"~01"~/~;#~,~/~;"~3"~/~6,~+~"~I = I know this is a tough semester for everyone.
27 was the rotation amount.

mBAKtKD.~;A21KF<BKA<K8;<DKA5.~AKD2K.~?2K=?<B1K<3KF<BKeT = But I wanted you to know that we are proud of you :)
43 was the rotation amount.

Here is the code I used to solve this:
from cisc108 import assert_equal

def rotate(character: int, rotation_amount: int)->int:
    
    return (character + rotation_amount - 32) % 94 + 32

def decrypt_text(encrypt_txt: str, rotation_amount: int)->str:
    
    int_list = []
    for value in list(encrypt_txt):
       int_list.append(ord(value))
    
    rotated_list = []
    for value in int_list:
        if value == 126:
            pass
        else:
            rotated_list.append(rotate(value, (rotation_amount * -1)))
    
    str_list = []
    txt = ''
    for value in rotated_list:
        str_list.append(chr(value))
    
    return txt.join(str_list)

def find(txt:str)->int:
    int_list = []
    for each in range(0,100):
       strs = decrypt_text(txt, each)
       if ' ' in strs:
           int_list.append(each)
       else:
            pass
    return int_list

def search(txt:str)->str:
    int_list = find(txt)
    for value in int_list:
        print(decrypt_text(txt, value))
        print(value)

#search('!~>RcWRHNW=><H=>=WMA>W?BKLMWEBG>cWMA:M^LWK>:EERW@K>:MX')
#search('d;(~+~,~4;1%~&~0;&~0;|;1,~2$~%~;0"~*~"~01"~/~;#~,~/~;"~3"~/~6,~+~"~I')
#search('mBAKtKD.~;A21KF<BKA<K8;<DKA5.~AKD2K.~?2K=?<B1K<3KF<BKeT')

'''