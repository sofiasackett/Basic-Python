#This program will calculate a restaurant tab with a gift certificate, with a user-entered tax rate

#program greeting
print("This program will calculate a restaurant tab for a couple with a gift certificate %\n")

#get tax rate
tax = input("Enter tax rate (as a decimal) here: ")
tax = float(tax)
            
#get amount of gift certificate
amt_certificate = float(input("Enter amount of the gift certificate: "))
            
#cost of ordered items
print("Enter ordered items for person1")

appetizer_per1 = float(input("Appetizer: "))
entree_per1 = float(input("Entree: "))
drinks_per1 = float(input("Drinks: "))
dessert_per1 = float(input("Dessert: "))

print("\nEnter ordered items for person 2")

appetizer_per2 = float(input("Appetizer: "))
entree_per2 = float(input("Entree: "))
drinks_per2 = float(input("Drinks: "))
dessert_per2 = float(input("Dessert: "))

#total items
amt_person1 = appetizer_per1 + entree_per1 + drinks_per1 + dessert_per1
amt_person2 = appetizer_per2 + entree_per2 + drinks_per2 + dessert_per2

#compute tab with tax
items_cost = amt_person1 + amt_person2
tab = items_cost + items_cost * tax

#display amount owe
print("\nOrdered items: $", format(items_cost, ".2f"))
print("Restaurant tax: $", format(items_cost * tax, ".2f"))
print("Tab: $", format(tab - amt_certificate, ".2f"))
print("(negative amount indicates unused amount of gift certificate)")
