import pygame
import pygame_menu
import random

pygame.init()
table_score = []
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 1920
dis_height = 1080
dis = pygame.display.set_mode((dis_width, dis_height)) #Задаём размер игрового поля.
pygame.display.set_caption('Змейка от Progium') #Добавляем название игры.
clock = pygame.time.Clock()
snake_block = 25
snake_speed = 15
dif = "Easy"
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("comicsansms", 35)


background_image = pygame.image.load('bg.png')
pygame.mixer.music.load('Medianoche.mp3')
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.5)
menu = pygame_menu.Menu('Snake', dis_width, dis_height,theme=pygame_menu.themes.THEME_ORANGE)
options_menu = pygame_menu.Menu('Options', dis_width, dis_height,theme=pygame_menu.themes.THEME_ORANGE)
def options():
    options_menu.enable()
    options_menu.mainloop(dis)
def music_volume(value):
    pygame.mixer.music.set_volume(value/100)

def set_window(value,dificulty):
    global dis
    global dis_width, dis_height
    if value[1] == 0:
        dis_width = 1920
        dis_height = 1080
        dis = pygame.display.set_mode((dis_width, dis_height))
        options_menu.resize(dis_width, dis_height)
        menu.resize(dis_width, dis_height)
    if value[1] == 1:
        dis_width = 1280
        dis_height = 720
        dis = pygame.display.set_mode((dis_width, dis_height))
        options_menu.resize(dis_width,dis_height)
        menu.resize(dis_width, dis_height)
    if value[1] == 2:
        dis_width = 800
        dis_height = 480
        dis = pygame.display.set_mode((dis_width, dis_height))
        options_menu.resize(dis_width, dis_height)
        menu.resize(dis_width, dis_height)
def set_background(value,dificulty):
    global background_image
    if value[1] == 1:
        background_image = pygame.image.load('backgrond-image.jpg')
def viewTable():
    while True:
        height = 2.5
        dis.blit(background_image, (0, 0))
        value = score_font.render("Таблица результатов: ", True, yellow, red)
        dis.blit(value, [dis_width / 4.5, dis_height / 9])
        value = score_font.render("№ Имя Счет Режим ", True, yellow, green)
        dis.blit(value, [dis_width / 4.5, dis_height / 6])
        with open("table_score.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                mesg = font_style.render(line.split('\n')[0], True, yellow, red)
                dis.blit(mesg, [dis_width / 4.5, dis_height / 4.5 + height])
                height += 40
        for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     menu.enable()
                     menu.mainloop(dis)
                     break
        pygame.display.update()

def set_difficulty(value,dificulty):
    global snake_speed
    global dif
    dif= value[0][0]
    print(value)
    if value[0][1] == 2:
        snake_speed = 25
    if value[0][1] == 1:
        snake_speed = 50
def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow, red)
    dis.blit(value, [0, 0])
def food():
    list_food =[]
    for i in range(2):
        coordinates = []
        coordinates.append(random.randrange(snake_block*4, dis_width - snake_block,snake_block))
        coordinates.append(random.randrange(snake_block*2, dis_height - snake_block,snake_block))
        list_food.append(coordinates)
    return list_food

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def barrier():
    x=(random.randrange(snake_block * 4, dis_width - snake_block, snake_block))
    y=(random.randrange(snake_block * 2, dis_height - snake_block,snake_block))
    return [x,y]
