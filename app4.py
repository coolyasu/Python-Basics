number = 10 
while number > 0:
    print(number)
    number -= 1

command = "" 
# while command != "quit" and command != "QUIT":
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

while True:
    cmd = input(">")
    if(cmd.lower() == "quit"):
        break  


print("*"*100)

count = 0
for num in range(1,10):
    if(num%2 == 0 ):
        count += 1
        print(num)
else:
    print(f"Count of even numbers: {count}")