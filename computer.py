
from working_class import *


class CompMoves:

    def __init__(self, board=None, row=None, col=None, piece=None):
        self.board = board
        self.row = row
        self.col = col
        self.piece = piece

    def evaluate_window(self,window,piece):
       self.window=window
       self.piece=piece

       score=0
       opp_piece=1

       if self.piece == 1:
           opp_piece=2

       if self.window.count(self.piece)== 4:
           score += 100
       elif self.window.count(self.piece)== 3 and self.window.count(EMPTY)== 1:
           score += 10
       elif self.window.count(self.piece) == 2 and self.window.count(EMPTY) == 2:
           score += 5

       if self.window.count(opp_piece)== 3 and self.window.count(EMPTY) == 1:
           score -= 80

       return score





    def score_position(self,board, piece):


        self.board=board
        self.piece=piece
        score = 0

        #score centre column
        centre_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
        centre_count = centre_array.count(piece)
        score += centre_count * 3



        #for horizontal

        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(self.board[r,:])]

            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += self.evaluate_window(window,self.piece)

        #for vertical

        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(self.board[:,c])]

            for r in range(ROW_COUNT - 3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += self.evaluate_window(window,self.piece)

        #for positive diagonal

        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window= [self.board[r+i][c+i] for i in range (WINDOW_LENGTH)]
                score += self.evaluate_window(window,self.piece)

        #for negative diagonal
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window= [self.board[r+3-i][c+i] for i in range (WINDOW_LENGTH)]
                score += self.evaluate_window(window,self.piece)


        return score




    def get_valid_locations(self, board):
        self.board = board
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if work_main.is_valid_location(self.board, col):
                valid_locations.append(col)

        return valid_locations



    def pick_best_move(self,board, piece):

        self.board = board
        self.piece=piece



        valid_locations = self.get_valid_locations(self.board)
        best_score = -10000
        best_col = random.choice(valid_locations)
        # print("random col:",best_col)

        for col in valid_locations:
            row = work_main.get_next_open_row(self.board, col)
            temp_board = board.copy()

            work_main.drop_piece(temp_board, row, col, self.piece)
            score = self.score_position(temp_board, self.piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col


moves_comp=CompMoves()



