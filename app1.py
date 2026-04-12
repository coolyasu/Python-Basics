x = input("Enter No: ")
# print(type(x))
y = int(x) + 1
print(f"x : {x} , y : {y}")

# int(x)
# float(x)
# str(x)
# bool(x)

# Falsy
# ""
# 0
# None
# False


bool("")  # False       
bool(0)  # False
bool(0.0)  # False
bool([])  # False
bool({})  # False
bool(None)  # False
bool(False)  # False
bool(set())  # False

bool(True)  # True
bool(1)  # True
bool([1, 2, 3])  # True
bool(0.1)  # True
bool({"name": "Yash"})  # True
bool({1, 2, 3})  # True 
bool("False")  # True
