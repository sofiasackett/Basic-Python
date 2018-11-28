#This program will generate a UAlbany system login name given a users first and last names and birth year

#program greetings and inputs
print("We are going to generate a UAlbany system login name. \n")
first_name = input("Enter your first name here: ")
last_name = input("Enter your last name here: ")
birth_year = input("Enter the year you were born here: ")

#compute first six letters of last name
shortened_last = last_name[:6]

#add first initial to first six letters of last name
initial = first_name[0]
name = shortened_last + initial

#add last two digits of birth year
year = birth_year[2:]
login = name + year

#print result
print("\n")
print("Your system login name is", login)
