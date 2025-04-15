# Please give your number
# number = input("Please give your number")
# # x = int(number)

# while True:
#     x = float(input("Please give your number: "))
#     if x <= 7:
#         print("Input correct")
#         break
#     else:
#         print("Input incorrect")

# While loop
# Define variables
# count = 0
# while count < 5:
#     print(count)
#     count += 1


# student_name = input("Please enter your name: ")
# student_id = input("Please enter your student ID: ")

# Grade = ""
# feedback = ""

# while True:
#     x_input = input("Please enter your marks (0–100): ")

#     if not x_input.isdigit():
#         print("❌ Input must be a number.")
#         continue

#     x = int(x_input)

#     if x < 0 or x > 100:
#         print("❌ Input incorrect. Marks should be between 0 and 100.")
#         continue
#     else:
#         print("✅ Input correct")

#         # Grading logic
#         if x >= 95:
#             Grade = "A+"
#             feedback = "Excellent 🌟"
#         elif x >= 90:
#             Grade = "A"
#             feedback = "Very Good 👍"
#         elif x >= 80:
#             Grade = "B"
#             feedback = "Good 🙂"
#         elif x >= 70:
#             Grade = "C"
#             feedback = "Average 😐"
#         elif x >= 50:
#             Grade = "D"
#             feedback = "Below Average 😕"
#         elif x >= 30:
#             Grade = "E"
#             feedback = "Very Poor 😟"
#         else:
#             Grade = "F"
#             feedback = "Fail 💔"

#         print(
#             f"\nHello {student_name}, your score is {x} and your grade is {Grade}. {feedback}")
#         break

student_name = input("Please enter your name: ")
student_id = input("Please enter your student ID: ")
Grade = " "
while True:
    x = input("Please enter your marks: ")

    if not x.isdigit():
        print("Input must be a number")
        continue

    x = int(x)

    if x >= 0 and x <= 100:
        print("Input correct")
        if x >= 95:
            Grade = "A+"
            feedback = "Excellent"
        elif x >= 90:
            Grade = "A"
            feedback = "Very Good"
        elif x >= 80:
            Grade = "B"
            feedback = "Good"
        elif x >= 70:
            Grade = "C"
            feedback = "Average"
        elif x >= 50:
            Grade = "D"
            feedback = "Below Average"
        elif x >= 30:
            Grade = "E"
            feedback = "Very Poor"
        else:
            Grade = "F"
            feedback = "Fail"
        print(
            f"Hello {student_name} your score is {x} and your grade is {Grade}.{feedback}")
        break
    else:
        print("Input incorrect")
