import random

def play_game():
    choices= ['snake','water','gun']
    user_score=0
    comp_score=0
    rounds=int(input('Enter number of rounds you want to play this game \n'))

    for i in range(rounds):
        user_choice=input("Enter your choice (snake,water,gun)\n").lower()
        comp_choice=random.choice(choices)
        print(f"Round{i +1}:you choose{user_choice},computer choose{comp_choice}")
 
        if user_choice == "snake":
            if comp_choice == "water":
                 print("you win! snake drink water")
                 user_score +=1
            elif comp_choice == "gun":
                print("Sorry! you loose,snake got killed by gun")
                comp_score +=1

            else:
                print("Match is draw")


        elif user_choice == "water":
            if comp_choice == "gun":
              print("you win!,gun drowned in water")
              user_score +=1

            elif comp_choice == "snake":
                 print("sorry!,snake drink water")
                 comp_score +=1

            else:
              print("Match is draw")


        elif user_choice == "gun":
            if comp_choice == "snake":
              print("you win !,snake got killed by gun")
              user_score +=1

            elif comp_choice =="water":
              print("soryy!,gun dorwned by water")
              comp_score +=1
        
            else:
             print("match is draw")

        else:
            print("Invalid ! input,you loose this round")
            comp_score +=1


    print("\n GAME OVER")

    if user_score>comp_score:
       print(f"you win {user_score} rounds and computer loose {comp_score}")


    elif comp_score> user_score:
       print(f"you loose {user_score} and computer win{comp_score}")

    else:
       print(f"game is draw! both you and computer tied this match{user_score}")
   
play_game()