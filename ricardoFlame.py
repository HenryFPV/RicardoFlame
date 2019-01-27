import pygame, time, random
from pygame.locals import *

pg = pygame
pg.init()

pg.display.set_caption('Ricardo Flame')
algust = pg.image.load("png/avaekraan1.png")
loppt = pg.image.load("png/endscreen.png")
ladu = pg.image.load("png/keskekraan.png")
#voitekr = pg.image.load("png/v6itja.png")

backgroundRect = algust.get_rect()
muusika = pg.mixer.music.load

BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
BRIGHTGREEN = (34,139,34)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 899
SCREEN_HEIGHT = 599

halfWinHeight = SCREEN_HEIGHT / 2
halfWinWIDTH = SCREEN_WIDTH / 2

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


def heli_peale():
    pg.mixer.music.play()

def text_objects2(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def text_objects4(text, font):
    textSurface = font.render(text, True, BLUE)
    return textSurface, textSurface.get_rect()


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

        screen.blit(algust, backgroundRect)
     

        button("DEFEND", 150, 475, 200, 50, GREEN, BRIGHTGREEN, "edasi")
        button("U GAY", 550, 475, 200, 50, RED, DARKRED, "quit")


        pg.display.update()

        clock.tick(0)


def keskmine():
    keskmine = True

    while keskmine:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(ladu, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects4("liiguta ennast nooltega", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT - 100))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects4("FAIAAAR tühikuga", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 160))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects4("Ära lase ennast vee poolt heteroks muuta", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 220))
        screen.blit(TextSurf, TextRect)

        pg.display.update()

        time.sleep(4)

        muusika('sound\starting sound.mp3')
        heli_peale()

        time.sleep(1.2)

        clock.tick(0)

        pela()
########################################################
def winn():
    winn = True

    while winn:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit

        screen.blit(voitekr, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects4("U stayed gay, well done!", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 3))
        screen.blit(TextSurf, TextRect)

        button("GG!", 350, 400, 200, 50, RED, DARKRED, "quit")

        pg.display.update()

        clock.tick(0)
########################################################

def outro():
    outro = True

    muusika('sound\krediit.mp3')
    heli_peale()

    while outro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(loppt, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects4("Delta ehitis d282.56.2", largeText)
        TextRect.center = (600, 585)
        screen.blit(TextSurf, TextRect)

        button("GET WELL!", 350, 400, 200, 50, RED, DARKRED, "quit")

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
    textRect.midtop = (x-390, y)

    surf.blit(textSurf, textRect)


class Player(pg.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pg.Surface([56, 79])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
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

        bullet = Bullet(self.rect.centerx, self.rect.bottom - 25)
        all_sprite_list.add(bullet)
        bullets.add(bullet)

class Bullet(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 19))
        self.image = pg.image.load("png\kuul1.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedy

        if self.rect.bottom < 0:
            self.kill()



class Mob(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((60, 1000))
        self.image = pg.image.load("png\enemy1.png")
        self.image = pg.transform.scale(self.image, [60, 100])

        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 500

        self.speedx = random.randrange(-5, -2)

    def update(self):
        self.rect.x += self.speedx

        if self.rect.top > self.rect.left < -60 or self.rect.right > SCREEN_WIDTH + 60:
            self.rect.x = random.randrange(899, 1000)
            self.rect.y = random.randrange(40, 550)
            self.speedy = random.randrange(-7, -5)


class Wall(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


all_sprite_list = pg.sprite.Group()
mobs = pg.sprite.Group()
bullets = pg.sprite.Group()
wall_list = pg.sprite.Group()

bg = Background("png\playarea.jpg", [0, 0])
bg.image = pg.image.load("png\playarea.jpg")
all_sprite_list.add(bg)

wall = Wall(0, 600, 900, 0)
wall_list.add(wall)
all_sprite_list.add(wall)

player = Player(10, 150)
player.image = pg.image.load("png\player1.png")
player.walls = wall_list

wall = Wall(0, 0, 900, 0)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(900, 0, 0, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 0, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

for i in range(10):
    m = Mob()
    all_sprite_list.add(m)
    mobs.add(m)

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

                    muusika('sound\shooot.mp3')
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

        pihtas = pygame.sprite.groupcollide(mobs, bullets, True, True)

        for piht in pihtas:
            muusika('sound\sliderbar.wav')
            heli_peale()

            skoor += 1

            m = Mob()
            all_sprite_list.add(m)
            mobs.add(m)


        kadunud = pg.sprite.spritecollide(player, mobs, False)

        if kadunud:
            muusika('sound\oof.mp3')
            heli_peale()

            time.sleep(1.2)
            outro()

        all_sprite_list.draw(screen)

        score(screen, str(skoor), 30, 450, 60)

        pg.display.flip()

        clock.tick(60)
        if str(skoor) == 15:
            winn()


#   if str(skoor) == 15:
#       winn()
#      done = True





intro()

pg.quit()
