"""
Prog: Student Roll
Name: Isabella Holloway
Date: 02/05/18
Desc: Creates list, add student, remove student, change student, with 2 challenges
"""

roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
student2 = roll[2]
print(student2)
enrolment = len(roll)
print(enrolment)
roll.append('James')
print(roll[10])
del roll[2]
print(roll[2])
roll[5] = 'Mike'
print(roll[5])
list.sort(roll)
print(roll)
list.reverse(roll)
print(roll)
