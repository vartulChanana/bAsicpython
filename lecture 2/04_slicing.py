#slicing is used to access , the vlaue from starting index , to ending index
str="HELLO WORLD"
print(str[1:4])
print(str[0:4])
print(str[0:]) #if we skip the last index , python itself takes it to the ending string
print(str[:len(str)]) #if we skip the first index , python itself takes to from the starting of the string
