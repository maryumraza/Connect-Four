from creation import *
from player import *
import time





def button(msg, x, y, w, h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()


    if x+w> mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,GREEN, (x, y, w, h))
        if click[0]==1 and action!=None:

            action()



    else:
        pygame.draw.rect(screen,green, (x, y, w, h))


    font = pygame.font.Font('freesansbold.ttf', 20)

    smallText = font.render(msg, True, WHITE)

    textRect = smallText.get_rect()
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(smallText, textRect)



def new_loop():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # font = pygame.font.SysFont('Elephant', 90)
        font = pygame.font.SysFont("Bowlby One SC", 70)
        text = font.render('Connect Four', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 3)
        screen.fill(BLACK)
        screen.blit(text, textRect)

        button("play", 300, 350, 100, 50, green, GREEN, game_loop)
        button("quit", 300, 450, 100, 50, green, GREEN, quit)
        button("scores", 300, 550, 100, 50, green, GREEN, scores)

        pygame.display.update()
        clock.tick(15)


def game_end():


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # font = pygame.font.SysFont("Elephant", 50)
            font = pygame.font.SysFont("Bowlby One SC", 40)
            text = font.render("Do you want to continue?", True, green)
            textRect = text.get_rect()
            textRect.center = (width // 2, height / 2.5)
            screen.fill(BLACK)
            screen.blit(text, textRect)

            button("yes", 200, 400, 100, 50, green, GREEN, new_loop)
            button("no", 400, 400, 100, 50, green, GREEN, quit)

            pygame.display.update()
            clock.tick(15)

def scores():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        file = shelve.open('score_file')
        match_played = file['matches']
        player_won = file['player']
        comp_won = file['computer']

        # while True:
        font = pygame.font.SysFont("Bowlby One SC", 60)

        text=font.render("Score Board",True,green)
        textRect=text.get_rect()
        textRect.center= (width//2, height/3)
        screen.fill(BLACK)
        screen.blit(text, textRect)


        newfont = pygame.font.Font('freesansbold.ttf', 20)

        text1=newfont.render("games played",True,green)
        text11=newfont.render(str(match_played),True,green)
        text2=newfont.render("player won",True,green)
        text22=newfont.render(str(player_won),True,green)
        text3 = newfont.render("computer won", True, green)
        text33=newfont.render(str(comp_won),True,green)
        dots=newfont.render("....................",True,green)

        textRect1=text1.get_rect()
        textRect11 = text11.get_rect()
        textRect2 = text2.get_rect()
        textRect22 = text22.get_rect()
        textRect3 = text3.get_rect()
        textRect33 = text33.get_rect()
        textdot1= dots.get_rect()
        textdot2 = dots.get_rect()
        textdot3 = dots.get_rect()

        textRect1.center=(width//3, height//2)
        textRect11.center = (width // 1.5, height // 2)
        textRect2.center = (width // 3, height // 1.75)
        textRect22.center = (width // 1.5, height // 1.75)
        textRect3.center = (width // 3, height // 1.5)
        textRect33.center = (width // 1.5, height // 1.5)
        textdot1.center= (width/1.85 , height//2)
        textdot2.center = (width / 1.85, height // 1.75)
        textdot3.center = (width / 1.85, height // 1.5)


        screen.blit(text1, textRect1)
        screen.blit(text11, textRect11)
        screen.blit(dots,textdot1)
        screen.blit(text2, textRect2)
        screen.blit(text22, textRect22)
        screen.blit(dots, textdot2)
        screen.blit(text3, textRect3)
        screen.blit(text33, textRect33)
        screen.blit(dots, textdot3)

        button("back", 300, 550, 100, 50, green, GREEN, new_loop)


        pygame.display.update()
        clock.tick(15)




def quit():

    sys.exit()


def game_loop():

    board=create.create_board()
    create.draw_Board(board)
    moves_player.keyboard(board)
    game_end()


new_loop()
