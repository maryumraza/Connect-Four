
from computer import *
# from main_loop import game_end

class PlayerMoves:



    def __init__(self, board=None, row=None, col=None, piece=None):
        self.board = board
        self.row = row
        self.col = col
        self.piece = piece

    def make_ball(self, board, row, col):
        self.board = board
        self.row = row
        self.col = col


        if self.board[self.row][self.col] == PLAYER_BALL:
            pygame.draw.circle(screen, RED, (int(self.col * SQUARE_SIZE + SQUARE_SIZE / 2), height - (int(self.row * SQUARE_SIZE + SQUARE_SIZE / 2))), RADIUS)
        elif self.board[self.row][self.col] == COMP_BALL:
            pygame.draw.circle(screen, YELLOW, (int(self.col * SQUARE_SIZE + SQUARE_SIZE / 2), height - (int(self.row * SQUARE_SIZE + SQUARE_SIZE / 2))), RADIUS)

        pygame.display.update()


    def keyboard(self, board):
        game_over = False

        self.board = board
        turn = random.randint(PLAYER, AI)

        x = int(SQUARE_SIZE / 2)
        y = int(SQUARE_SIZE / 2)
        initial_position = (x, y)
        pygame.draw.circle(screen, RED, initial_position, RADIUS)


        while not game_over:



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:


                    if turn == PLAYER and event.key == pygame.K_RIGHT:

                        if x < 650:
                            x += int(SQUARE_SIZE)
                            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                            pygame.draw.circle(screen, RED, (x, y), RADIUS)

                    elif turn == PLAYER and event.key == pygame.K_LEFT:
                        if x > 50:
                            x -= int(SQUARE_SIZE)

                            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                            pygame.draw.circle(screen, RED, (x, y), RADIUS)

                    elif turn == PLAYER and event.key == pygame.K_DOWN:

                        col = int(math.floor(x / SQUARE_SIZE))
                        if work_main.is_valid_location(self.board, col):
                            row = work_main.get_next_open_row(self.board, col)

                            work_main.drop_piece(self.board, row, col, PLAYER_BALL)

                            self.make_ball(self.board, row, col)
                            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                            # pygame.draw.circle(screen, YELLOW, (x, y), RADIUS)

                            turn += 1
                            turn = turn % 2

                            if work_main.winning_move(self.board, PLAYER_BALL):

                                label=win_font.render("Player wins!!",True,RED)
                                screen.blit(label,(40,10))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                work_main.score_board(PLAYER_BALL)
                                game_over = True

                            else:
                                pygame.draw.circle(screen, YELLOW, (x, y), RADIUS)


                    pygame.display.update()








            if turn == AI :

                col = moves_comp.pick_best_move(self.board,COMP_BALL)
                # col,minimax_score=object4.minimax(self.board,4,True)

                # col = random.randint(0,COLUMN_COUNT-1)
                if work_main.is_valid_location(self.board, col):
                    pygame.time.wait(1000)
                    row = work_main.get_next_open_row(self.board, col)

                    work_main.drop_piece(self.board, row, col, COMP_BALL)
                    self.make_ball(self.board, row, col)
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                    # pygame.draw.circle(screen, RED, (x, y), RADIUS)

                    turn += 1
                    turn = turn % 2


                    if work_main.winning_move(self.board, COMP_BALL):
                        # pygame.time.wait(2000)
                        label = win_font.render("Computer wins!!", True,YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        work_main.score_board(COMP_BALL)
                        game_over = True

                    else:
                        pygame.draw.circle(screen, RED, (x, y), RADIUS)

            pygame.display.update()


        # game_end()


moves_player=PlayerMoves()



