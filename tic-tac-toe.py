import cmd, re

# MANAGES THE GAME STATE

game_state = {
    "board": [[" "," "," "],[" "," "," "],[" "," "," "]],
    "player_1": "X",
    "player_2": "O",
    "current_player_turn": "player_1",
    "running_game": True
}

# THIS METHOD RUNS THE GAME

def run_game():
    print "Hello! Welcome to Tic Tac Toe..."

    while game_state["running_game"]:
        print "Type 'start' to play. "
        print "Type 'reset' to start over. "
        print "Type 'help' for instructions and help."
        print "Type 'exit' to quit the game."

        user_input = raw_input()

        if user_input == 'start':
            play_game()
        elif user_input == 'help':
            print "Type 'start' to play. "
            print "Type 'reset' to start over. "
            print "Type 'help' for instructions and help."
            print "Type 'exit' to quit the game."
            print "To make a move, just type in coordinates of the empty space in the following format 'x,y'. " \
                  "Use the numbers on the side of the board for guidance."
            pass
        elif user_input == 'reset':
            reset_game()
            print "The game has been reset."
            pass
        elif user_input == 'exit':
            game_state["running_game"] = False
            print "Exiting..."

        else:
            print "Invalid input"
            pass

# THIS METHOD PLAYS THE GAME

def play_game():
    move_count = 0

    while move_count < 9:
        display_board()

        print "Player {player}: Make a move".format(player=(game_state[game_state["current_player_turn"]]))
        move_input = raw_input()

        if valid_coords(move_input) and valid_move(int(move_input[0]),int(move_input[2])):
            player_move(int(move_input[0]),int(move_input[2]))

            if check_game_won():
                end_game(True)
                break
            else:
                next_player()
                move_count += 1
        elif move_input == 'reset':
            reset_game()
            print "The game has been reset."
            break
        elif move_input == 'help':
            print "Type 'start' to play. "
            print "Type 'reset' to start over. "
            print "Type 'help' for instructions and help."
            print "Type 'exit' to quit the game."
            print "To make a move, just type in coordinates of the empty space in the following format 'x,y'. " \
                  "Use the numbers on the side of the board for guidance."
            pass
        elif move_input == 'exit':
            game_state["running_game"] = False
            print "Exiting..."
            break
        else:
            print "Invalid input!"
            pass
    else:
        end_game(False)


# THIS METHOD SHOWS THE BOARD

def display_board():
    print "   0  1  2"
    print_row(game_state["board"][0], 0)
    print_row(game_state["board"][1], 1)
    print_row(game_state["board"][2], 2)

# THIS METHOD PRINTS EACH BOARD ROW

def print_row(row,pos):
    if pos == 2:
        print pos, row[0], "|", row[1], "|", row[2]
    else:
        print pos, row[0], "|", row[1], "|", row[2]
        print "  ---------"

# THIS METHOD CHECKS WHETHER THE PLAYER INPUTED THE COORDS CORRECTLY

def valid_coords(coords):
    if re.match(r"[0-2],[0-2]", coords):
        return True
    else:
        return False

# THIS METHOD CHECKS WHETHER THE PLAYER MOVE IS VALID

def valid_move(x,y):
    if game_state["board"][y][x] == " ":
        return True
    else:
        return False

# THIS METHOD UPDATES THE BOARD FOR THE PLAYER MOVE

def player_move(x,y):
    if game_state["current_player_turn"] == "player_1":
        game_state["board"][y][x] = "X"
    else:
        game_state["board"][y][x] = "O"

# THIS METHOD UPDATES THE CURRENT PLAYER

def next_player():
    if game_state["current_player_turn"] == "player_1":
        game_state["current_player_turn"] = "player_2"
    else:
        game_state["current_player_turn"] = "player_1"

# THIS METHOD CHECKS WHETHER THE GAME IS WON

def check_game_won():
    print col_check()

    if row_check():
        return True
    elif col_check():
        return True
    elif diag_check():
        return True
    else:
        return False

# THIS METHOD CHECKS FOR A WINNING ROW

def row_check():
    board = game_state["board"]

    for row in board:
        if row == ["X","X","X"] or row == ["O","O","O"]:
            return True
    else:
        return False

# THIS METHOD CHECKS FOR A WINNING COLUMN

def col_check():
    board = game_state["board"]

    for n in range(3):
        col = [board[k][n] for k in range(3)]

        if col == ["X", "X", "X"] or col == ["O", "O", "O"]:
            return True
    else:
        return False

# THIS METHOD CHECKS FOR A WINNING DIAGANOL

def diag_check():
    board = game_state["board"]
    left_right = [board[n][n] for n in range(3)]
    right_left = []

    pos = [n for n in range(2, -1, -1)]
    for k in range(3):
        right_left.append(board[k][pos[k]])

    if left_right == ["X", "X", "X"] or left_right == ["O", "O", "O"]:
        return True
    elif right_left == ["X", "X", "X"] or right_left == ["O", "O", "O"]:
        return True
    else:
        return False

# THIS METHOD ENDS THE GAME

def end_game(won):
    print game_state["current_player_turn"]
    if won:
        display_board()
        print "Player {player}: Congratulations! You have won!".format(player=(game_state[game_state["current_player_turn"]]))
        reset_game()
    else:
        display_board()
        print "Bummer... It looks like no one won... Better luck next time!"
        reset_game()

# THIS METHOD RESETS THE GAME MANAGER

def reset_game():
    game_state["board"] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game_state["current_player_turn"] = "player_1"
    game_state["move_count"] = 0

# THIS INVOKES THE GAME

run_game()
