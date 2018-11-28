#use a loop so that the program will return to the beginning

while True:
    from random import *
    print("Welcome!")

    n = input("Enter a number of tickets: ")
    n = int(n)
    
    tickets_left = 80 - n
    if tickets_left < n:
        print("Sorry, there are not enough tickets left.")
    elif tickets_left >= n:
        count = n
        file = open("ticket.txt", "w")
        while count !=0:
            count = count - 1
            ticket_code = randint(10000, 99999)
            file.write(str(ticket_code) + "\n")
    file.close()


    # calculate the price of the tickets and round it to the nearest cent
    price = n*49.99
    price = round(price, 2)

    # print total cost and codes
    print("The total cost for", n, "tickets is $", price,  "and the codes are below:")
    file = open("ticket.txt", "r")
    print(file.read())

    #ask if the cashier wants to continue
    cont = input("Are there more customers? Enter 'yes' or 'no': ")
    if cont =="yes":
        continue
    elif cont == "no":
        break
    else:
        print("ERROR: Try again and please enter 'yes' or 'no'.")