def tableScore(Len_of_snake):
    global user_name
    global dif
    check = False
    table_score.clear()
    with open("table_score.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            table_score.append((line.split('\n')[0]))
        print(table_score)
        table_score.sort(key=lambda i: int(i.split()[2]), reverse=True)
    for i in range(len(table_score)):
        if user_name.get_value() == (table_score[i].split())[1]:
            if Len_of_snake >= int(table_score[i].split()[2]):
                table_score[i] = str(table_score[i].split()[0][0]) + ") " +str(user_name.get_value() + " " + str(Len_of_snake) + " "+ str(dif))
            check = True
    if not check:
        table_score.append(str(int(table_score[-1].split()[0][0]) + 1) + ") " +str(user_name.get_value() + " " + str(Len_of_snake) + " "+ str(dif)))
    table_score.sort(key = lambda i: int(i.split()[2]), reverse= True)
    for i in range(len(table_score)):
        splited = table_score[i].split()
        splited[0] = str(i+1) + ')'
        table_score[i] = ''
        for j in splited:
            table_score[i] +=   j + ' '
        print(splited)
    with open('table_score.txt', 'w',encoding="utf-8") as f:
        for line in table_score:
            f.write(line+ '\n')
def message(msg, color):
    height = 2.5
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width /4.5  , dis_height / 5])
    value = score_font.render("Таблица результатов: ", True, yellow, red)
    dis.blit(value, [dis_width /4.5  , dis_height / 3.5])
    value = score_font.render("№ Имя Счет Режим ", True, yellow, green)
    dis.blit(value, [dis_width / 4.5, dis_height / 3])
    for i in table_score:
        mesg = font_style.render(i, True, yellow, red)
        dis.blit(mesg, [dis_width / 4.5, dis_height/2.5 + height])
        height += 40

def gameLoop():
    game_over = False
    game_close = False
    x1 = random.randrange(0, dis_width - snake_block, snake_block)
    y1 = random.randrange(0, dis_height - snake_block, snake_block)
    x1_change = 0
    y1_change = 0
    file_work = False
    snake_List = []
    list_barrier = barrier()
    Length_of_snake = 1
    list_food = food()
    while not game_over:
        dis.blit(background_image, (0, 0))
        while game_close == True:
            dis.blit(background_image, (0, 0))
            if not file_work:
                tableScore(Length_of_snake-1)
            file_work = True
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:
                        menu.enable()
                        menu.mainloop(dis)
                        break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        pygame.draw.rect(dis, green, [list_food[0][0], list_food[0][1], snake_block, snake_block])
        pygame.draw.rect(dis, green, [list_food[1][0], list_food[1][1], snake_block, snake_block])
        pygame.draw.rect(dis, red, [list_barrier[0], list_barrier[1], snake_block, snake_block*5])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if  (list_barrier[0] - snake_block < x1 < list_barrier[0] + snake_block ) and list_barrier[1] <= y1 < list_barrier[1] + snake_block*5:
           game_close = True
        for eat in list_food:
            if eat[0] == x1 and eat[1]==y1:
                eat[0] = random.randrange(0, dis_width - snake_block, snake_block)
                eat[1] = random.randrange(0, dis_height - snake_block, snake_block)
                Length_of_snake +=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
def optionsMenu():
    options_menu.add.button('Back', options_menu.disable, font_size=60, padding=(0, 20))
    options_menu.add.range_slider("Music Volume", 50, (0, 100), 1, onchange=music_volume, font_size=60)
    options_menu.add.selector('Background image :', [('Standart', 2), ('New', 1)], onchange=set_background,
                              font_size=60,
                              padding=(0, 20))
    options_menu.add.selector('Window size :', [('1920x1080', 2), ('1280x720', 1), ('800x480', 0)], onchange=set_window,
                              font_size=60,
                              padding=(0, 20))

# ------------main-------------
user_name = menu.add.text_input('Name :', default='Имя', font_size=60, padding=(0, 20))
menu.add.selector('Difficulty :', [('Easy', 2), ('Hard', 1)], onchange=set_difficulty, font_size=60,
                  padding=(0, 20))
menu.add.button('Play', gameLoop, font_size=60, padding=(0, 20))
menu.add.button('Results Table', viewTable, font_size=60, padding=(0, 20))
menu.add.button('Options', options, font_size=60, padding=(0, 20))
menu.add.button('Quit', pygame_menu.events.EXIT, font_size=60, padding=(0, 20))
optionsMenu()       
menu.mainloop(dis)
