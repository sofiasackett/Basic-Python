# Sofia Sackett
# This program extracts, prints out, and writes the name portion of email addresses to a file called addr.txt

# Open mbox2.txt file and use try/except to check for unopenable files
try:
    file = open("mbox2.txt", "r")
except:
    print("The file cannot be opened.")
    exit()
else:

    # Create and open addr.txt
    newFile = open("addr.txt", "w")

    # Program explanation
    print("The name portions of the emails contained in 'mbox2.txt' are: ")

    # For loop to extract name portion of emails and append addr.txt file
    for line in file:
        line = line.rstrip()
        if line.startswith("From:"):
            email = line[6:]
            name = email.split("@")
            name = name[0]
            newFile.write("\n")
            newFile.write(name)

    # Close files
    file.close()
    newFile.close()

    # Open addr.txt for reading and print the contents
    addr = open("addr.txt", "r")
    emails = addr.read()
    print(emails)
    addr.close()

