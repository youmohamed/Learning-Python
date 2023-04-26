#operators العوامل 

#العوامل الحسابية
'''x = 3 #assignment
x % y  # اخر باقي القسمة 
x % 2 = 0 #عدد زوجي
5 / 2 = 2.5
5 // 2 = 2 #عدد بدون فاصلة'''

#comparison operator عوامل المقارنة
'''a == b
a != b لا تساوي 
a >= b
a <= b'''
# exercise 
'''a = b = 5
c = 10
if a > b :
    print("a>=b")
if a != c :
    print("a!=c")'''
#logical operator عوامل منطقية
# and , or , not : true, false
#exercice
'''username = "user1"
pwd = "1234"
if (username == "user" and pwd == "123"):
    print("welcome sir!!!")
else :
    print("login failed!!!")'''

'''a += b #a = a + b
    a -= b #a = a - b
    a /= b #a = a / b
    a *= b #a = a * b'''

#conditions : if ; elif ; else ,
# exercice:
'''number = int(input("give me a number :")) 

if number == 1:
    print("one")
elif number == 2:
    print("two")
elif number == 3:
    print("three")
elif number >= 4:
    print("four or greater")        
else:
    print("negative number") '''

#exercice 2

s = input("Gender : \n")
age = int(input("Age : \n"))
if s == "male":
    print("Gender:male")
    if age <= 21:
        print("he is a young boy")
    else :
        print("he is adult")    
elif s == "female":
    print("Gender:female")
    if age <= 21:
        print("she is a young girl")           
    else :
        print("she is adult")
else :
    print("Erreur typing !!!!") 
           