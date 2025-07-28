import json                 #Importing json

data = {                    #Dictionary to contain all the data - Stores key value pairs
    "subject": "Mathematics",
    "teacher": "Mr. Kimani",
    "students": ["Ali", "Becky", "Chris"]       # List of students
}

with open ('class_info.json', 'w') as school:   # Opening the json file in write mode
    json.dump(data,school,indent = 4)           # Writes into the file 

with open('class_info.json', 'r') as school:    # Opening the json file in read mode 
    lesson = json.load(school)                  # Reads the entire content of json file

# Print the entire data
print("Class Information:", lesson)

# Access specific parts of the data
print("Subject:", lesson ['subject'])             # Accessing the subject
print("Teacher:", lesson ['teacher'])             # Accessing the teacher
print("Students:",",".join(lesson ['students']))  # Accessing the students
