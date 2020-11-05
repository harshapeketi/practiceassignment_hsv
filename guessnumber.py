print("WELCOME TO GUESS THE NUMBER GAME ")
print("YOU WANT TO PLAY THIS GAME ???")
email_id = input("please enter your email id:")
if email_id == "harsha.chnu@gmail.com":
    password = input("please enter your password:")
if password == "07102004":
    print("your have successfully logined")
else:
    print("failed")


import random
def guess_the_number_game():
    number = random.randint(1, 100)
    x = 1
    while x < 6:
        guessing_number = int(input("guess the number between 1 to 100:"))
        x = x + 1
        if (guessing_number < 1 and guessing_number < 100):
            print("it should be in the range 1 to 100")
        if guessing_number == number:
            another_chance = input("IT IS CORRECT!!!,you want to play again???(yes/no)")
            if another_chance == "yes":
                guess_the_number_game()
            if another_chance == "no":
                print("okay,bye!!! HAVE A NICE DAY!! ")
                break
        if guessing_number < number:
            print("it is lower value")
        elif guessing_number > number:
            print("it is higher value")

try:
    guess_the_number_game()
except:
    print("this is not the number")
    guess_the_number_game()


print("OPPS !!!,You have used all chances,better luck next time !!,okay,bye!!! HAVE A NICE DAY!! ")
