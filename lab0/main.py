import student_code

total_grade = 0

start1 = [1, 3, 2, 8, 9, 11, 100, 4]
final1 = [1, 2, 3, 4, 8, 9, 11, 100]

print("running test 1")
print("input data", start1)
df1 = student_code.order(start1)
print("student sorted data", start1)
print("expected data", final1)
grade = 2
for x in range(len(start1)-1):
    if start1[x] != final1[x]:
        if grade >= 1:
            grade = grade-1
print("grade for test data 1=", grade)
total_grade = total_grade+grade


start1 = []
final1 = []

print("running test 2")
print("input data", start1)
df1 = student_code.order(start1)
print("student sorted data", start1)
print("expected data", final1)
grade = 2
for x in range(len(start1)-1):
    if start1[x] != final1[x]:
        if grade >= 1:
            grade = grade-1
print("grade for test data 2=", grade)
total_grade = total_grade+grade


start1 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
final1 = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


print("running test 3")
print("input data", start1)
df1 = student_code.order(start1)
print("student sorted data", start1)
print("expected data", final1)
grade = 2
for x in range(len(start1)-1):
    if start1[x] != final1[x]:
        if grade >= 1:
            grade = grade-1
print("grade for test data 3=", grade)
total_grade = total_grade+grade


start1 = [-1, -99, 12, 937, 46, 995, -913, 2, 7, 100, 7, 901, 55, 0, 0, 0]
final1 = [-913, -99, -1, 0, 0, 0, 2, 7, 7, 12, 46, 55, 100, 901, 937, 995]


print("running test 4")
print("input data", start1)
df1 = student_code.order(start1)
print("student sorted data", start1)
print("expected data", final1)
grade = 2
for x in range(len(start1)-1):
    if start1[x] != final1[x]:
        if grade >= 1:
            grade = grade-1
print("grade for test data 4=", grade)
total_grade = total_grade+grade


start1 = [1]
final1 = [1]

print("running test 4")
print("input data", start1)
df1 = student_code.order(start1)
print("student sorted data", start1)
print("expected data", final1)
grade = 2
for x in range(len(start1)-1):
    if start1[x] != final1[x]:
        if grade >= 1:
            grade = grade-1
print("grade for test data 4=", grade)
total_grade = total_grade+grade


print("\ntotal correct in test cases out of 10 is", total_grade, "\n")
