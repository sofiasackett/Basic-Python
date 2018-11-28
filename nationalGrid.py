#Compute running total of heating and cooling days

#program greetings and set counters
cooling_count = 0
heating_count = 0 
print("Enter a series of temperatures then press the enter key to quit.")
temp = input("Enter a temperature: ")

#input temperatures
while temp !="":
    temp = float(temp)
    if temp < 60:
        heating_count = heating_count + 1
    elif temp > 80:
        cooling_count = cooling_count + 1
    temp = input("Enter a temperature: ")

#print output
print("The temperatures you entered contain", cooling_count)
print("cooling degree day(s) and", heating_count, "heating degree day(s).")

    
