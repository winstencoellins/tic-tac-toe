"""
Written by: Winsten Coellins
Title: 2 Player Tic Tac Toe
"""


class TicTacToe:
    """
    Initialization of the TicTacToe object with three parameters
    Constructor
    """

    def __init__(self):
        self.player1 = "X"
        self.player2 = "O"
        self.board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]

    """
    This function is to check whether O or X are occupying the space.
    If either one is occupying the space, tell the user if the space is occupied
    and choose another space. Else, occupy the space with either O or X.
    Return True if occupied so that the program can ask the user to re-input the number
    Return False if the space is not occupied and continue to another player.
    """

    def check_occupied(self, num, player, board):
        if 1 <= num <= 3:
            if board[0][num - 1] != "-":
                print("This space is occupied, please choose another space.")
                return True
            else:
                board[0][num - 1] = player
                return False
        elif num <= 6:
            if board[1][num - 4] != "-":
                print("This space is occupied, plese choose another space.")
                return True
            else:
                board[1][num - 4] = player
                return False
        elif num <= 9:
            if board[2][num - 7] != "-":
                print("This space is occupied, please choose another space.")
                return True
            else:
                board[2][num - 7] = player
                return False

    """
    This function is to check the winning condition for player X.
    """

    def check_winning_X(self, board):
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            return "X win"
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            return "X win"
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            return "X win"
        elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            return "X win"
        elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            return "X win"
        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            return "X win"
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            return "X win"
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            return "X win"
        else:
            print(" ")

    """
    This function is to check the winning condition for player O
    """

    def check_winning_O(self, board):
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            return "O win"
        elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
            return "O win"
        elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            return "O win"
        elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            return "O win"
        elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            return "O win"
        elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            return "O win"
        elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            return "O win"
        elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            return "O win"
        else:
            print(" ")

    """
    This function is to print out the board to the console so that the
    player can visualize the condition of the updated board.
    """

    def print_board(self, board):
        length_counter = 0
        for i in range(len(board)):
            for j in board[i]:
                if length_counter == 2:
                    print("|" + " " + str(j) + " " + "|", end="\n")
                else:
                    print("|" + " " + str(j) + " " + "|", end="")
                length_counter += 1
            length_counter = 0

    """
    This is the main function to start the game. This function needs to 
    be called to start the game.
    """

    def start_game(self):
        win = "Draw Match ..."
        pointer = 0
        val_holder = True
        while ("-" in self.board[0]) or ("-" in self.board[1]) or ("-" in self.board[2]):
            if pointer == 0:
                while val_holder:
                    player1_input = int(
                        input("Choose where to place the 'X' (1 to 9): "))

                    if player1_input > 9 or player1_input < 1:
                        print("Value not recognized ...", end="\n")
                    else:
                        val_holder = self.check_occupied(
                            player1_input, self.player1, self.board)

                val_holder = True
                self.print_board(self.board)

                win = self.check_winning_X(self.board)

                if win == "X win":
                    break

                pointer += 1
            else:
                while val_holder:
                    player2_input = int(
                        input("Choose where to place the 'O' (1 to 9): "))

                    if player2_input > 9 or player2_input < 1:
                        print("Value not recognized ...", end="\n")
                    else:
                        val_holder = self.check_occupied(
                            player2_input, self.player2, self.board)

                val_holder = True
                self.print_board(self.board)

                win = self.check_winning_O(self.board)

                if win == "O win":
                    break

                pointer -= 1

        print(win, end="\n")


T = TicTacToe()
T.start_game()
