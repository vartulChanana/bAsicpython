# #Q Wap to check if a number is odd or even
# num=int(input("Enter a number"))
# if(num%2 == 0):
#     print("IT IS EVEN")
# else:
#     print("It is odd")

#Q wap to find greatest of 3 number , take input from user
# num1=int(input("Enter a number"))
# num2=int(input("Enter second number"))
# num3=int(input("Enter third number"))
# if(num1>num2 and num1>num3):
#     print("BIGGER NUMBER IS ", num1)
# elif(num2>num1 and num2>num3):
#     print("BIGGER NUMBER IS", num2)
# elif(num3>num1 and num3>num2):
#     print("BIGGER NUMBER IS", num3)

#Q wap to check if the number is divisble by 7 or not
# num=int(input("ENTER A NUMBER"))
# if(num%7 == 0):
#     print("IT IS DIVISBLE")
# else:
#     print("NO NOT DIVISIBLE")

#Q wap to find largest out of 4 number
num1=int(input("Enter a number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
num4=int(input("Enter fourth number"))
if(num1>num2 and num1>num3 and num1>num4):
    print("BIGGER NUMBER IS ", num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("BIGGER NUMBER IS", num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("BIGGER NUMBER IS", num3)
else:
    print("BIGGEST IS ",num4)