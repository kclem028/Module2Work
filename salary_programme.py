#Create a program that determines if yuo can get a loan based on a salary adn years worked.
#If you have worked 2 years or more and your salary is greater than 30,000 a year, then you qualify for a loan.

#salary
salary = float(input("Give me your salary for the year "))
years_on_the_job = int(input("How many years have you worked at your place of employment? " ))


if salary >= 30000 and years_on_the_job >= 2:
    print("You qualify for a loan.")

#we want to know why they dont qualify

elif salary >= 30000 and years_on_the_job < 2:
    print("You have not worked long enough to qualify for a loan. Salary is acceptable")

#worked long enough, but not enough salary

elif salary < 30000 and years_on_the_job >= 2:
    print("Your salary is not high enought to qualify. You have worked long enough at your job.")

else:
    print("You don't have a high enough salary, and you haven't worked long enough at your job.")