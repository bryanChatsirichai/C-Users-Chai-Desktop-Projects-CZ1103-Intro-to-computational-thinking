def inputRecord(dataBase, group, id, score):
    data_key = (group, id) # key
    dataBase[data_key] = score # value

def query(dataBase, group, id): # return individual score
    try:
        data_key = (group, id)
        return dataBase[data_key]
    except:
        return None

def listGrades(dataBase, group):
    list_of_score = []
    for key, value in dataBase.items():
        if key[0] == group: #('FS1', 1) means same FS grp
            list_of_score.append(value)
    return list_of_score

def maxGrade(dataBase, group):
    score = listGrades(dataBase,group)
    return max(score)

def read_data():
    groupName = input("Please input the group name: ")
    sID = int(input("Please input the student id: "))
    score = int(input("Please input the score: "))
    return {
            ('group'): groupName,
            ('ID'): sID,
            ('score'): score
            }  #return dictionary


full_list = {}
data = read_data()
while data[('score')] != -1:
    inputRecord(full_list, data[('group')], data[('ID')], data[('score')])
    data = read_data() # invoke to enter student again
print(full_list)
individual_score = query(full_list, str(input('individual score enter grp ')), int(input('indicidual enter input id ')))
print(individual_score)
list_grades = listGrades(full_list, str(input('Group list ')))
print(list_grades)
highest_score = maxGrade(full_list, input("enter grp for max grades inside"))