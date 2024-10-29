#nested if tutorial, avoid if possible


ticket_price = 10.00
discount = 0.10

age = int(input("How old are you? "))
rating = "G"
#when comparing strings, capitalization DOES matter.
if (rating == "G"):
    if(age <= 12):
        ticket_price = ticket_price - (ticket_price * discount)
        print("Child discount. Your ticket price is", ticket_price)
    if(age >= 65):
        ticket_price = ticket_price - (ticket_price * discount)
        print("Senior Citizen discount. Your ticket price is", ticket_price)
    else:
        print("Ticket price is", ticket_price)
else:
    print("Rating is not G, discount is not allowed. Ticket price is", ticket_price)