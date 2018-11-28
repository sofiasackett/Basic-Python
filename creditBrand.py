# This program will determine the brand of credit card given the card number

#input number and get first number of card
card = (input("Enter your 16-digit credit card number: "))
first_number = card[0]
first_number = int(first_number)
if len(card) ==16:
    try:
        first_number >=3 and first_number <= 5
    except:
        print("An error has occured. Please enter a valid credit card number.")
    else:
        if first_number == 3:
            print("The number you entered belongs to an American Express card.")
        elif first_number == 4:
            print("The number you entered belongs to a Visa card.")
        elif first_number == 5:
            print("The number you entered belongs to a MasterCard card.")
        else:
            print("An error has occured: unknown card.")      
else:
    print("An error has occured. Please enter a valid, 16-digit card number.")
  

    
