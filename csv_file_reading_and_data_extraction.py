import csv

# Reading lines from the CSV file
def read_file():
    data = []                                   # This will store all rows from the CSV in a list
    with open("2score.csv", "r") as file:
        reader = csv.DictReader(file)           # Reads the rows 
        for row in reader:                      # Loops through each row in the CSV file
            print(row["name"], row["score"])    # Prints each name and score      
            data.append(row)                    # Adds all the rows in the .csv file to the list          
    return data                                 # Return the list of rows as dictionaries

# Dictionary
def score(data):
    scores = {}                     # Empty dictionary to score the key value pairs - name and score
    for row in data:                # Loop through each row to access data
        name = row["name"]          # Get the name from the row
        score = int(row["score"])   # Convert score to an integer
        #if loop to handle duplicates - Duplicate names
        if name in scores :          
            scores[name] = max(scores[name],score) # Gives the name with the highest score
        else:
            scores[name] = score
    return scores                   # Returns to the dictionary

# Sorting 
def show_top_3(scores):
    if not scores:                  # If empty dictionary // for error handling
        print("Your File is Empty")
        return 
     #sorts the dictionary by the score in descending order
     #x - gives the name
     #x[1] - Gives the score
     #key=lambda x: x[1] - Sorts based on score
     #reverse=True - Sorts from highest to lowest
    print("Scores Dictionary:", scores)                 # Shows all the data in the dictionary
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_scores[:3]
    print("Top 3 Scorers:")
    for name, score in top_3:
        print(name, "-", score)

# Main program
lines = read_file()       # Reads data from the CSV file
scores = score(lines)     # Converts list of rows into a dictionary
show_top_3(scores)        # Displays the top 3 scorers
