#Q Wap to print the element of the following list in a tuple with a loop :
#tup = (1,4,9,16,25,36,49,56,81,100)
# # tup=(1,4,9,16,25,36,49,56,81,100)
# for el in tup:
#     print(el)
#q search for x in the abve list 
tup=(1,4,9,16,25,36,49,56,81,100) #this process of searching is caleed linear search
x=int(input("enter a no"))
idx=0
for el in tup:
    if x==el:
        print("found at ",idx)
        idx+=1
        break
    else:
        print("trying")