import secrets
import time

letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!§$%#*'
used_alphabets = letters_lowercase + letters_uppercase + numbers + special_characters



print('Choose your password length: \n')

password_length = int(input())


print('Choose the number of passwords: \n')

password_count = int(input())

print('')

if password_count == 1:
    print('>>>Your password is<<<')
elif password_count == 0:
    print('>>>No password<<<')
else:
    print('>>>Your passwords are<<<')

print('')

for j in range(password_count):
        password = ''.join(secrets.choice(used_alphabets)
            for i in range(password_length))
        print(password)

print('')

time.sleep(120)