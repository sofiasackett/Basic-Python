# Sofia Sackett
# This program will identify a correctly formed IP address

# Get user input and separate address by section
ip = input("Please enter an IP address separated by a dash (-): ")
delimiter = "-"
splitAddress = ip.split(delimiter)

# Set each section of the address equal to a unique variable
section1 = splitAddress[0]
section2 = splitAddress[1]
section3 = splitAddress[2]
section4 = splitAddress[3]

# Define a function to check for valid section values
def validSection(s):
    if s.isalpha():
        return("This section does not contain an integer.")
    else:
        s = int(s)
        if s >= 0 and s <= 255:
            return("This section is valid.")
        elif s <= 0 or s >= 255:
            return("This section is outside the range of acceptable integers.")

# Create a new variable for each section check
check1 = validSection(section1)
check2 = validSection(section2)
check3 = validSection(section3)
check4 = validSection(section4)

# Output for each section
print("Section 1: " + str(check1))
print("Section 2: " + str(check2))
print("Section 3: " + str(check3))
print("Section 4: " + str(check4))
