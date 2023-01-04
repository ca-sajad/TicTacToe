import random
from models.responses import UserResponse, Button, AppResponse

'''
first written by: David McKenney 
modified for use with fastAPI
'''

board = [["", "", ""], ["", "", ""], ["", "", ""]]


def getrandomaimove():
    while True:
        r = random.randint(0, 2)
        c = random.randint(0, 2)

        if board[r][c] == "":
            break
    return r, c


def getwinner():
    # check rows:
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "":
            return board[row][0]
    # check cols:
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    # check diagonal:
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != "":
        return board[1][1]
    # check if any blanks:
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return ""
    return "Tie"


def eval_winner(winner):
    if winner == "Tie":
        return 0
    if winner == "X":
        return 1
    else:
        return -1


def getminimaxmove():
    move, score = minimax(board, True)
    return move[0], move[1]


'''Pseudocode:

You require a way of determining if the game is over.
Alternatively, you may need to limit the search to a specific depth for complicated games 
(add a function argument that you decrease in recursive calls)
You also need a way to measure the 'value' of the gameboard.
For tic-tac-toe, you can return 1 for AI win, -1 for human win, and 0 for tie. 
The AI tries to maximize the value they can obtain while the human tries to minimize 
the value the AI can obtain.

minimax(board, aiplayer):
	if the game is over:
		return None (no move, since game is over), eval(board)
		
	if aiplayer (or maximizing player, in general):
		bestmove = None
		bestscore = -Infinity (or any value less than the lowest possible score value. 
			this way, at least one of the possible moves will cause the bestmove to be updated)
	otherwise:
		bestmove = None
		bestscore = Infinity (same logic before except this player is minimizing, 
			so start with a high value)
		
	for every possible move m:
		
'''


def minimax(board, aiplayer):
    winner = getwinner()
    if winner != "":
        return None, eval_winner(winner)

    if aiplayer:
        bestmove = []
        bestscore = -10
    else:
        bestmove = []
        bestscore = 10

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                if aiplayer:
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"

                move, score = minimax(board, not aiplayer)
                board[r][c] = ""

                if aiplayer and score > bestscore:
                    bestmove = [r, c]
                    bestscore = score
                if not aiplayer and score < bestscore:
                    bestmove = [r, c]
                    bestscore = score
    return bestmove, bestscore


def playgame(user_response: UserResponse) -> AppResponse:
    if user_response.restart == "True":
        restart_game()
    else:
        winner = getwinner()
        if winner == "":
            button = int(user_response.changed_button.strip("button"))
            r, c = int(button / 3), int(button % 3)
            board[r][c] = "O"
            if getwinner() == "":
                if user_response.difficulty == "hard":
                    rai, cai = getminimaxmove()
                else:
                    rai, cai = getrandomaimove()
                board[rai][cai] = "X"

    app_response = AppResponse()
    app_response.buttons.clear()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            app_response.buttons.append(Button(button=3*i + j, choice=board[i][j]))
    app_response.winner = getwinner()
    return app_response


def return_board(response: AppResponse) -> AppResponse:
    response.buttons.clear()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            response.buttons.append(Button(button=3 * i + j, choice=board[i][j]))
    response.winner = getwinner()
    return response


def restart_game():
    board.clear()
    board.append(["", "", ""])
    board.append(["", "", ""])
    board.append(["", "", ""])
