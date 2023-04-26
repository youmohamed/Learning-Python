
'''import datetime
#print(dir(datetime))
dt = datetime.datetime.now()
#print(dt)
print(dt.strftime("%W"))'''

#gaaaaammmeeeee:

#the goal>> Guess the number from 1 to 20
# we have two indicators : rak nektha 7abat or rak nektha tela3
# we have 5 tries times availaible : number of guesses
# we must define a counter

from random import randint
number = randint(1,20)
player_name = input("wech sahbi , 3labali asmek yanis mais kawev ro7ek 3awed aktbo wela akteb wech t7ab ak ta3 bch nbano pro: \n")
number_of_guesses = 0
print("okey "+player_name+" ana salo kon ja robot khamemt fi number between 1 to 20 aya ylzem tel9ah, 3endek 5 mo7awlat sinon takhser")
while number_of_guesses < 5:
    try:   # gestion des erreur
        guess = int(input())
        number_of_guesses += 1 # number_of_guess = number_of_guess + 1
        if guess < number:
            print("rak nektha zid tela3")
        elif guess > number:
            print("rak nektha zid 7abat")
        elif guess == number:
            break
    except ValueError:
        print("dert 7sabi lkolch akteb numero between 1 to 20 reya7 matkhelat")  #hna tkhlas try  
if guess == number:
    print("rak rba7tni fi lmo7awla "+str(number_of_guesses)+" mat7asch ro7ek chikour byn jebtha zhar")
else:
    print("cbon khlaso drahmek fercha madernach ila kont rajel 3awed al3eb my secret number is "+str(number)) 

