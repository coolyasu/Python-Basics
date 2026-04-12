for number in range(10):
    print(number, number + 1, (number+1) * "*")  # 0 - 9


for number in range(1, 10):
    print(number, (number) * "*")


for number in range(1, 10, 2):
    print(number, (number) * "*")


print("*"*100)

success = True
for number in range(1, 10):
    print("Attempt")
    if success:
        print("Successful")
        break
else:
    print("Attempted 10 times and failed")


for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

print(type(range(5)))  # <class 'range'>
print(type(4))  # <class 'int'>

#Iterable
for x in range(5):
    print(x)

for x in "Yash Raj":
    print(x)

for x in ["sdf",1, 2, 3, 4, 5]:
    print(x)