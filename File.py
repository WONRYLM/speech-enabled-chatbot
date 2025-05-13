file_reader = open ("file.txt","r")

# print(file_reader.read())       #f.read - opening the file to be read
    #print(file_reader.read(5#number of characters to be read))

# print(file_reader.read(5)) 
#print(file_reader.readline()) #reading a line at a time

    #Reading a file line by line
first_line = file_reader.readline()
second_line = file_reader.readline()
print(first_line)
print(second_line)
file_reader.close()

    #Use a for loop to access the first 2 lines in the file 
#for variable in file object
    #print variable
# for line in file_reader:
    # print (line) #reading a line at a time

# for x in range (2):           #Optimize it !!!
#     z = file_reader.readline
#     print(z)


# with open ("file.txt","r") as file :
#     for _ in range (2):
#         line = file.readline()
#         if not line :
#             break
#         print(line,end = "") #reading multiple lines at a time