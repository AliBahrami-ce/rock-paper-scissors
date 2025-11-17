from random import randint
import os

def game_menu():
    clear_screen()
    print('*' * 50) 
    print('1. Rock')
    print('2. Paper')
    print('3. Scissor')
    print('*' * 50)

def press_enter():
    input('Press enter to continue...')

def clear_screen():
    if os.name == 'nt':
        os.system('cls') # Windows Users
    else:
        os.system('clear') #Linux Users

def menu(): 
    run = True
    while run:
        clear_screen()
        print('-' * 50)
        print('1. Play with Bot.')
        print('2. Play with friend (offline).')
        print('3. Exit.')
        print('-' * 50)
        
        try:
            wrong_answer = True
            while wrong_answer:
                player_choice_menu = int(input('Enter your option.(1,2,3) '))
                
                if(player_choice_menu > 3 or player_choice_menu < 1):
                    print('ERORR : Please enter number between 1 to 3 :)')
                    print('-' * 50) 
                else:
                    wrong_answer = False
            
            run = options(player_choice_menu)
            
        except:
            print('What is that??! Enter a NUMBER...')
            press_enter()

def options(choice):
    if choice == 1:
        player_bot()
        return True
    elif choice == 2:
        player_friend()
        return True
    elif choice == 3:
        return False
        
def player_bot():
    bot_choice_game = randint(1,3) # 1 = rock, 2 = paper, 3 = scissor
    
    game_menu()

    try:
        wrong_answer = True
        while wrong_answer:
            player_choice_game = int(input('Enter number of your choice: '))
            if(player_choice_game > 3 or player_choice_game < 1):
                print('ERORR : Please enter number between 1 to 3 :)')
                print('-' * 50)
            else:
                result = get_winner(player_choice_game, bot_choice_game)
                clear_screen()
                print('1. Rock || 2. Paper || 3. Scissor')
                print('+' * 50)
                print(f'Player : {player_choice_game} | Bot : {bot_choice_game}')
                if result == 'player1':
                    print('<-> YOU WON... <-> \n')
                    press_enter()
                elif result == 'player2':
                    print('<-> BOT WON... <-> \n')
                    press_enter()
                else:
                    print('<-> DRAW... <-> \n')
                    press_enter()
                    
                wrong_answer = False
    except:
        print("What is that??! Next time, enter a NUMBER...")
        press_enter()
    
def player_friend(): 
    try:
        wrong_answer = True
        while wrong_answer:
            game_menu()
            player1_choice_game = int(input('Player 1 -> Enter number of your choice: '))
            if(player1_choice_game > 3 or player1_choice_game < 1):
                print('ERORR : Please enter number between 1 to 3 :)')
                print('-' * 50)
            else:
                game_menu()
                player2_choice_game = int(input('Player 2 -> Enter number of your choice: '))
                if(player2_choice_game > 3 or player2_choice_game < 1):
                    print('ERORR : Please enter number between 1 to 3 :)')
                    print('-' * 50)
                else:
                    result = get_winner(player1_choice_game, player2_choice_game)
                    clear_screen()
                    print('1. Rock || 2. Paper || 3. Scissor')
                    print('+' * 50)
                    print(f'Player 1 : {player1_choice_game} | Player 2 : {player2_choice_game}')
                    if result == 'player1':
                        print('<-> Player 1 WON... <-> \n')
                        press_enter()
                    elif result == 'player2':
                        print('<-> Player 2 WON... <-> \n')
                        press_enter()
                    else:
                        print('<-> DRAW... <-> \n')
                        press_enter()
                    
                    wrong_answer = False
                
    except:
        print("What is that??! Next time, enter a NUMBER...")
        press_enter()
    
def get_winner(player1, player2):
    if player1 == player2:
        return 'Draw'
    elif player1 == 1 and player2 == 2:
        return 'player2'
    elif player1 == 1 and player2 == 3:
        return 'player1'
    elif player1 == 2 and player2 == 1:
        return 'player1'
    elif player1 == 2 and player2 == 3:
        return 'player2'
    elif player1 == 3 and player2 == 1:
        return 'player2'
    elif player1 == 3 and player2 == 2:
        return 'player1'
    
menu()    
