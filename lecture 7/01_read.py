f= open("E:\pythonbasics\lecture 7\demo.txt", "r")
data = f.read()
print(data)
f.close()

#we have to create a variable giving it command to open the file (location , reading mode)
#then we have to create another variable so that it gets or reads the data , then make it print
#a good programmer closes the file 

#readline method is used just to read one line at a time
#read is used to read the entrire elements in the file

