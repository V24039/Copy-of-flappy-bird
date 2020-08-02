import pygame as pg

pg.init()
screen = pg.display.set_mode((576, 800))
sfont = pg.font.Font('media/04B_19.TTF', 100)

back = pg.transform.scale2x(pg.image.load('media/images/back.png').convert_alpha())  #back button
back_rect = back.get_rect(center=(20, 20))

def dis():

    bg_suf = pg.image.load('media/images/background-day.png').convert()  # importing image
    bg_suf = pg.transform.scale2x(bg_suf)  # rescale the image
    screen.blit(bg_suf, (0, 0))

    option.bird(0)
    option.pipe(0)
    option.b_g(0)
    screen.blit(back, back_rect)

class option:

    def bird(self):
        bird_red = pg.transform.scale2x(pg.image.load('media/images/redbird-midflap.png').convert_alpha())  # importing image
        bird_rect_red = bird_red.get_rect(center=(140, 130))  # creating a rectangle to check for collision and rotate it
        screen.blit(bird_red, bird_rect_red)  # display screen

        bird_yellow = pg.transform.scale2x(pg.image.load('media/images/yellowbird-midflap.png').convert_alpha())  # importing image
        bird_rect_yellow = bird_yellow.get_rect(center=(300, 130))  # creating a rectangle to check for collision and rotate it
        screen.blit(bird_yellow, bird_rect_yellow)  # display screen

        bird_blue = pg.transform.scale2x(pg.image.load('media/images/bluebird-midflap.png').convert_alpha())  # importing image
        bird_rect_blue = bird_blue.get_rect(center=(460, 130))  # creating a rectangle to check for collision and rotate it
        screen.blit(bird_blue, bird_rect_blue)

    def pipe(self):
        pipe_green = pg.image.load('media/images/pipe-green.png').convert() # importing pipe image
        pipe_rect_green = pipe_green.get_rect(center=(70, 450))  # creating a rectangle to check for collision and rotate it
        screen.blit(pipe_green, pipe_rect_green)

        pipe_red = pg.image.load('media/images/pipe-red.png').convert() # importing pipe image
        pipe_rect_red = pipe_red.get_rect(center=(200, 450))  # creating a rectangle to check for collision
        screen.blit(pipe_red, pipe_rect_red)

    def b_g(self):
        bg_day = sfont.render("LIGHT", True, (255, 255, 255))
        bg_rect_day = bg_day.get_rect(center=(420, 350))
        screen.blit(bg_day, bg_rect_day)

        bg_night = sfont.render("DARK", True, (0, 0, 0))
        bg_rect_night = bg_night.get_rect(center=(420, 550))
        screen.blit(bg_night, bg_rect_night)

def main_screen():

    bg_suf = pg.image.load('media/images/background-day.png').convert()  # importing image
    bg_suf = pg.transform.scale2x(bg_suf)  # rescale the image
    screen.blit(bg_suf, (0, 0))

    play_but = pg.image.load('media/images/play.png').convert_alpha()
    play_rect = play_but.get_rect(center = (275,400))  # rescale the image
    screen.blit(play_but, play_rect)

    text = pg.image.load('media/images/title.png').convert_alpha()
    text_rect = text.get_rect(center = (285,150))
    screen.blit(text,text_rect)

    setting_but = pg.image.load('media/images/settingsbutton.png').convert_alpha()
    setting_rect_but = setting_but.get_rect(center = (280,650))  # rescale the image
    screen.blit(setting_but, setting_rect_but)

class img:

    def b_g(l):
        bg_suf = pg.image.load(l[1]).convert()  # importing image
        bg_suf = pg.transform.scale2x(bg_suf)  # rescale the image
    def pipe(l):
        pipe_suf = pg.image.load(l[0]).convert()  # importing pipe image
        pipe_suf = pg.transform.scale2x(pipe_suf)  # rescale the image

def click(clc):
    l_pipe = ["media/images/pipe-green.png", "media/images/pipe-red.png"]
    l_bg = ["media/images/background-day.png", "media/images/background-night.png"]
    l_bird = [['media/images/redbird-midflap.png','media/images/redbird-downflap.png','media/images/redbird-upflap.png'],
              ['media/images/yellowbird-midflap.png','media/images/yellowbird-downflap.png','media/images/yellowbird-upflap.png'],
              ['media/images/bluebird-midflap.png','media/images/bluebird-downflap.png','media/images/yellowbird-upflap.png']]
    if (499 > clc[0] > 104) and (156 > clc[1] > 100):

        if clc[0] <= 175:
            return (2,l_bird[0])
        if 335 > clc[0] > 265:
            return (2,l_bird[1])
        if clc[0] > 425:
            return (2,[l_bird[2]])

    if (96 > clc[0] > 44) and (610 > clc[1] > 285):
        return 0,l_pipe[0]

    if (230 > clc[0] > 174) and (609 > clc[1] > 288):
        return 0,l_pipe[1]

    if (536 > clc[0] > 295) and (388 > clc[1] > 304):
        return 1,l_bg[0]

    if (528 > clc[0] > 305) and (590 > clc[1] > 506):
        return 1,l_bg[1]
