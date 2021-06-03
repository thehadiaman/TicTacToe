class TicTacToe:
    def __init__(self):
        self.board = [
            [" ", " 1 ", " 2 ", " 3 "],
            ["A", "   ", "   ", "   "],
            ["B", "   ", "   ", "   "],
            ["C", "   ", "   ", "   "],
        ]
        self.avatar_one = "X"
        self.avatar_two = "O"
        self.empty_cols = 0

    def display_board(self):
        print("_______________________")
        print(f"|   |  1  |  2  |  3  |")
        print("-----------------------")
        print(f"| A | {self.board[1][1]} | {self.board[1][2]} | {self.board[1][3]} |")
        print(f"| B | {self.board[2][1]} | {self.board[2][2]} | {self.board[2][3]} |")
        print(f"| C | {self.board[3][1]} | {self.board[3][2]} | {self.board[3][3]} |")
        print("_______________________")
        return

    def column_selector(self, index):
        board_column = int(index[0])
        board_row = index[1]

        for column in self.board:
            if column[0] == board_row:
                if column[board_column] == "   ":
                    if self.empty_cols % 2 == 0:
                        column[board_column] = f" {self.avatar_one} "
                        self.empty_cols += 1
                    else:
                        column[board_column] = f" {self.avatar_two} "
                        self.empty_cols += 1
                    return
                else:
                    print("Can't use the column with value")
        return

    def who_win(self):
        row_1 = self.board[1]
        row_2 = self.board[2]
        row_3 = self.board[3]

        # Horizontal
        test_1 = [row_1[1] == row_1[2] and row_1[2] == row_1[3] and row_1[1] != "   ", row_1[1]]
        test_2 = [row_2[1] == row_2[2] and row_2[2] == row_2[3] and row_2[1] != "   ", row_2[1]]
        test_3 = [row_3[1] == row_3[2] and row_3[2] == row_3[3] and row_3[1] != "   ", row_3[1]]

        # Vertical
        test_4 = [row_1[1] == row_2[1] and row_2[1] == row_3[1] and row_1[1] != "   ", row_1[1]]
        test_5 = [row_1[2] == row_2[2] and row_2[2] == row_3[2] and row_1[2] != "   ", row_1[2]]
        test_6 = [row_1[3] == row_2[3] and row_2[3] == row_3[3] and row_1[3] != "   ", row_1[3]]

        # XCross
        test_7 = [row_1[1] == row_2[2] and row_2[2] == row_3[3] and row_1[1] != "   ", row_1[1]]
        test_8 = [row_1[3] == row_2[2] and row_2[2] == row_3[1] and row_1[3] != "   ", row_1[3]]

        tests = [test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8]
        for test in tests:
            if True in test:
                if test[1] == ' X ':
                    print('Player One won')
                else:
                    print('Player Two won')
                return True
        return False

    def is_game_end(self):
        if self.who_win() or self.empty_cols == 9:
            return False
        return True

    def play(self, index):
        indexes = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C"]
        if index in indexes:
            self.column_selector(index)
        else:
            print("The values must be in index")
            return
        return


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.display_board()

    while tic_tac_toe.is_game_end():
        user_play = input(':Player Two: ') if tic_tac_toe.empty_cols % 2 == 1 else input(':Player One: ')
        tic_tac_toe.play(user_play.upper())
        tic_tac_toe.display_board()
