# # #WRITE A FN TO PRINT THE LENGTH OF A LIST
# # def calc_list(lit):
# #     print(len(lit))
# # calc_list(["ELLO","HOAREYOU","GOA","MUMBAI"]) # we can also create a list first but here what we did was"[]" we created a list inside the function 
# # #we can also create a separate list as shown below
# # cities=["GOA","MUMBAI","PUNE","SRE"]
# # calc_list(cities)

# # #wap to print the elements of the list in a single line
# # def prints_name(list):
# #     print(list, end="")
# # cities=("GOA","MUMBAI","PUNE","SRE")
# # prints_name(cities)

# #wap to print factorial of n

# def calc_factorial(n):
#     fact = 1 
#     for i in range(1, n+1):
#         fact *=i 
#     print("fact is ", fact)

# calc_factorial(10)

# def calc_inr(a,b=80):
#     mult = a*b
#     print("your inr is",mult)
# calc_inr(10)

#q : wap to take input from the user and then tell if its even or odd:

def num_check(n):
    if n%2 == 0 :
        print("even")
    else:
        print("odd")
num_check(n=int(input("ENTER A NO")))