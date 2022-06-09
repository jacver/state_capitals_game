from capitals import states
import random
# print(states)

def shuffle_states_list():
    ### Shuffle game data ###
    random.shuffle(states)
shuffle_states_list()

def add_keys_to_dict():
    ### Add keys to each state for correct and incorrect responses ###
    for state in states:
        state["correct"] = 0
        state["incorrect"] = 0
add_keys_to_dict()



def welcome_player():
    ### Welcome sequence ###
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print('Welcome to the Python State Capitals game! What is your name?')
    username = input()
    print(f"Nice to meet you, {username}. Let's get started.")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
welcome_player()

def play_game(states_list):
    ### Initialize Score ###
    score = 0
    
    ### Game turn Managed Within For Loop ###
    for idx, state in enumerate(states_list):

        ### Set variables for game sequence ###
        state_name = state["name"]
        state_capital = state["capital"]

        ### Question Prompt & Answer Collection ###
        print("----------------------------------------------------------")
        print(f"Question {idx + 1}: What is the capital of {state_name}?")
        print(f">>  HINT: The first 3 letters are: {state_capital[0 : 3]}  <<")
        print("----------------------------------------------------------")
        answer = input().title()

        ### Scoring ###
        if answer == state_capital:
            score += 1
            state["correct"] += 1
            print(f"Correct! The capital of {state_name} is {state_capital}!")
            print(f"Your score is now {score}.")
        else: 
            state["incorrect"] += 1
            print(f"Wrong! The capital of {state_name} is {state_capital} - not {answer}.")
            print(f"Your score remains {score}")

        ### Handle Final Scoring ###
        if idx == len(states_list) - 1:
            print("----------------------------------------------------------")
            print("You made it! Let's check your score...")
            if score == 50:
                print(f"Amazing! Are you George Washington or something? You scored a perfect {score} out of {idx + 1}.")
            if score < 50 and score >= 35:
                print(f"Not bad! You scored {score} out of {idx + 1}.")
            if score < 35 and score >= 25:
                print(f"Getting there! You should probably buy a map though. You scored a {score} out of {idx + 1}.")
            if score < 25:
                print(f"Not even half? You're not invited to July 4th. You scored {score} out of {idx + 1}.")
        
            ### Handle Play Again? ###
            print("----------------------------------------------------------")
            print("Would you like to play again?")

            play_again = input().capitalize()

            if play_again == "Yes":
                ### Sort by ones with most incorrect responses ###
                sorted_list = sorted(states_list, key=lambda i: i['incorrect'], reverse = True)
                print(sorted_list)

                ### Reinitialize game using this sorted list ###
                play_game(sorted_list)

            else:
                ### Farewell! ###
                print("Bye! Study up before you come back!")


play_game(states)
