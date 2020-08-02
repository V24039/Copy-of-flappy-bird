import random
import sys
import pygame as pg
import schange

# game var
gravity = 0.4
bird_move = 0
on_off = False  # if game active
start = True  # for start screen
score = 0  # for getting score
h_score = 0  # for holding high score
pos = []  # to check mouse position
l = ["media/images/pipe-green.png", "media/images/background-day.png",
     ['media/images/bluebird-midflap.png','media/images/bluebird-downflap.png','media/images/bluebird-upflap.png'],]  # to store change
a=[0]

def floor_move():
    screen.blit(floor_suf, (floor_x_pos, 700))  # adding two floors
    screen.blit(floor_suf, (floor_x_pos + 576, 700))

def create_pipe():
    ran_pipe_pos = random.choice(pipe_height)  # choosing random hieght from list
    bot_pipe = pipe_suf.get_rect(midtop=(700, ran_pipe_pos))  # creating the rectangle for pipe
    top_pipe = pipe_suf.get_rect(midtop=(700, ran_pipe_pos - 800))
    return bot_pipe, top_pipe

def move_pipes(pipes):  # moves pipes
    for pipe in pipes:  # using the pipe list
        pipe.centerx -= 5  # move it by 5 and create a new list
    return pipes

def draw_pipes(pipes):  # to draw pipes
    for pipe in pipes:  # to draw pipe for ever single pipe in list
        if pipe.bottom >= 700:  # for bottom pipe
            screen.blit(pipe_suf, pipe)
        else:  # for top pipe
            flip_pipe = pg.transform.flip(pipe_suf, False, True)  # x-false y-truw
            screen.blit(flip_pipe, pipe)
    return pipes

def check_col(pipes):  # to check collision
    for pipe in pipes:
        if bird_rect.colliderect(pipe):  # collision with pipe
            hit_son.play()
            for i in range(100000):
                continue
            death_son.play()
            return False
    if bird_rect.top <= -40 or bird_rect.bottom >= 700:  # collision with floor
        hit_son.play()
        for i in range(100):
            continue
        death_son.play()
        return False
    return True

def rotate_bird(bird):  # rotating the bird
    new_bird = pg.transform.rotozoom(bird, bird_move * (-3), 1)  # fun rotozoom
    return new_bird

def bird_anim():
    new_bird = bird_frames[bird_i]
    new_bird_reect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_reect

def score_dis(state):
    if state == 'start':
        score_suf = font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_suf.get_rect(center=(288, 50))
        screen.blit(score_suf, score_rect)
    if state == 'over':
        score_suf = font.render(f'Score: {str(int(score))}', True, (255, 255, 255))
        score_rect = score_suf.get_rect(center=(288, 50))
        screen.blit(score_suf, score_rect)

        h_score_suf = font.render(f'High Score: {str(int(h_score))}', True, (0, 0, 0))
        h_score_rect = h_score_suf.get_rect(center=(288, 680))
        screen.blit(h_score_suf, h_score_rect)

def click(clc):
    l_pipe = ["media/images/pipe-green.png", "media/images/pipe-red.png"]
    l_bg = ["media/images/background-day.png", "media/images/background-night.png"]
    if (499 > clc[0] > 104) and (156 > clc[1] > 100):
        if clc[0] <= 175:
            pass
        if 335 > clc[0] > 265:
            pass
        if clc[0] > 425:
            pass
    if (96 > clc[0] > 44) and (610 > clc[1] > 285):
        l[0] = l_pipe[0]

    if (230 > clc[0] > 174) and (609 > clc[1] > 288):
        l[0] = l_pipe[1]

    if (536 > clc[0] > 295) and (388 > clc[1] > 304):
        l[1] = l_bg[0]

    if (528 > clc[0] > 305) and (590 > clc[1] > 506):
        l[1] = l_bg[1]

def change():
    back = True
    while back :
        for event in pg.event.get():                #event loop
            if event.type == pg.QUIT:               #exit game
                pg.quit()
                sys.exit()                          #exit with no error
            if event.type == pg.MOUSEBUTTONDOWN:
                pos.extend(pg.mouse.get_pos())
                if (39 >= pos[0]) and (40 >= pos[1]):#while loop ends on
                    back = False                     #pressing back button
                else:
                    a.extend(schange.click(pos))
                    l[a[1]] = a[2]
                    a.pop()
                    a.pop()
                    pos.clear()
            screen = pg.display.set_mode((576, 800))
        schange.dis()
        pg.display.update()
        pg.time.Clock().tick(120)  # frame speed

def mouse():
    fin = True
    while fin:
        for event in pg.event.get():  # event loop
            if event.type == pg.QUIT:  # exit game
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos.extend(pg.mouse.get_pos())
                if (410 >= pos[0] >= 142) and (323 <= pos[1] <= 470):
                    pos.clear()
                    fin = False         #ends the loop on pressing start
                elif (450 >= pos[0] >= 115) and (615 <= pos[1] <= 695):
                    pos.clear()
                    change()            # returned from change on pressing back
                else:
                    pos.clear()
        schange.main_screen()           #main screen display from schange till the loop ends

        pg.display.update()
        pg.time.Clock().tick(120)

