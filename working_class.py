from common_variables import *


class Working:

    def __init__(self,board=None, row=None, col=None, piece=None):
        self.board=board
        self.row=row
        self.col=col
        self.piece=piece


    def is_valid_location(self, board, col):
        self.board = board
        self.col = col
        return self.board[ROW_COUNT - 1][self.col] == 0

    def get_next_open_row(self, board, col):
        self.board = board
        self.col = col
        for r in range(ROW_COUNT):
            if self.board[r][self.col] == 0:

                return r

    def drop_piece(self, board, row, col, piece):
        self.board = board
        self.row = row
        self.col = col
        self.piece = piece

        self.board[self.row][self.col] = self.piece

    def winning_move(self, board, piece):
        self.board = board
        self.piece = piece


        # check horizontal location
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == self.piece and self.board[r][c + 1] == self.piece and self.board[r][c + 2] == self.piece and self.board[r][c + 3] == self.piece:
                    return True

        # check vertical location
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == self.piece and self.board[r + 1][c] == self.piece and self.board[r + 2][c] == self.piece and self.board[r + 3][c] == self.piece:
                    return True

        # check for positive diagonal
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == self.piece and self.board[r + 1][c + 1] == self.piece and self.board[r + 2][c + 2] == self.piece and self.board[r + 3][c + 3] == self.piece:
                    return True

        # check for negative diagonal
        for c in range(COLUMN_COUNT - 1, COLUMN_COUNT - 5, -1):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == self.piece and self.board[r + 1][c - 1] == self.piece and self.board[r + 2][c - 2] == self.piece and self.board[r + 3][c - 3] == self.piece:
                    return True


    def score_board(self,piece):
        self.piece=piece

        file=shelve.open('score_file')
        match_played=file['matches']
        match_played+=1
        file['matches']=match_played
        # print(match_played)

        if self.piece==PLAYER_BALL:
            player_won = file['player']
            player_won+=1
            file['player']=player_won
            # print(player_won)

        elif self.piece==COMP_BALL:
            comp_won = file['computer']
            comp_won+=1
            file['computer']=comp_won
            # print(comp_won)

        file.close()


#
work_main = Working()