#q store folllowing words in a dictionary 
#"table" :"something something","something something"
#"cat" :"a small amimal"
# dict ={}
# dict.update({"table ":("something something ",  "wow wow"), "cat":"a small animal"})
# print(dict)

#as you know one key cannot have multiple values , so what we did was , we added two sent as a tupple which counted as one value

#Q  , you are given a list of subjects , suppose one subject takes one class , so how many classes will all the subject take
# sets= {
#     "python","java","C++","python","javascript","C++"
# }
# print(len(sets))

#Q WAP TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN DICTIONARY 
#Start with an empty dictionary and fill values one by one.

dict={
    input("enter 1subject"):input("enter 1marks"),
    input("enter 2subject"):input("enter 2marks"),
    input("enter 3subject"):input("enter 3marks"),
}
print(dict)