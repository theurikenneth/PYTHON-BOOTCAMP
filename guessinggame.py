import random
randomNumber = random.randint(1,30)
print(randomNumber)

i = 3
while i>0:
    guess = int(input("Enter a random number\n:"))

    if guess==randomNumber and guess>=1 and guess<=30:
        print("You Win!!!")
        break
    elif guess<1:
        print("Your guess is too Low")
    elif guess>30:
        print("Your guess is too high")
    elif guess!=randomNumber:
        i-=1
        if i==0:
            print("You Lose!!")
        else:
             print("You have",i,"attempts left")