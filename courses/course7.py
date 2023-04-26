#admin , editor, reader 
'''ad001 -> admin
ed001 -> editor
rd001 -> reader'''
#dictionary:
'''data = {}
print(type(data))'''
#key : value
# exemples:
#1
'''data = {
    1 : "Admin",
    2 : "Editor",
    3 : "Reader"
}
print(data)'''
#2
'''data ={
    "id" : 1,
    "name" : "sl3",
    "phone" : 2345677
}
print(data["name"])
for key in data :
    print (key)
    print(data[key])'''
#3
data ={
    1 : "Admin",
    2 : "Editor",
    3 : "Reader"
}
#CRUD (create, read, update, delete,)
data[2] = "subscribe" #update
data[4] = "author" #create 
del data[3] #delete
'''print(data)'''
'''print(2 in data)''' # true or false kyn wela mkch 
'''print(len(data))''' # len : how much items i have
'''data.clear() 
print("data containe: ", data)'''  #clear fonction tfaragh lvariable matsuprimihch kima (del) dir : del data , tefham
'''data2 = data.copy() 
print (data2)'''   #copy fonction
'''keys = data.keys()
print(keys)'''   #keys fonction