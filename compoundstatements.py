#compound statements

# and = both things must be true
# or = only ONE thing must be true
# not = flips the boolean value of the result to it's opposite (false becomes true, true becomes false)

age = 16
registered = "y"
##
#if (age >= 18):
#    if (registered == "y"):
#        print("You can vote.")

##

if age >=18 and registered == "y":
    print("You can vote")

elif age >=18 and registered == "n":
    print("You are old enough, but are not registered to vote. You cannot vote")

elif age <=17 and registered == "y":
    print("You are reigstered to vote, but you are too young. You cannot vote.")

else:
    print("You are too young and you are not registered to vote. You cannot vote.")