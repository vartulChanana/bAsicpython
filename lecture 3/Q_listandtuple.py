#Q take input of three movie name and store them in a list
# a=input("ENTER MOVIE 1")
# b=input("Enter movie 2")
# c=input("enter movie3")
# list=[a,b,c]
# print(list)

#Q wap to check if the list has palindrome of elements. hint<use copy()method>
# list=[1,2,1]

# copy_list= list.copy()
# copy_list.reverse

# if(list==copy_list):
#     print("yes pallindrome is their",list)
# else:
#     print("NO NOT THERE")

#Q wap to find how many students got an A in the following tuple , marks= (A,B,A,A,A,F,C,B,D,A,)
marks= ('A','B','A','A','A','F','C','B','D','A')
print(marks.count("A"))

#Q Store the above values in a list and then sort them
marks = ['A','B','A','A','A','F','C','B','D','A']
marks.sort()
print(marks)