# if else statement with elif
student_name = input("Please enter your name: ")
student_id = input("Please enter your student ID: ")
# if student_id == "":
#     print("Please provide a student ID")
# else:
#     marks = input("Please enter your marks: ")
# x = int(marks)
Grade = " "
while True:
    x = int(input("Please enter your marks: "))
    

    
    if x >= 0 and x <= 100:
        print("Input correct")
        if x >= 95:
            Grade = "A+"
            feedback = "Excellent"
            Grade = "A+"
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
