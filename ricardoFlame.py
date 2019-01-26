import pygame, time, random
from pygame.locals import *

pg = pygame
pg.init()

pg.display.set_caption('Ricardo')
algusekr = pg.image.load("png/algus.png")
loppekr = pg.image.load("png/l6pp.png")
kesk = pg.image.load("png/keskimg.jpg")
backgroundRect = algusekr.get_rect()
muusika = pg.mixer.music.load

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 20, 147)
BLUE = (50, 50, 255)
GREEN = (102, 205, 0)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
BRIGHTRED = (255, 0, 0)
BRIGHTGREEN = (0, 255, 0)

SCREEN_WIDTH = 899
SCREEN_HEIGHT = 599

halfWinHeight = SCREEN_HEIGHT / 2
halfWinWIDTH = SCREEN_WIDTH / 2

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])




def button(msg, x, y, w, h, iv, av, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(screen, av, (x, y, w, h))

        if click[0] == 1 and action != None:
            if action == "quit":
                muusika('sound\key1.wav')
                heli_peale()
                time.sleep(0.5)

                muusika('sound\exit.mp3')
                heli_peale()
                time.sleep(2)

                pg.quit()
                quit

            elif action == "more":
                muusika('sound\key1.wav')
                heli_peale()

                intro()

            elif action == "edasi":
                muusika('sound\key1.wav')
                heli_peale()

                keskmine()

    else:
        pg.draw.rect(screen, iv, (x, y, w, h))
        smallText = pg.font.Font("freesansbold.ttf", 25)

        textSurf, textRect = text_objects2(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))

        screen.blit(textSurf, textRect)


def intro():
    intro = True

    muusika('sound\soliders.mp3')
    heli_peale()

    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(algusekr, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects1("Ricardo The Saviour", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 3))
        screen.blit(TextSurf, TextRect)

        button("Gayen em", 150, 400, 200, 50, GREEN, BRIGHTGREEN, "edasi")
        button("Gay yerself", 550, 400, 200, 50, RED, DARKRED, "quit")

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects1("Based on true events", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 50))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects2("creators: Henry and Martin", largeText)
        TextRect.center = (350, 350)
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects3("Alpha build v0.186", largeText)
        TextRect.center = (100, 585)
        screen.blit(TextSurf, TextRect)

        pg.display.update()

        clock.tick(0)


def keskmine():
    keskmine = True

    while keskmine:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(kesk, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects3("Move with arrow keys!", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects3("erease them with space", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 60))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects3("Dont get turned straight", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 120))
        screen.blit(TextSurf, TextRect)

        pg.display.update()

        time.sleep(4)

        muusika('sound\starting sound.mp3')
        heli_peale()

        time.sleep(1.2)

        clock.tick(0)

        pela()

def heli_peale():
    pg.mixer.music.play()


def text_objects1(text, font):
    textSurface = font.render(text, True, PINK)
    return textSurface, textSurface.get_rect()


def text_objects2(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def text_objects3(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()


def text_objects4(text, font):
    textSurface = font.render(text, True, BLUE)
    return textSurface, textSurface.get_rect()


def outro():
    outro = True

    muusika('sound\krediit.mp3')
    heli_peale()

    while outro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(loppekr, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects4("U failed!", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 3))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects3("U got turned straight", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 30))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects4("gay_build a0112", largeText)
        TextRect.center = (100, 585)
        screen.blit(TextSurf, TextRect)

        button("STRAIGHT", 350, 400, 200, 50, RED, DARKRED, "QUIT")

        pg.display.update()

        clock.tick(0)


class Background(pg.sprite.Sprite):

    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(image_file)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def score(surf, text, size, x, y):
    largeText = pg.font.Font('freesansbold.ttf', size)

    textSurf = largeText.render(text, True, RED)
    textRect = textSurf.get_rect()
    textRect.midtop = (x, y)

    surf.blit(textSurf, textRect)


class Player(pg.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pg.Surface([68, 31])
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

        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left

            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            else:
                self.rect.top = block.rect.bottom

    def shoot(self):

        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprite_list.add(bullet)
        bullets.add(bullet)


class Wall(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Mob(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((60, 1000))
        self.image = pg.image.load("png\rikardoflexx.png")
        self.image = pg.transform.scale(self.image, [60, 100])

        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 470

        self.speedx = random.randrange(-5, -2)

    def update(self):
        self.rect.x += self.speedx

        if self.rect.top > self.rect.left < -60 or self.rect.right > SCREEN_WIDTH + 60:
            self.rect.x = random.randrange(899, 1000)
            self.speedy = random.randrange(-7, -5)


class Bullet(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pg.image.load("png\c4.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()


all_sprite_list = pg.sprite.Group()
mobs = pg.sprite.Group()
bullets = pg.sprite.Group()
wall_list = pg.sprite.Group()

bg = Background("png\bkk.png", [0, 0])
bg.image = pg.image.load("png\bkk.png")
all_sprite_list.add(bg)

for i in range(5):
    m = Mob()
    all_sprite_list.add(m)
    mobs.add(m)

wall = Wall(0, 570, 900, 1)
wall_list.add(wall)
all_sprite_list.add(wall)
wall.image = pg.image.load("png\terrain.png")

wall = Wall(0, 0, 900, 1)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(900, 0, 1, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 1, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

player = Player(10, 150)
player.image = pg.image.load("png\papamilos.png")
player.walls = wall_list

all_sprite_list.add(player)

clock = pg.time.Clock()


def pela():
    skoor = 0
    done = False
    while not done:
        for event in pg.event.get():

            if event.type == pg.QUIT:

                done = True

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT:
                    player.changespeed(-5, 0)

                elif event.key == pg.K_RIGHT:
                    player.changespeed(5, 0)

                elif event.key == pg.K_UP:
                    player.changespeed(0, -5)

                elif event.key == pg.K_DOWN:
                    player.changespeed(0, 5)

                elif event.key == pygame.K_SPACE:

                    muusika('sound\tulista.mp3')
                    heli_peale()
                    player.shoot()

            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    player.changespeed(5, 0)

                elif event.key == pg.K_RIGHT:
                    player.changespeed(-5, 0)

                elif event.key == pg.K_UP:
                    player.changespeed(0, 5)

                elif event.key == pg.K_DOWN:
                    player.changespeed(0, -5)


        all_sprite_list.update()

        katki = pygame.sprite.groupcollide(mobs, bullets, True, True)

        for katk in katki:
            muusika('sound\hitt.wav')
            heli_peale()
            skoor += 1
            m = Mob()
            all_sprite_list.add(m)
            mobs.add(m)
        seeshitt = pg.sprite.spritecollide(player, mobs, False)
        if seeshitt:
            muusika('sound\dead.mp3')
            heli_peale()
            time.sleep(1.2)
            outro()
        all_sprite_list.draw(screen)
        score(screen, str(skoor), 30, 450, 60)
        pg.display.flip()
        clock.tick(60)


intro()

pg.quit()