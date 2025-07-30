with open ("E:\pythonbasics\lecture 7\demo.txt","r") as f:
    data=f.read()
    print(data)

#with syntax , it is basically a better way to do I/O operations on a file 
#we dont have to close() , as in with syntax it automatically closes