import pygame
import random
import sys


pygame.init()
screen = pygame.display.set_mode((1001, 801))
pygame.display.set_icon(pygame.image.load('png/icon.png'))
pygame.display.set_caption('Color Visual Memory')

bg_surface = pygame.image.load('png/grid.png')
[red, blue, green] = [pygame.image.load('png/red.png').convert_alpha(),
                      pygame.image.load('png/blue.png').convert_alpha(),
                      pygame.image.load('png/green.png').convert_alpha()]
next_button = pygame.image.load('png/next.png')
next_button_rect = next_button.get_rect()
[next_button_rect.x, next_button_rect.y] = [820, 704]

start_button = pygame.image.load('png/start.png')
start_button_rect = start_button.get_rect()
[start_button_rect.x, start_button_rect.y] = [380, 350]

input_box_red = pygame.image.load('png/input_box_red.png').convert_alpha()
input_box_red_rect = input_box_red.get_rect()
[input_box_red_rect.x, input_box_red_rect.y] = [900, 38]

input_box_green = pygame.image.load('png/input_box_green.png').convert_alpha()
input_box_green_rect = input_box_green.get_rect()
[input_box_green_rect.x, input_box_green_rect.y] = [900, 98]

input_box_blue = pygame.image.load('png/input_box_blue.png').convert_alpha()
input_box_blue_rect = input_box_blue.get_rect()
[input_box_blue_rect.x, input_box_blue_rect.y] = [900, 158]

[red_box, blue_box, green_box] = [False, False, False]

[level, life] = [1, 3]
[red_count, blue_count, green_count] = [0, 0, 0]
[player_red_count, player_blue_count, player_green_count] = [0, 0, 0]
[run, game_active, game_active2, menu] = [True, False, False, True]


def random_cord():
    global list_cord
    cord = random.choice(list_cord)
    list_cord.pop(list_cord.index(cord))
    return cord


def random_color():
    global red_count, blue_count, green_count
    color = random.choice([red, green, blue])
    if color == red:
        red_count += 1
    if color == green:
        green_count += 1
    if color == blue:
        blue_count += 1
    return color


def level_function():
    global level
    for i in range(level):
        screen.blit(random_color(), random_cord())
    if level < 64:
        level += 1


def active_input_box():
    global input_box_red, input_box_green, input_box_blue
    if red_box:
        input_box_red = pygame.image.load('png/input_box_red_active.png')
        input_box_green = pygame.image.load('png/input_box_green.png').convert_alpha()
        input_box_blue = pygame.image.load('png/input_box_blue.png').convert_alpha()

    if green_box:
        input_box_green = pygame.image.load('png/input_box_green_active.png').convert_alpha()
        input_box_red = pygame.image.load('png/input_box_red.png').convert_alpha()
        input_box_blue = pygame.image.load('png/input_box_blue.png').convert_alpha()

    if blue_box:
        input_box_blue = pygame.image.load('png/input_box_blue_active.png').convert_alpha()
        input_box_red = pygame.image.load('png/input_box_red.png').convert_alpha()
        input_box_green = pygame.image.load('png/input_box_green.png').convert_alpha()


def draw_hearts():
    global life
    heart = pygame.image.load('png/heart.png').convert_alpha()
    for i in range(life):
        screen.blit(heart, (830 + (i*50), 220))


