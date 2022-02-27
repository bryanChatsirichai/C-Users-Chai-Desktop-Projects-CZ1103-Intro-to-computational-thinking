boys = int(input("Enter the number of boys "))
girls = int(input("Enter the number of girls"))
total = girls + boys
b_percent = (boys / total) * 100
g_percent = (girls / total) * 100
print('Boys: {0:.0f} and girls: {1:.0f}'.format(b_percent, g_percent))
