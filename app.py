import math
print("Hello")
print("*"*10)
print(10+29)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(10+"29")
# print("yash"+10)
print(2+3)
x = 10

students_count = 100
rating = 4.9
is_published = True
course_name = "Python for Beginners"
print(rating)
print(is_published)
print(course_name)
print(students_count)


message = """
Hello everyone,
Welcome to the Python for Beginners course.
Best regards,
"""
print(message)

print(len(message))

print(course_name[0])
print(course_name[1])
print(course_name[0:4])
print(course_name[0:])  # from 0 to end
print(course_name[:4])  # from start to 4
print(course_name[:])  # from start to end
print(course_name[-1])  # last character
print(course_name[-2])  # second last character
print(course_name[-4:])  # last 4 characters
print(course_name[:-4])  # from start to last 4 characters

course = "\'Python\n \"for\"\t \t \\Beginners"
print(course)

first = "Yash"
last = "Raj"
# full = first + " " + last
full = f"{first} {last}"
msg = f"{len(course)} characters in course name {3+7}"
print(full)
print(msg)


print("*"*100)

name = "yash raj"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

word = "     python  "
print(word)
print(word.strip())
print(word.lstrip())
print(word.rstrip())
print(word.find("p")) # not found, returns -1 if not found
print(word.replace("p","c"))
print("pz" in word) # returns True if found, else False
print("pysa" not in word) # returns True if not found, else False

print("*"*100)

x = 11
x = 1.1
x = 1+2j # complex number a + bj
print(x)
print(x.real) # real part
print(x.imag) # imaginary part
print(x.conjugate()) # conjugate of complex number


print(4+3)
print(34-2)
print(3*4)
print(10/3) # float division
print(10//3) # floor division
print(10%3) # modulus operator
print(2**3) # exponentiation operator

x = x + 2 # x = x + 2
x += 2 # x = x + 2
x -= 2 # x = x - 2

print("*"*100)
print(round(2.6))
print(abs(-2.9))
print(math.ceil(2.01))
print(math.floor(2.6))  
print(math.sqrt(16))
print(math.pow(2,3)) # 2 raised to the power of 3
print(math.pi)
print(math.factorial(5)) # 5! = 5*4*3*2*1