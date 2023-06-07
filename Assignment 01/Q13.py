#WAP to create a dictionary of student marks in five subjects and you have to find the student having maximum and minimum average marks.
student_marks = {
    'Aditya': [80, 85, 90, 92, 88],
    'Vasistha': [75, 78, 82, 80, 85],
    'c': [90, 92, 95, 88, 92],
    'Ravi': [78, 82, 80, 85, 88],
    'Sanchi': [85, 88, 90, 92, 85]
}

#average marks for each student
averages = {}
for student, marks in student_marks.items():
    average = sum(marks) / len(marks)
    averages[student] = average

# maximum and minimum average marks
max_average_student = max(averages, key=averages.get)
min_average_student = min(averages, key=averages.get)

print(f"Student with maximum average marks: {max_average_student}, Average marks: {averages[max_average_student]}")
print(f"Student with minimum average marks: {min_average_student}, Average marks: {averages[min_average_student]}")
