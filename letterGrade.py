# This program calculates letter grade given a raw score between 0 and 100

#accept raw score as a numeric grade between 0 and 100
raw_score = float(input("Enter the raw score as a number between 0 and 100: "))
raw_score = round(raw_score)

#determine final letter grade and print 
if raw_score >= 93 and raw_score<= 100:
    letter_grade = "A"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=90 and raw_score <=92:
    letter_grade = "A-"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=87 and raw_score <=89:
    letter_grade = "B+"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=83 and raw_score <=86:
    letter_grade = "B"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=80 and raw_score <=82:
    letter_grade = "B-"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=77 and raw_score <=79:
    letter_grade = "C+"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=73 and raw_score <=76:
    letter_grade = "C"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=70 and raw_score <=72:
    letter_grade = "C-"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=67 and raw_score <=69:
    letter_grade = "D+"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=63 and raw_score <=66:
    letter_grade = "D"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score>=60 and raw_score <=62:
    letter_grade = "D-"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
elif raw_score >=0 and raw_score <=59:
    letter_grade = "E"
    print("A raw score of", raw_score, "corresponds to a letter grade of " + str(letter_grade), ".")
if raw_score > 100 or raw_score < 0:
    print("The number you entered was out of the acceptable range. Please try again.")
