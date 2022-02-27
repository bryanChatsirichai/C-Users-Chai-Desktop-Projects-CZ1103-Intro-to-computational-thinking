def colour(color): # colour argument not needed.Is just to print red, blue ,or green in input
    count = 1
    while count < 4:
        colour_str = input("Enter the value of the " + color +\
                           " color for message (0 to 255):")  # colour parameter print red, blue ,or green in input
        try:
            converted = int(colour_str)
        except ValueError: # no exception name mean catch all
            print("Not a number")
            count += 1
            continue
        # finally: try / except /finally
        # Finally have to be the last no else or what behind

        if converted > 255:
            print("Out of range to high")
            count += 1
            continue
        if converted < 0:
            print("Out of range to low")
            count += 1
            continue
        elif 0 <= converted <= 255:  # with in 3 try and accepted value
            return converted
    else:
        return 0  # return 0 if fail 3 times



