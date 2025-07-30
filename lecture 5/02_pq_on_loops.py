# # #PRINT NUMBER FROM 0 TO 100
# # i = 1
# # while i<=100 :
# #     print(i)
# #     i += 1
# # print("Loop ended")

# # #print number from 100 to 0

# # i=100
# # while i>=1:
# #     print(i)
# #     i-=1
# # print("lOOP ENDED")

# #Print a multiplication table of number n

# n= int(input("ENTER A NUMBER"))
# count = 1
# while count <= 10 :
#     print(n*count)
#     count+=1
# print("Table Printed")

#Print sqaure of first 10 number :
# i= 1
# while i<=10:
#     print(i**2)
#     i += 1
# print("SQAURE READY")

#q Search for a number x in the list created above :

tup = (1,4,9,16,25,36,49,64,81,100)
x=36  
i=0
while i < len(tup) :
    if (tup[i]==x):
        print("yes found",i)
        break
    else:
        print("Searching")
    i+=1
    
   
   