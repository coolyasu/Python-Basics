def greet():
    print("Hello, welcome to the app!")


greet()


def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name} : Welcome to the app!")


greet("Yash", "Raj")
# TypeError: greet() takes 2 positional arguments but 3 were given
greet("ash", "aj")

# 1 - Perform a task
# 2 - Return a value


def greet(name):
    return f"Hello {name}"


message = greet("Raj")
print(message)

# file = open("content.txt", "w")
# file.write(message)
# file.close() //copo


def greet():
    print("Hello, welcome to the app!")


print(greet())  # Hello, welcome to the app! \n None


def increment(number, by):
    return number + by


print(increment(10, by=2))  # 12




def increment(number, by=4):
    return number + by


print(increment(10))  # 14


def mult(*num):
    total = 1
    for n in num:
        print(n)
        total *= n
    return total

print(mult(1, 2, 3, 4, 5))  # 120