#elif uses more than 2 descriptions

#below is an example of taking a numerical grade and assigning a letter grade.

# A = 90-100, B = 80-89, C = 70-79, D = 60-69, F = < 60

number_grade = int(input("What is your letter grade? "))
letter_grade = ""

if number_grade >= 90:
    letter_grade = "A"

#short circuting = when an if or elif condition is met, it skips the rest of the statements below

elif number_grade >= 80:
    letter_grade = "B"

elif number_grade >= 70:
    letter_grade = "C"

elif number_grade >= 60:
    letter_grade = "D"

else:
    letter_grade = "F"

print("Your letter grade is", letter_grade)