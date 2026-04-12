temperature = 15
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")
print("Enjoy your day")


age = 17
if age >= 18:
    message = "Eligible to vote"
else:
    message = "Not eligible to vote"
print(message)


message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(message)

print("*"*100)


# and or not
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print("*"*100)

student = True

if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


if (high_income or good_credit) and not student:
    print("Eligible for loan")
# Logical operators are short circuit

print("*"*100)

age = 16

# Chaining comparison operators
if 18 <= age < 65:
    # if age >= 18 and age < 65:
    print("Eligible for work")
