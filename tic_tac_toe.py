import os
import sys
from random import randrange

# Function to clear the terminal for better readability
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize the board and free fields list
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
free_fields = []

# Function to reset the game state
def reset_game():
    global board, free_fields
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Reset board to initial state
    free_fields = []  # Clear free fields list
    clear_terminal()
    display_board(board)
    enter_move(board)

# Function to display the current state of the board
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

# Function to update the list of free fields
def make_list_of_free_fields(board):
    global free_fields
    free_fields = [(i, j) for i in range(3) for j in range(3) if isinstance(board[i][j], int)]

# Function to handle the player's move
def enter_move(board):
    global free_fields
    make_list_of_free_fields(board)
    
    # Check for tie before player's move
    if len(free_fields) == 0:
        show_message("tie")
        play_again()
        return

    try:
        selected_space = int(input("Enter your move, select free space: "))

        if selected_space < 1 or selected_space > 9:
            print("The number must be between 1 and 9. Try again.")
            return enter_move(board)

        for linha, coluna in free_fields:
            if board[linha][coluna] == selected_space:
                board[linha][coluna] = 'X'
                make_list_of_free_fields(board)
                clear_terminal()
                display_board(board)
                if victory_for(board, 'X'):
                    show_message("win")
                    play_again()
                    return
                draw_move(board)
                return

        print("Space must be free! Try again.")
        return enter_move(board)

    except ValueError:
        print("Not a number! Try again.")
        return enter_move(board)

# Function to handle the computer's move
def draw_move(board):
    global free_fields
    make_list_of_free_fields(board)

    # Check for tie after player's move
    if len(free_fields) == 0:
        show_message("tie")
        play_again()
        return

    while True:
        random_number = randrange(1, 10)
        for linha, coluna in free_fields:
            if board[linha][coluna] == random_number:
                board[linha][coluna] = 'O'
                make_list_of_free_fields(board)
                clear_terminal()
                display_board(board)
                if victory_for(board, 'O'):
                    show_message("lose")
                    play_again()
                    return
                # Check for tie after computer's move
                if len(free_fields) == 0:
                    show_message("tie")
                    play_again()
                    return
                enter_move(board)
                return

# Function to check if there is a victory for the given sign
def victory_for(board, sign):
    # Check rows
    for linha in board:
        if all(cell == sign for cell in linha):
            return True

    # Check columns
    for coluna in range(3):
        if all(board[linha][coluna] == sign for linha in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

# Function to ask the player if they want to play again
def play_again():
    answer = input("Do you want to play again? (yes/no): ").strip().lower()
    if answer in ['yes', 'y']:
        reset_game()
    else:
        print("Thanks for playing!")
        sys.exit()

# Function to display win, lose or tie messages with ASCII art
def show_message(message):
    clear_terminal()  # Clear the terminal before showing the message

    if message == "win":
        print("""
__     ______  _    _  __          __ _  _   _ 
\ \   / / __ \| |  | | \ \        / /| || \ | |
 \ \_/ / |  | | |  | |  \ \  /\  / / | ||  \| |
  \   /| |  | | |  | |   \ \/  \/ /  | || . ` |
   | | | |__| | |__| |    \  /\  /   | || |\  |
   |_|  \____/ \____/      \/  \/    |_||_| \_|
                                                                               
        """)
        print("🎉 Congratulations! You WIN! 🎉\n")

    elif message == "lose":
        print("""
__     ______  _    _   _      ____   _____ ______ 
\ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
 \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
  \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
   | | | |__| | |__| | | |___| |__| |____) | |____ 
   |_|  \____/ \____/   \_____\____/|_____/|______|
                                                  
        """)
        print("💔 Oh no! You LOSE! Better luck next time! 💔\n")
    
    elif message == "tie":
        print("""
 _________ _____ ______ 
|___   ___|_   _|  ____|
    | |     | | | |__   
    | |     | | |  __|  
    | |    _| |_| |____ 
    |_|   |_____|______|
                                                  
        """)
        print("🤝 It's a TIE! Good game! 🤝\n")
    
    input("Press ENTER to continue...")  # Wait for the player to read the message