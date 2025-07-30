# CREATE A FILE practice.txt, and add some data in it
with open("practice.txt","x") as f:
    data = f.write("HELLO MY NAME IS VARTUL")
    print(data) 