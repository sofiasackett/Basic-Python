#this program will create a 5 question quiz using conditional statement

#program greetings
print("Get ready for a quiz.. good luck!!")

#question 1
print("\n")
print("#1: What is the scientific name for a tiger?")
print("   A) Puma concolor")
print("   B) Acinoynx jubatus")
print("   C) Panthera tigris")
print("   D) Panthera pardus")
q1 = input("Enter your answer here: ").lower()

correct = 0
if q1 == "c":
    print("Correct!")
    correct = correct + 1
    
elif q1 != "c":
    print("Sorry, the correct answer was C) Panthera Tigris")
    
#question 2
print("\n")
print("#2: True or False - A tiger is the largest of the big cats.")
q2 = input("Enter your answer here: ").lower()

if q2 == "true":
    print("Correct!")
    correct = correct + 1
elif q2 != "true":
    print("Sorry, the correct answer was true.")
    
#question 3
print("\n")
print("#3: Fill in the blank - Tiger hunts are only successful about one in every  _____ attempts.")
q3 = int(input("Enter your answer here: "))

if q3 >= 10 or q3 <=20:
    print("Correct!")
    correct = correct + 1
else:
    print("Sorry, the correct answer was between 10 and 20.")
    
#question 4
print("\n")
print("#4: How many pounds of meat can a tiger eat in one sitting?")
print("   A) 88 lbs")
print("   B) 60 lbs")
print("   C) 305 lbs")
print("   D) 12 lbs")
q4 = input("Enter your answer here: ").lower()

if q4 == "a":
    print("Correct!")
    correct = correct + 1
    
else:
    print("Sorry, the correct answer was A) 88 lbs!")
    
#question 5
print("\n")
print("#5: What is the term for a group of tigers?")
print("   A) pride")
print("   B) streak")
print("   C) gaggle")
print("   D) pod")
q5 = input("Enter your answer here: ").lower()

if q5 == "b":
    print("Correct!")
    correct = correct + 1
    
else:
    print("Sorry, the correct answer was B) streak")

#calculate and print percent correct
if correct == 5:
    print("Congrats! You got 100% correct!")
elif correct == 4:
    print("Nice job, you got 80% correct!")
elif correct == 3:
    print("You got 60% correct!")
elif correct == 2:
    print("Uh oh! You only got 40% correct.")
elif correct ==1:
    print("Brush up on your tiger facts! You only got 20% correct.")
else:
    print("Sorry, you got a 0% - better luck next time!")
    

