password = input('Enter password')
min_length = 8
upcase = False
lowcase = False
digit = False
for letter in password:
    if letter.isupper():
        upcase = True
    if letter.islower():
        lowcase = True
    if letter.isdigit():
        digit = True
length = len(password)

strong = upcase and lowcase and digit and length > min_length

if strong:
    print("your password {0} is good".format(password))
else:
    print('your password {0} is too weak'.format(password))