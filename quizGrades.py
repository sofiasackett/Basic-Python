#accept a quiz score as input and print out the corresponding letter grade
quizScore = input("Enter a quiz score from 1 to 10: ")
if quizScore == '10':
    grade = 'A'
    print(grade)
elif quizScore == '9':
    grade = 'A-'
    print(grade)
elif quizScore == '8':
    grade = 'B'
    print(grade)
elif quizScore == '7':
    grade = 'C'
    print(grade)
elif quizScore == '6':
    grade = 'D'
    print(grade)
elif quizScore == '5':
    grade = 'D-'
    print(grade)
elif quizScore == '4' or quizScore =='3' or quizScore =='2' or quizScore =='1' or quizScore =='0':
    grade = 'E'
    print(grade)
else:
    print("Not a valid quiz score")
