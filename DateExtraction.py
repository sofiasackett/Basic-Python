# Sofia Sackett
# This program extracts and prints dates and number of lightning strikes in Albany

# Open UAlbanyLightning.txt file 
file = open("UAlbanyLightning.txt", "r")

# Create a for loop to print date and number of strikes per day
for line in file:
    line = line.strip()

    # Use if-elif-else to avoid empty strings and header column
    if len(line) == 0:
        continue
    elif line.startswith("DAY"):
        continue
    else:
        # Separate data by commas
        data = line.split(",")
        
        # Split the date by dashes and create variable with reformatted date
        splitDate = data[0].split("-") 
        date = (splitDate[1] + "-" + splitDate[2] + "-" + splitDate[0])

       # Print number of lightning strikes per day 
        print(date + ": " + data[3] + " lighting strikes were recorded.")

file.close()



