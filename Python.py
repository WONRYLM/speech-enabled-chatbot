print("I'm learning Python from BroCode")
print("It's really interesting")
 
#VARIABLES#  #String,Integer,Float,Boolean
#Variables are used to store values in a program

#Strings
first_name = "Kevin"
food = "Chapati"
email = "johndoe@fakeemail.com"

print(first_name)
#f string   f means /format/
print(f"Hi {first_name}")
print(f"I love my mom's {food}")
print(f"My email is {email}")

#Integer
age =18
quantity = 7
num_of_students = 28
print(age)
print(f"You are {age} years old")
print(f"You are buying {quantity} books")
print(f"We are {num_of_students} students in the class")

#float /floating Points/
price = 10.00
distance = 7.8
print(f"The price is {price}")
print(f"I walked {distance} kilometers")

#Booleans /True or False/ Binary
is_adult = True
is_fruit = False
print(f"Are you an adult : {is_adult}")
print(f"A tomato is a fruit : {is_fruit}")
is_online = False
if is_online:               #if else stmt in a Boolean
    print("Holly is online")
else:
    print("Holly is offline")

#Typecasting /Converting a variable from one datatype to another str,int,float,bool/
name = "Kevin"
age = 18 
num = 5
score = 90
is_student = True

print(type(name))
print(type(age))

age =int(age)
print(age)
num = float(num)
print(num)

score = str(score)
print(score)

name = bool(name)
print(name)

#input()   /Prompts user to enter data & returns data entered as a string/
# input()
# name = input
# input("What's your name?")
# print(f"Hello {name}!")

# age = input("How old are you?")
# age = int(age)
# age = age + 1 #Can only concatenate strings.Convert to a string.
# print(f"Hello {name}!")
# print(f"You are {age} years old")
# #....condensing
# age = int(input("How old are you?"))
 
#EXERCISES.
# Area of a RECTANGLE
# Length = float(input("Please enter the length : ")) #float/int whichever
# Width = float(input("Please enter the width : "))
# Area = Length * Width
# print(f"The area of the rectangle is {Area} square units")

# Area of a CIRCLE
Radius = float(input("Please enter the radius : "))
Area = 3.142 * (Radius ** 2)
print(f"The area of the circle is {Area} square units")

#Numpy
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr[0])     # 10
print(arr[-1])    # 40
