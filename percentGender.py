#accept number of females and males in a class and give percentages of each
numMales = input("Enter the number of males in the class here: ")
numMales = int(numMales)

numFemales = input("Enter the number of females in the class here: ")
numFemales = int(numFemales)

students = numMales +numFemales

percentMales = (numMales / students) * 100
percentMales = float(percentMales)

percentFemales = 100 - percentMales
percentFemales = float(percentFemales)

print("There are", percentMales, "% males and", percentFemales, "% females in this class")

