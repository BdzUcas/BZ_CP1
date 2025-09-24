#BZ 1st What is my Grade
while True:
    percentage = input('What is your grade?\n> ').strip()
    if percentage.replace('.','').isdigit():
        percentage = float(percentage)
        break
    else:
        print('Please enter a number.')
letter_grades = ['n F',' D-',' D',' D+',' C-',' C',' C+',' B-',' B',' B+','n A-','n A']
percent_grades = [54,63,66,69,71,76,79,81,86,89,91,100]
for i in percent_grades:
    if percentage <= i and percentage > percent_grades[percent_grades.index(i)-1]:
        print(f'Your grade is {percentage}, a{letter_grades[percent_grades.index(i)]}!')
if percentage < 0:
    print('Stop lying you\'re not that bad')
elif percentage == 0:
    print('You should probably not be taking this class.')
elif percentage < 54:
    print('Looks like you\'re failing!')
elif percentage < 71:
    print('Get your grades up!')
elif percentage < 80:
    print('Cs get degrees!')
elif percentage < 90:
    print('Keep it up!')
elif percentage < 100:
    print('Nice Job!')
elif percentage == 100:
    print('Perfect grade!')
elif percentage < 116:
    print('Wow, extra credit!')
elif percentage < 150:
    print('Thats... suspiciously high.')
else:
    print('Stop lying to yourself.')