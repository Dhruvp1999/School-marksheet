""""Write a program that takes a student's score as input and prints the corresponding grade. Use the following grading scale:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F"""

grade = int(input('Enter your grades : '))
if (grade > 90 ) :
    print('Your grade is A ' )
    print(grade)
elif ( 80 <= grade < 89) :
    print('Your grade is B')
    print(grade)
elif ( 70 <= grade < 79) :
    print('Your grade is C')
    print(grade)
elif ( 60 <= grade < 69) :
    print('Your grade is D')
    print(grade)
else :
    print ('Your grade is F')
