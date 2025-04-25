# sum = 0
# score = [13,12,67,58]
# for score in score:
#     sum += score
# print(sum)

# Program to generate student ids
for  i in range (1000):
    if i < 9:
        sid = (f"S00{i+1}")
    elif i < 99:
        sid = (f"S0{i+1}")
    else:            
        sid = (f"S{i+1}")
    print (sid)    
