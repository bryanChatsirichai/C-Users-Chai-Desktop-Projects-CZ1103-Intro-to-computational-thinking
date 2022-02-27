def inputRecord(dataBase, group, id, score):
    data_key = (group, id) # key
    dataBase[data_key] = score # value

def query(dataBase, group, id):
    try:
        data_key = (group, id)
        return dataBase[data_key] # use key to access value
    except:
        return None

def listGrades(dataBase, group):
    list_of_score = [] #local to this function
    for key, value in dataBase.items():
        if key[0] == group: # ('FS1', 1) means some 'FS' index[0], student_id[1]
            list_of_score.append(value)
    return list_of_score

def maxGrade(dataBase, group):
    score = listGrades(dataBase, group) # create a list of all student grades(value) in that group
    return max(score)

def grp_names(dataBase, group):
    names = listGrades(dataBase, group) # create a list of all student names in that group
    return names

def read_data(): # input student
    groupName = input("Please input the group name: ")
    sID = int(input("Please input the student id: "))
    score = int(input("Please input the score: "))
    return {
            ('group'): groupName,
            ('ID'): sID,
            ('score'): score
            }  #return dictionary


def main():
    data_base = {}
    get_data = True
    while get_data:

        print("Welcome to the grading system! Please enter your option: ")
        print('1: input record')
        print('2: query a student')
        print('3: List grades in a group')
        print('4: get max in a group')
        print('5: list all group names')
        print('6: exit')
        option = int(input("Welcome to the grading system! Please enter your option: "))
        if option == 1:
            data = read_data() # input student
            while data[('score')] != -1:
                inputRecord(data_base, data[('group')], data[('ID')], data[('score')]) # assign to dict data_base
                data = read_data() # another input until -1 enter
            print(data_base)

        elif option == 2:
            group = str(input('Enter group name '))
            s_ID = int(input('Enter individual input id '))
            individual_score = query(data_base, group, s_ID)
            print(individual_score)

        elif option == 3:
            group = str(input('Group list '))
            list_grades = listGrades(data_base, group)
            print(list_grades)

        elif option == 4:
            group = str(input("enter grp for max grades inside "))
            highest_score = maxGrade(data_base, group)
            print(highest_score)

        elif option == 5:
            group = str(input("enter grp to get all names inside "))
            names_list = grp_names(data_base, group)
            print(names_list)

        elif option == 6:
            get_data = False

main()