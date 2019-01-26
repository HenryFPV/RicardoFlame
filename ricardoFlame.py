import pygame, time
from pygame.locals import *

pg = pygame
pg.init()

pg.display.set_caption('Ricardo Flame')
#backgroundRect = algust.get_rect()
#Lisa siia koik piltide sissetulekud
muusika = pg.mixer.music.load



BLACK = (0, 0, 0)
WHITE  = (255, 255, 255)
PINK = (255, 20, 147)
BLUE = (50, 50, 255)
GREEN = (102, 205, 0)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
LIGHTGREEN = (0, 255, 0)


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

HALF_WIDTH = SCREEN_WIDTH/2
HALF_HEIGHT = SCREEN_HEIGHT/2


ekraan = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def heli_peale():
    pg.mixer.music.play()

def teksti_asjad1(text, font):
    textSurface = font.render(text, True, Roosa)
    return textSurface, textSurface.get_rect()

def teksti_asjad2(text, font):
    textSurface = font.render(text, True, MUST)
    return textSurface, textSurface.get_rect()

def teksti_asjad3(text, font):
    textSurface = font.render(text, True, PUNANE)
    return textSurface, textSurface.get_rect()

def teksti_asjad4(text, font):
    textSurface = font.render(text, True, SININE)
    return textSurface, textSurface.get_rect()



class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get.rect()
        self.rect.left. self.rect.top = location


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface([])    #paneb siia hiljem need piklsi detailid
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 1
        self.walls = None

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y


    def update(self):
        self.rect.x += self.change_x

        #lisame siia block hit listi
        #peale listi lisame tulistamise


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        




