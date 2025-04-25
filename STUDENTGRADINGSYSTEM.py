# names = []
# marks = []
# for i in range (1,4):
#     x = input(f"ENTER NAME {i} : ")
#     y = int(input(f"ENTER YOUR MARKS :"))
#     names.append(x)
#     marks.append(y)
# for x in range(3):
#     print(names[x]+":",marks[x])
import datetime                     #inbuilt Python function for dates
today = datetime.date.today()
k = "KEVIN"
print("***************************************\n")
title = "\tSTUDENT GRADING SYSTEM"  #A program to print the heading for the system -Student Grading System-
print(title)
print("..............Own It...................")
print(f"By {k}")
print(f"Date Today : {today}")
print("\n***************************************")
students = {}
subjects = ['Math', 'Kiswahili', 'English']

# Collecting the information for 5 students
for i in range(5):
    if i < 9:
        sid = (f"S00{i+1}")
    elif i < 99:
        sid = (f"S0{i+1}")
    else:            
        sid = (f"S{i+1}") 

    # sid = input(f"Enter Student ID {i+1}: ")    # sid - Student ID
    name = input("Enter Name: ")
    
    # Creating an empty dictionary for marks
    marks = {}
    
    # Collecting marks for each subject
    for subject in subjects:
        while True :
            mark = input(f"Enter {subject} marks for {name}-{sid}: ")
            if not mark.isdigit():
                print("Marks must be numbers!")
                continue
            mark = int(mark)   
            if mark < 0 or mark > 100 :    # OR - Either condition must be true
                print("Input must be within 0 and 100!")
                continue
            marks[subject] = mark
            break
    
    # Storing the student information in the dictionary
    students[sid] = {'name': name, 'marks': marks}

# To show the complete results for the students
for sid in students:                  #A loop that iterates through each student in the dictionary
    info = students[sid]
    name = info['name']               #Info represents the information that will be given by the user/student
    marks = info['marks']
    scores = []                       #A list to store the subjects and marks as given by the user

    # Collect marks into a list
    for subject in marks:
        scores.append(marks[subject]) # Takes the marks with the corresponding subject and adds it to the scores list

    # Calculate stats 
    # total = sum(scores)
    total = 0
    for score in scores:
        total += score
        print(total)
    average = total / len(scores)
    minimum = min(scores)       #
    maximum = max(scores)

    # Grading
    x = average
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
        
    # Print student data using f-strings
    print(f"\nStudent ID: {sid}")  #\n - represents a new line
    print(f"Name: {name}")
    for subject in marks:          #Prints the subject and the corresponding mark
        print(f"{subject}: {marks[subject]}")
    print(f"Average Marks: {average : .2f}") #.2f - Displays the average to two decimal points
    print(f"Minimum Marks: {minimum}")
    print(f"Maximum Marks: {maximum}")
    print(f"Grade: {Grade}")
    print(f"Feedback: {feedback}")
