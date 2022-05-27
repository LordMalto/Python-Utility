import secrets
import time

letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!§$%#*'
used_alphabets = letters_lowercase + letters_uppercase + numbers + special_characters



print('Choose your password length: \n')

password_length = input()
password_length_int = int(password_length)

print('Choose the number of passwords: \n')

password_count = input()
password_count_int = int(password_count)



print('')

if password_count_int == 1:
    print('>>>Your password is<<<')
else:
    print('>>>Your passwords are<<<')

print('')

for j in range(password_count_int):
        password = ''.join(secrets.choice(used_alphabets)
            for i in range(password_length_int))
        print(password)

print('')

time.sleep(120)