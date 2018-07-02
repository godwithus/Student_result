"""
    We get inputs from the user (Student name, Missing assignment, Present grade)
    then we multiply the missing assignment by 2
    
"""

s_name = input('Input the name of Students: ')
s_name = s_name.replace(" ", "")
s_name = s_name.split(",")

assignments = input('Input the value for assignment: ')
assignments = assignments.replace(" ", "")
assignments = assignments.split(",")


grade = input('Input the value for grade: ')
grade = grade.replace(" ", "")
grade = grade.split(",")

assignment_new_array = []
s_name_new_array = []
grade_new_array = []

i = 0

while i < len(grade):
    s_name_new_array.append(str(s_name[i]))
    assignment_new_array.append(int(assignments[i]))
    grade_new_array.append(int(grade[i]))    
    
    i += 1

print('Student Name: ', s_name_new_array)
print('Missing Assignment: ', assignment_new_array)
print('Grade before addition: ', grade_new_array)


print()
print()

i = 0

message = "We work on your result bellow"
while i < len(grade_new_array):
    p_grade = grade_new_array[i] + (assignment_new_array[i] * 2)
    m_grade = grade_new_array[i]
    
    print(s_name_new_array[i], message)
    print('your potential grade ' , p_grade)
    print('your present grade ', m_grade)
    print()

    i += 1;
