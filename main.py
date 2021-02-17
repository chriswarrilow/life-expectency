age = input("What is your current age? ")

ageInt = int(age)
yearsRemaining = 90 - ageInt
daysRemaining = yearsRemaining * 365
weeksRemaning = yearsRemaining * 52
monthsRemaining = yearsRemaining * 12

print(f"You have {daysRemaining} days remaining or {monthsRemaining} months remaining or {yearsRemaining} years remaining until you are 90 years old.")