numbers = [10, 20, 30]

print(numbers)  # [10, 20, 30]

numbers.append(40)   # add
print(numbers) 
numbers.remove(20)   # remove
print(numbers) 

for num in numbers:
    if(num>10):
        print(num)  # 30, 40

squares = [x*x for x in numbers if x >20] # list comprehension
print(squares)  # [100, 400, 900, 1600]


user = {
    "name": "Yash",
    "age": 25
}

print(user["name"])

user["age"] = 26

print(user)  # {'name': 'Yash', 'age': 26}

for key,value in user.items():
    print(f"{key}: {value}")

users = {
    "user1": {"name": "Yash", "age": 25},
    "user2": {"name": "John", "age": 30}
}

print(users.get("user1"))
print(users["user2"]["name"])


def get_user_info(users, username):
    return users.get(username, "User not found")

users = {
    "yash": {"age": 25},
    "john": {"age": 30}
}

print(get_user_info(users, "john"))