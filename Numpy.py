import numpy as np

arr = np.array([10, 20, 30, 40])                   # arr - array name
print("Accessing the first element : ", arr[0])    # 10 #Accessing the first element
print("Accessing the last element : ", arr[-1])    # 40

    #2D Arrays
#mat = np.array([[1, 2], [3, 4]])
mat = np.array([[1, 2, 3], [4, 5, 6] ,[4, 5, 6]])   #3 by 3 arrays
# [1, 2, 3],                                         
# [4, 5, 6]
# [4, 5, 6]
print("Obtaining the first element in the array :", mat[0, 0])
print("Obtaining the second element in the array :",mat[0, 1])
print("Obtaining the third element in the array :",mat[0, 2])

    #Array Slicing
a = np.array([10, 20, 30, 40, 50])
print("Accessing the first 3 elements in my array :", a[0:3])     # [10 20 30]

#2D Arrays
b = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
print("All Arrays :")
print(b)     # [[1 2 3],[4 5 6]]
# [1,2,3]
# [4,5,6]
# [7,8,9]
#print("Accessing all elements in columns 1 and 2 :")
#print(b[:, 1:])   # Get all rows, columns 1 and 2
print("Accessing the 2 and 3 row and 1 and 2 column :")
print(b[1:3, :3])

    #Statistical Functions
    