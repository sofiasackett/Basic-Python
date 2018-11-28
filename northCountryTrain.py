# This program will sell tickets for the North Country Train
while True:
    import random
    
    # Greet user
    print("\nHello, welcome back to the North Country Train Ticket Counter!")

    # Ask for number of tickets the customer wants
    numTickets = int(input("How many tickets would the customer like to purchase? "))

    # Checks for remaining seats
    remaining = 80 - numTickets
    if remaining < numTickets:
        print("There are not enough seats available for this customer.")
        
    elif remaining >= numTickets:
        count = 0
        cost = round(numTickets * 49.99, 2)
        output = open("ticket.txt", "w")

        while count < numTickets:
            code = random.randint(10000, 99999)
            output.write(str(code) + "\n")
            count = count + 1
    output.close()

    # Print total price of the ticket(s) and code(s) for each ticket
    output = open("ticket.txt", "r")
    print("This customer owes $", cost, "for", numTickets, "tickets. ")
    print("The following are the code(s) for each ticket:")
    print(output.read())
    
    # Ask if user would like to continue selling or quit
    print("Would you like to continue selling tickets?")
    question = input("Please enter 'yes' or 'no': ")
    question = question.lower()
    if question == "y":
        continue
    elif question == "n" or remaining == 0:
        print("Goodbye!")
        break
