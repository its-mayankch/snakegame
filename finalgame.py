import pygame
import random
pygame.init()

# creating window and setting caption
gameWindow = pygame.display.set_mode((1200,550))
pygame.display.set_caption("Snake Game")

# loading images and setting icon
bkg_img = pygame.transform.scale(pygame.image.load('snakebkg2.png'), gameWindow.get_size())
bkg_img_wel = pygame.transform.scale(pygame.image.load('snakehomepage.png'),gameWindow.get_size())
icon_img = pygame.image.load('snakeicon.png')
pygame.display.set_icon(icon_img)

# colors
red = (255,0,0)
blue = (0,0,255)
green =(0,255,0)
white = (255,255,255)

# clock
clock = pygame.time.Clock()
fps = 60

# font
font = pygame.font.SysFont(None,50)
font2 = pygame.font.SysFont('Lucida Console',30)
font3 = pygame.font.SysFont('Lucida console',15)

# score on screen
def show_score(text,color):
    text1 = font.render (text,True,color)
    gameWindow.blit(text1,(5,5))

def plot_snake(snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,red,(x,y,snake_size,snake_size))

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(bkg_img_wel, (0, 0))
        text1 = font.render ('Welcome to the world of snakes',True,blue)
        gameWindow.blit(text1,(300,150))
        text2 = font2.render('Press C for classic mode ',True,red)
        gameWindow.blit(text2,(350,220))
        text3 = font2.render('Press E for endless mode ',True,red)
        gameWindow.blit(text3,(350,270))
        text4 = font3.render('Description : in endless mode snake height is constant and boundaries are not restricted',True,white)
        gameWindow.blit(text4,(50,450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_loop()
                if event.key == pygame.K_e:
                    game_loop2()

        pygame.display.update()
        clock.tick(fps)

High_score1 = 0

# Classic mode
def game_loop():
    
    # Game specific variables
    exit_game = False
    game_over = False
    food_x = random.randint(5,gameWindow.get_width()-20)
    food_y = random.randint(45,gameWindow.get_height()-20)
    food_size = 15
    fps = 60
    score =0

    snake_x = 10
    snake_y = 50                         
    snake_size = 15
    vel_x = 0
    vel_y = 0
    init_vel = 5

    snk_list = []
    snk_lenght = 1

    while not exit_game:
        global High_score1
        # background image
        gameWindow.blit(bkg_img, (0, 0))

        if game_over:
            text2 = font.render("Your score : "+str(score),True,white)
            gameWindow.blit(text2,(500,190))
            text1 = font.render ("Tera Khel Khatam Hai!  Enter Daba",True,white)
            gameWindow.blit(text1,(370,225))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            #for quit 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True


                # Movement decide

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = init_vel
                        vel_y = 0

                    if event.key == pygame.K_LEFT:
                        vel_x = -init_vel
                        vel_y = 0

                    if event.key == pygame.K_UP:
                        vel_x = 0
                        vel_y = - init_vel

                    if event.key == pygame.K_DOWN:
                        vel_x = 0
                        vel_y = init_vel

                    if event.key == pygame.K_h:
                        welcome()
                        pygame.quit()

            if vel_x==0 and vel_y==0 and score==0:
                text2 = font.render("Press any arrow key to start",True,white)
                gameWindow.blit(text2,(400,200))
                text3 = font.render("Press H to go to home ",True,white)
                gameWindow.blit(text3,(400,270))

            # adding food to eat
            food_rect = pygame.draw.rect(gameWindow,blue,(food_x,food_y,food_size,food_size))

            # making snake move
            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y

            snake_rect = pygame.Rect((snake_x,snake_y,snake_size,snake_size))
            # updating score
            if snake_rect.colliderect(food_rect):
                score+=1
                # creating new food
                food_x = random.randint(5,gameWindow.get_width()-15)
                food_y = random.randint(35,gameWindow.get_height()-15)
                snk_lenght+=5
                if score>High_score1:  
                    High_score1 = score

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]

            # condition of game over
            if head in snk_list[:-1]:
                game_over = True
            if snake_x<0 or snake_x>gameWindow.get_width() or snake_y<0 or snake_y>gameWindow.get_height() :
                game_over = True

            plot_snake(snk_list,snake_size)
            show_score("Score : "+str(score)+"    High Score : "+str(High_score1),green)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


# Endless mode 
def game_loop2():
    # text font 
    font1 = pygame.font.SysFont('freesanbold', 50)

    # Game specific variables
    exit_game = False

    food_x = random.randint(5,gameWindow.get_width()-20)
    food_y = random.randint(45,gameWindow.get_height()-20)

    fps = 30

    score =0

    snake_x = 10
    snake_y = 50
    snake_size = 15
    food_size = 15
    vel_x = 0
    vel_y = 0

    # event loop
    while not exit_game:

        #for quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            # Movement decide

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_x = 10
                    vel_y = 0

                if event.key == pygame.K_LEFT:
                    vel_x = -10
                    vel_y = 0

                if event.key == pygame.K_UP:
                    vel_x = 0
                    vel_y = - 10

                if event.key == pygame.K_DOWN:
                    vel_x = 0
                    vel_y = 10

                if event.key == pygame.K_q:
                    vel_x = 0
                    vel_y = 0

                if event.key == pygame.K_h:
                    welcome()
                    pygame.quit()

        # background image
        gameWindow.blit(bkg_img, (0, 0))

        # adding food to eat
        food_rect = pygame.draw.rect(gameWindow,blue,(food_x,food_y,food_size,food_size))

        # making snake move
        snake_x = snake_x + vel_x
        snake_y = snake_y + vel_y

        # updating score
        snake_rect =pygame.Rect((snake_x,snake_y,snake_size,snake_size))
        if snake_rect.colliderect(food_rect):
            score+=1
            # creating new food
            food_x = random.randint(5,gameWindow.get_width()-15)
            food_y = random.randint(45,gameWindow.get_height()-15)

        # snake
        if vel_y==0:
            pygame.draw.rect(gameWindow,red,(snake_x,snake_y,snake_size+10,snake_size))
        if vel_x==0 and vel_y!=0:
            pygame.draw.rect(gameWindow,red,(snake_x,snake_y,snake_size,snake_size+10))

        if (snake_x<0):
            snake_x=gameWindow.get_width()
        if (snake_x>gameWindow.get_width()):
            snake_x=0
        if (snake_y<50):
            snake_y=gameWindow.get_height()
        if (snake_y>gameWindow.get_height()):
            snake_y=45

        text1=font1.render("Score : "+str(score),True,green)
        gameWindow.blit(text1,(5,3))
        if vel_x==0 and vel_y==0 :
            text2=font1.render(("Press any arrow key to start"),True,green)
            gameWindow.blit(text2,(350,3))
            text3=font1.render(("Press H to go to home"),True,white)
            gameWindow.blit(text3,(350,200))
        else :
            text2=font1.render(("Press q to quit"),True,green)
            gameWindow.blit(text2,(450,3))
        text2=font3.render(("ENDLESS MODE"),True,white)
        gameWindow.blit(text2,(950,10))
        pygame.draw.rect(gameWindow,green,(0,40,1200,3))

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

welcome()


