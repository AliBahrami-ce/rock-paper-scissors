from random import randint
import os

global player_choice_menu
player_choice_menu = 0

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
        print('-' * 20)
        print('1. Play with Bot.')
        print('2. Play with friend (offline).')
        print('3. Exit.')
        print('-' * 20)
        
        try:
            wrong_answer = True
            while wrong_answer:
                player_choice_menu = int(input('Enter your option.(1,2,3) '))
                
                if(player_choice_menu > 3 or player_choice_menu < 1):
                    print('ERORR : Please enter number between 1 to 3 :)')
                    print('-' * 20) 
                else:
                    wrong_answer = False
            
            run = options(player_choice_menu)
            
        except:
            print('What is that??! Enter Number...')
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
    
    bot_player = randint(0,2) # 0 = rock, 1 = paper, 2 = scissor
    
    print('*' * 20) 
    print('1. Rock')
    print('2. Paper')
    print('3. Scissor')
    print('*' * 20)
    try:
        player_choice_game = int(input('Enter number of your choice: '))
          
    except:
        pass
    
    pass

def player_friend():
    pass

menu()    
