from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (70, 70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def go(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y += self.speed
        if keys[K_DOWN] and self.rect.x < win_height-70:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = "left"

    def go(self):
        if self.rect.x <= 450:
            self.direction = "right"
        if self.rect.x >= win_width - 100:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


win_width = 700
win_height = 500

win = display.set_mode((win_width, win_height))
display.set_caption("Лабіринт")
background = transform.scale(image.load(
    "background.jpg"), (win_width, win_height))

player = GameSprite("hero.png", 10, 10, 410)
monstr = GameSprite("cyborg.png", 1, 550, 260)
gold = GameSprite("treasure.png", 10, 550, 410)

game = True
FPS = 60
clock = time.Clock()

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play
font.init()
font = font.Font(None, 70)
lose = font.render("You LOSE", True, (180, 0, 0))
victory = font.remder("You WIN", True (0, 250, 0))
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        win.blit(background, (0, 0))
        player.draw()
        monstr.draw()
        gold.draw()
        player.do()
        Enemy.go()

        if sprite.collide_rect(player, monstr)
        finish = True
        win.blit(lose, (200, 200))
        if sprite.collide_rect(player, gold)
        finish = True
        win.blit(victory, (200, 200))

    display.update()
    clock.tick(FPS)
