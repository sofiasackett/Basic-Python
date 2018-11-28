# Convert temperature from celsius to fahrenheit using functions

def main():
    temp = float(input("Enter a temperature in degrees Celsuis: "))
    print("Temperature in degrees Fahrenheit: ", convertTemp(temp))

def convertTemp(degrees):
    fahrenheit = degrees * 9/5+ 32
    return fahrenheit

main()
