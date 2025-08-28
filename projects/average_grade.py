#BZ 1st Average Grade
grades = []
periods = input("How many classes do you have? > ")
average = 0
for i in range(1, int(periods) + 1):
    grades.append(input(f"percentage grade in class {i}? > "))
for i in grades:
    average = average + int(i)
average = round(average / len(grades), 2)
print(f"your average grade is {average}.")