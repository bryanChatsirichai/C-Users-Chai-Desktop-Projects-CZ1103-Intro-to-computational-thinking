count = 0
while True:
    string = input('Enter a string')
    if string == "#":
        break
    for let in string:
        if let == 'a':
            count += 1
            break
    print(count, "String with letter 'a' ")

