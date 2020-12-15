import random

print("Welcome to Stone Paper Scissor Game\nLets begin")
name = input("Kindly Enter your Name\n")

lst = ["stone","paper", "scissor"]


i = 1
cs = 0
us = 0
while i <= 3:
    cc = random.choice(lst)
    uc = input("\nChoose your option\n")

    if cc == "stone" and uc == "paper":
        print("User won")
        cs = cs + 1

    elif cc == "paper" and uc == "stone":
        print("Computer won")
        us = us + 1

    elif cc == "scissor" and uc == "paper":
        print("Computer won")
        cs = cs + 1

    elif cc == "stone" and uc == "scissor":
        print("Computer won")
        us = us + 1

    elif cc == "stone" and uc == "stone":
        print("Its a Tie")
        cs = cs
        us = us

    elif cc == "paper" and uc == "paper":
        print("Its a tie")
        cs = cs
        us = us

    elif cc == "paper" and uc == "scissor":
        print("User won")
        us = us + 1

    elif cc == "scissor" and uc == "stone":
        print("User won")
        cs = cs + 1

    elif cc == "scissor" and uc == "scissor":
        print("Its a tie")
        cs = cs
        us = us

    else:
        print("choose valid option")

    i=i+1

if us > cs:
    winner = f"\nwinner is {name} and score is {us}"
    print(winner)
elif us == cs:
    print("Its a Tie")
    score = f"\nuser score: {us} , computer score: {cs}"
    print(score)
else:
    winner = f"\nwinner is computer and score is {cs}"
    print(winner)