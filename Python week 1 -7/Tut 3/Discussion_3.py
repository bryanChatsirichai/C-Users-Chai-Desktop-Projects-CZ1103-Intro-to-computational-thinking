grades = {
 ('FS1', 1) : 45,
 ('FS1', 2) : 75,
 ('FS1', 3) : 25,
 ('FS1', 4) : 65,
 ('FS2', 1) : 75,
 ('FS2', 2) : 40,
 ('FS2', 3) : 70,
 ('FS2', 4) : 80
}

print(grades[('FS1', 1)])
print(grades.items())
for key,value in grades.items():
 print(value)
for key,value in grades:
 print(key,value)
