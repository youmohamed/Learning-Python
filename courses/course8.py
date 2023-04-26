#function ; methode
#built in fun ; user defined fun
'''def greeting (name):
    print("Hello "+name+" welcome to our website!!")
greeting("sl3")'''
'''def get_sum(a , b):
    return a+b # return لارجاع قيمة معينة في الداكرة

x = get_sum(3,5) 
print(x)'''

'''print (get_sum.__doc__)''' #doc:  '''تافيشي ليكومنتار لي داخل الفانكشون بصح اللي فيها

#Default argument
'''def print_language(language = "English") : # hadi tafichi wech rak hab par default
    print ("your language is ", language)
print_language("Arabic")
print_language()'''

'''def print_info(name,salary):
    print("Name : ",name)
    print("salary : ",salary)
print_info (20000,"sl3")
print_info (salary=20000,name="sl3")''' # bach mayakhrebch tartib

#function with no limit of args 

'''def print_args(*args):
    for e in args:
        print(e)
#print_args(1,2,3,4,5,6)
#print_args(7,8,9)
print_args()'''

'''def print_average(*values):
    print(sum(values)/len(values))
print_average(12,10,5,6,8)
print_average(18,16,19,16,14,15)'''


def print_user_average(user,*notes):
    avg = sum(notes)/len(notes)
    print("the average of ",user," is ",avg)
    
print_user_average("mounib mohamed",16.17,16.17,16.17,14.08,19.42,17.17,17.42,17.42,13.25,13.25,13.25,13.58,17.00,19.00)