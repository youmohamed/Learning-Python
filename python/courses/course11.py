#oop (object oriented programming)

x = int("pp")*3
text = "hello"
logic = False
lst = ["sl3",2,3]
dicto = {}
tupl = ()
print(type(x))  #7awesna 3la type ta3 ga3 had les variables
print(type(text))
print(type(tupl))
print(type(logic))
print(type(lst))
print(type(dicto))

# def print_message():
#     print("hello world from function")

# print(type(print_message))  # class function

# nothing = None
# complx = 4J
# print(type(nothing))  # kifkif classes ta3 had 2 variables


'''evrything in python is object .
".classesكلش فالبايثون عندو هدف وكل هدف مصنف في صنف معين نعيطولهوم " '''
# class:   بطريقة خاصة (variables and functions) هي حاوية تحتوي على مجموعة من المتغيرات والدوال
# class :  blueprint مادة خام او 
# variables :   properties
# fuctions : methods


# x object from class int
x = 44
y = 22
z = 55
print(type(x))
print(type(y))
print(type(z))
'''object yetbedel mais class yeb9a ثابت '''


#i'll create my own class will be called myclass
class myclass:
    x = 0 #property or (variable out of the class)
    y = 33
    z = "sl3"

obj = myclass() # عملية استنساخ واش كاين فالكلاس
obj.x = 10    # na9edro nbdlo l9ima ta3 lobject kima nhabo
z = 56
print(obj.x)
print(type(obj))
print(type(obj.z)) # ida derna obj.z = 23432 yweli class int machi str  ya3ni nbdlo l9ima kima n7abo
print(type(z))