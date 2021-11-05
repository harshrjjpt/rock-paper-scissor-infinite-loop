import random

you_win = 0
pc_win = 0
win_score = 3
while you_win < win_score and pc_win < win_score:
    print("***rock***")
    print("***paper***")
    print("***scissors***")
    print(f"your score:{you_win}  pc score:{pc_win}")

    print("make your choice:")
    p1=input().lower()
    if p1 == "quit" or p1 == "q":
    	break
    print(". \n" *5)

    pc_num = random.randint(0,2)
    if pc_num == 0:
        pc = "rock"
    elif pc_num == 1:
        pc = "paper"
    else:
        pc = "scissors"
    print(f"computer plays {pc}")

    if p1 == "rock" and pc == "scissors":
        print("you won!!")
        you_win += 1
    elif p1 == "scissors" and pc == "rock":
        print("you lose!")
        pc_win += 1
    elif p1 == "paper" and pc == "rock":
        print("you won !!!")
        you_win += 1
    elif p1 == "rock" and pc == "paper":
        print("you lose !!!")
        pc_win += 1
    elif p1 == "paper" and pc == "scissors":
        print("you lose !!!")
        pc_win += 1
    elif  p1 == "scissors" and pc == "paper":
        print("you won!!!")
        you_win =+1         
    elif p1 == pc:
        print("its a tie, hahaha")
    else:
        print("please enter 'rock,paper or scissors correctly")

if you_win > pc_win:
    print("congrats, you won")
elif you_win == pc_win:
	print("lol its a tie")
else:
    print("you lose ..... sed")






















