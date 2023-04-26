#loop for

'''days = ["samedi","dimanche","lundi","mardi"]

#for element in sequense
for day in days :
    print(day)'''

#2example:

'''sentence = "mouloudia daymen 9awya!"
for letter in sentence :
    print(letter)'''

#range(1,6,1) 12345 ( mnin tbda , mnin takhlas -1 , direction +-)

'''for n in range(1,-6,-1) :
    print(n)'''

#loop while 
#تعريف قيمة لمتغير ما 

'''i = 1
while i <= 10 :
    print(i)
    i += 1  # i = i + 1'''

while True :
    try :
        num = int(input("give ur number: \n"))
        break
    except ValueError :
        print("input an integer only...")
print("number :",num)
