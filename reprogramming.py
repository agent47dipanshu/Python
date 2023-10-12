import random
randnu = random.randint(1,100)
guess = 0
you = None

while randnu != you:
    you = int(input("Enter your number: "))
    guess += 1
    if you == randnu:
        print("You guess it right...")
        print(f"You guessed in {guess} tries...")
    elif you > randnu:
        print("You guessed it wrong.Enter a smaller number..")
    elif you < randnu:
        print("You guessed it wrong.Enter a larger number...")    
    else:
        print("You guessed it wrong...")

# if you == randnu:
#     with open ("hiscore.txt",'r') as f:
#         f.read ("hiscore")
     
#     if    
                