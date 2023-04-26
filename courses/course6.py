print("please think a number between 0 and 100")
low = 0
high = 100
meduim = (low + high) // 2 #لتجنب الفاصلة//
state = True
while state:
    print("is your secret number?" + str(meduim)) #concatenate المجاوروة
    guess = input("Enter h to indicate the guess is too high,Enter l to indicate the guess is too low,Enter c to indicate the guess is correctly!!! \n")
    if guess == "c":
        print("game over, your secret number was : " + str(meduim))
        state = False
    elif guess == "h":
        high = meduim
        meduim = (low + high) // 2
    elif guess == "l":
        low = meduim
        meduim = (low + high) // 2
    else :
        print("sorry, i did not understand your input, Try again!!")
        #else pour le controle de saisie; gestion des erreurs; intégrité des inputs .