# game logic
while run:
    while game_active:
        list_cord = [(1, 1), (101, 1), (201, 1), (301, 1), (401, 1), (501, 1), (601, 1), (701, 1),
                     (1, 101), (101, 101), (201, 101), (301, 101), (401, 101), (501, 101), (601, 101), (701, 101),
                     (1, 201), (101, 201), (201, 201), (301, 201), (401, 201), (501, 201), (601, 201), (701, 201),
                     (1, 301), (101, 301), (201, 301), (301, 301), (401, 301), (501, 301), (601, 301), (701, 301),
                     (1, 401), (101, 401), (201, 401), (301, 401), (401, 401), (501, 401), (601, 401), (701, 401),
                     (1, 501), (101, 501), (201, 501), (301, 501), (401, 501), (501, 501), (601, 501), (701, 501),
                     (1, 601), (101, 601), (201, 601), (301, 601), (401, 601), (501, 601), (601, 601), (701, 601),
                     (1, 701), (101, 701), (201, 701), (301, 701), (401, 701), (501, 701), (601, 701), (701, 701)]
        [red_text, green_text, blue_text] = ['0', '0', '0']
        screen.blit(bg_surface, (0, 0)), level_function(), pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
        print(red_count, green_count, blue_count)  # delete line for no cheat
        pygame.time.delay(3000)
        game_active, game_active2 = False, True

    while game_active2:
        screen.blit(bg_surface, (0, 0)), screen.blit(next_button, next_button_rect)
        screen.blit(input_box_red, input_box_red_rect), screen.blit(input_box_green, input_box_green_rect)
        screen.blit(input_box_blue, input_box_blue_rect), active_input_box(), draw_hearts()

        level_surface = pygame.font.SysFont('arial', 30).render('LEVEL  ' + str(level - 1), True, (0, 0, 0))
        screen.blit(level_surface, (830, 652))

        red_text_surface = pygame.font.SysFont('arial', 20).render(red_text, True, (0, 0, 0))
        screen.blit(red_text_surface, (910, 45))
        green_text_surface = pygame.font.SysFont('arial', 20).render(green_text, True, (0, 0, 0))
        screen.blit(green_text_surface, (910, 105))
        blue_text_surface = pygame.font.SysFont('arial', 20).render(blue_text, True, (0, 0, 0))
        screen.blit(blue_text_surface, (910, 165))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
            if input_box_red_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                [red_box, green_box, blue_box] = [True, False, False]
            if input_box_green_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                [red_box, green_box, blue_box] = [False, True, False]
            if input_box_blue_rect.collidepoint((pygame.mouse.get_pos())) and event.type == pygame.MOUSEBUTTONDOWN:
                [red_box, green_box, blue_box] = [False, False, True]
            if event.type == pygame.KEYDOWN and red_box:
                if event.key == pygame.K_BACKSPACE:
                    red_text = red_text[:-1]
                elif len(red_text) < 4:
                    red_text += event.unicode
            if event.type == pygame.KEYDOWN and green_box:
                if event.key == pygame.K_BACKSPACE:
                    green_text = green_text[:-1]
                elif len(green_text) < 4:
                    green_text += event.unicode
            if event.type == pygame.KEYDOWN and blue_box:
                if event.key == pygame.K_BACKSPACE:
                    blue_text = blue_text[:-1]
                elif len(blue_text) < 4:
                    blue_text += event.unicode

        if next_button_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            if len(red_text) == 0 or len(blue_text) == 0 or len(green_text) == 0:  # Empty textbox
                pass
            if red_text.isdigit() is False or green_text.isdigit() is False or blue_text.isdigit() is False:  # alphabet
                pass
            elif int(red_text) == int(red_count) and int(green_text) == int(green_count) and int(blue_text) == int(blue_count):
                [game_active2, game_active, red_count, green_count, blue_count] = [False, True, 0, 0, 0]
                pass
            else:
                if life > 1:
                    life -= 1
                    level -= 1
                    [game_active2, game_active, red_count, green_count, blue_count] = [False, True, 0, 0, 0]
                    
                else:
                    [game_active2, game_active, menu, red_count, green_count, blue_count] = [False, False, True, 0, 0, 0]
                    

    while menu:
        screen.fill('black')
        screen.blit(start_button, start_button_rect)
        high_score = level - 2
        with open('high_score.txt', 'r+') as f:
            if high_score > int(f.read()):
                f.seek(0)
                f.write(str(high_score))
            f.seek(0)
            highest_score = f.read()
        highest_score_surface = pygame.font.SysFont('arial', 40).render('Highest Score:  ' + str(highest_score), True, (
            255, 255, 255))
        screen.blit(highest_score_surface, (345, 550))
        for event in pygame.event.get():
            if start_button_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                game_active, game_active2, menu = True, False, False
                [level, life] = [1, 3]
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
        pygame.display.update()
