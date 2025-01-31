import random
attempts_list =[]
def show_score():
    if len(attempts_list) <=0:
        print("There is currently no high score")
    else:
        print("The current high score is {} attempts". format(min(attempts_list)))
        
def start_game():
    random_number= int(random.randint(1,10))
    print("Hello welcome to game of guesses")
    player_name= input("Please Enter your name to start the game")
    wanna_play =input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ". format(player_name))
    # print(wanna_play)
    attempts =0
    show_score()
    while wanna_play.lower() == "yes":
        guess = int(input("Please enter number between 1 to 10"))


        