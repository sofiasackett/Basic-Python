# Sofia Sackett
# This program extracts and prints dates and number of lightning strikes in Albany

# Open UAlbanyLightning.txt file and use try/except to check for unopenable files
try:
    file = open("UAlbanyLightning.txt", "r")
except:
    print("The file cannot be opened.")
else:

#

    # Close file
    file.close()