for i in range(1):
    mouse()

pg.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pg.init()  # initialzing py game
screen = pg.display.set_mode((576, 800))
clock = pg.time.Clock()
font = pg.font.Font('media/04B_19.TTF', 40)

back = pg.transform.scale2x(pg.image.load('media/images/back.png').convert_alpha())  # back button
back_rect = back.get_rect(center=(20, 20))

bg_suf = pg.image.load(l[1]).convert()  # importing image
bg_suf = pg.transform.scale2x(bg_suf)  # rescale the image

pipe_suf = pg.image.load(l[0]).convert()  # importing pipe image
pipe_suf = pg.transform.scale2x(pipe_suf)  # rescale the image

bird_mid = pg.transform.scale2x(pg.image.load(l[2][0]).convert_alpha())  # importing image
bird_down = pg.transform.scale2x(pg.image.load(l[2][1]).convert_alpha())  # importing image
bird_up = pg.transform.scale2x(pg.image.load(l[2][2]).convert_alpha())  # importing image

floor_suf = pg.image.load('media/images/base.png').convert()
floor_suf = pg.transform.scale2x(floor_suf)
floor_x_pos = 0

bird_frames = [bird_down, bird_mid, bird_up]
bird_i = 0  # index
bird = bird_frames[bird_i]
bird_rect = bird.get_rect(center=(100, 350))  # creating a rectangle to check for collision and rotate it
BIRDFLIP = pg.USEREVENT + 1
pg.time.set_timer(BIRDFLIP, 1200)

pipe_list = []
SPAWNPIPE = pg.USEREVENT  # event triggered by timer
pg.time.set_timer(SPAWNPIPE, 1200)  # event triggered after every 1200ms
pipe_height = [300, 450, 345, 500, 320, 290, 400, 600]  # position of pipe

set_game = pg.transform.scale2x(pg.image.load('media/images/settings.png').convert_alpha())
set_rect = set_game.get_rect(center=(550, 29))

game_over = pg.transform.scale2x(pg.image.load('media/images/gameover.png').convert_alpha())  # importing image
game_over_rect = game_over.get_rect(center=(280, 350))

game_suf = pg.transform.scale2x(pg.image.load('media/images/message.png').convert_alpha())
game_suf_rect = game_suf.get_rect(center=(280, 350))

flap_son = pg.mixer.Sound('media/audio/wing.wav')
hit_son = pg.mixer.Sound('media/audio/hit.wav')
death_son = pg.mixer.Sound('media/audio/die.wav')
score_son = pg.mixer.Sound('media/audio/point.wav')
score_son_count = 1

while 1:
    for event in pg.event.get():  # event loop
        if event.type == pg.QUIT:  # exit game
            pg.quit()
            sys.exit()  # exit with no error

        if event.type == pg.MOUSEBUTTONDOWN:
            pos.extend(pg.mouse.get_pos())
            if (39 >= pos[0]) and (40 >= pos[1]):
                pos.clear()
                mouse()
            else:
                pos.clear()

        if event.type == pg.KEYDOWN:  # checks keyboard interrupt
            if (event.key == pg.K_SPACE or event.key == pg.K_UP) and on_off:  # for jumping the bird by user
                bird_move = 0
                bird_move -= 8
                flap_son.play()

            if event.key == pg.K_SPACE and on_off == False:
                start = False
                on_off = True
                pipe_list.clear()
                bird_rect.center = (100, 350)
                bird_move = 0
                score = 0

        if event.type == SPAWNPIPE and on_off == True:  # creates a pipe after every spawnpipe event
            pipe_list.extend(create_pipe())  # extend bcoz tuple
            score += 1
            score_son_count -= 1

        if event.type == BIRDFLIP:  # animating bird flip
            if bird_i < 2:
                bird_i += 1
            else:
                bird_i = 0
            bird, bird_rect = bird_anim()

    screen.blit(bg_suf, (0, 0))  # display background screen

    if on_off:
        bird_move += gravity  # BIRD
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_move  # to the bird
        screen.blit(rotated_bird, bird_rect)  # bird display
        on_off = check_col(pipe_list)

        score_dis('start')

        if score > h_score:
            h_score = score
        if score_son_count <= 0:
            score_son.play()
            score_son_count = 1
        pipe_list = move_pipes(pipe_list)  # moving rectangles
        draw_pipes(pipe_list)

    else:
        if start == False:
            screen.blit(game_over, game_over_rect)
        else:
            screen.blit(game_suf, game_suf_rect)
            #screen.blit(back, back_rect)
        score_dis('over')

    floor_x_pos -= 1  # dec x of floor so that the image moves left
    floor_move()
    if floor_x_pos <= -576:  # after 2nd floor x is -576
        floor_x_pos = 0  # set the x to 0 so that they are back at start pos

    pg.display.update()
    pg.time.Clock().tick(120)  # frame speed