name = "KEVIN KIBET"
capitalized_name = name.capitalize()
print(capitalized_name)

# centering a string
string = "GOMYCODE ONLINE"
x = string.center(30)
print("centered string:", x)

# string count
string = "Python is awesome, isn,t it?"
substring = "P"
count = string.count(substring, 0, 10)
print("The count is:", count)

# expanding tabs in a string
string = "xyz\t12345\tabcd\t97"
result = string.expandtabs()
print(result)

# string formatting
print("Hello {0}, your balance is {1:9.3f} as of {2} at {3}".format(
    "Kevin", 123.4567, "today 2025/4/8", "7:15"))
b = ("Today is {0}, {3} {2} {1}".format("Tuesday", "April", 8, 2025))
print(b)

age = 18
location = "Nairobi"
print("Hello, my name is {name}, I am {age} years old and I stay in {location}".format(
    name=name, age=age, location=location))

# string formatting with f-strings
is_name = "Kevin Kibet"
print(f"Hello {is_name}, welcome to GOMYCODE")

name = "Kevin Kibet"
age = 18
print(f"Hello, my name is {name}, I am {age} years old.")

# boolean values
is_hungry = True
print("Is hungry =", is_hungry, (type(is_hungry)))
print("the variable type of is_hungry is", type(
    is_hungry), "and it's value is", is_hungry)
print("Kevin is hungry =", is_hungry)

c = 5
d = 10
e = c == d
print("c == d =", c == d)
print("c != d =", c != d)
print("c > d =", c > d)
print("c < d =", c < d)
print(e)

# type conversion
# converting 5.7 float to an int
a = 5.7
b = int(a)
print("The value of b is", b, "and the type is", type(b),
      " The value of a is", a, "and the type is", type(a))
print(b)
# converting 5.7 float to a string
a = 5.7
b = str(a)
print("The value of b is", b, "and the type is", type(b),
      " The value of a is", a, "and the type is", type(a))
print(b)
# converting 5.7 float to a boolean
a = 5.7
b = bool(a)
print("The value of b is", b, "and the type is", type(b),
      " The value of a is", a, "and the type is", type(a))
print(b)

# converting 5.7 float to a list
a = 5.7
a_str = str(a)  # convert float to string
b_list = list(a_str)  # convert string to list
print(b_list)

# converting 5.7 float to a tuple
a = 5.7
a_str = str(a)  # convert float to string
a_tuple = tuple(a_str)  # convert string to tuple
print(a_tuple)

# converting 5.7 float to a set
a = 5.7
a_str = str(a)  # convert float to string
a_set = set(a_str)  # convert string to set
print(a_set)

# converting 5.7 float to a dictionary
a = 5.7
a_dict = {'float_value': str(a)}  # convert float to dictionary
print(a_dict)

# if else statement
number = -10
if number < 0:
    print(f"The number {number} is negative")
else:
    number = 10
if number > 0:
    print("The number", number, "is positive")

# if else statement with elif
a >= 90
b >= 80
c < 70
x = marks = 33
Grade = " "
if x >= 95:
    Grade = "A+"
    feedback = "Excellent"
elif x >= 90:
    Grade = "A"
    feedback = "Very Good"
elif 80 <= x < 90:
    Grade = "B"
    feedback = "Good"
elif x >= 70:
    Grade = "C"
    feedback = "Average"
elif 50 <= x < 70:
    Grade = "D"
    feedback = "Below Average"
elif 49 <= x < 30:
    Grade = "E"
    feedback = "Very Poor"
else:
    Grade = "F"
    feedback = "Fail"
print(f"Your mark is {x} and your grade is {Grade}.{feedback}")

# loops
for i in range(10):  # Python counts its indexes from 0
    print(i + 1)
    print("The value of i is", i + 1)
for i in range(0, 21):  # Printing even numbers from 1 t0 20
    if i % 2 == 0:
        print("This is an even number", i)
for i in range(1, 51):
    if i % 3 == 0:
        print("Fizz", i)
    if i % 5 == 0:
        print("Buzz", i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)

# While loop
    # Define variables
count = 0
while count < 5:
    print(count)
    count += 1
    # While loop with else statement
while True:
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("You are an adult")
        break
    else:
        print("You are a minor")
