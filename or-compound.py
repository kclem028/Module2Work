#nested if tutorial, avoid if possible


ticket_price = 10.00
discount = 0.10

age = int(input("How old are you? "))
rating = "G"
#when comparing strings, capitalization DOES matter.
if age <= 12 or age >= 65:
    print("Your discount has been applied, your ticket price is ", ticket_price - ticket_price * discount)