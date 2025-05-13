# #Appending
# file_reader = open ("file.txt","a")     #file object - file_reader
# file_reader.write( "\n Appending the file object \n")
# file_reader.close()

# file_reader = open ("file.txt","r") 
# print(file_reader.read())

#Overwriting
file_reader = open ("file.txt","a")     #file object - file_reader
file_reader.write( "\n Rewriting the file object \n")
file_reader.close()

file_reader = open ("file.txt","r") 
print(file_reader.read())
