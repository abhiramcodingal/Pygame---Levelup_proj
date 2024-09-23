#Collision of Sprites - for 5 times to win the game

import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
SPR_COL_CHANGE = pygame.USEREVENT + 1
BLUE = pygame.Color(0,0,255)
RED = pygame.Color(255,0,0)
GREEN = pygame.Color(0,250,0)
YELLOW = pygame.Color(255,255,0)
PINK = pygame.Color(255,0,255)
PURPLE = pygame.Color(170,0,170)

pygame.init()
pygame.mixer.init()

bg_image = pygame.transform.scale(pygame.image.load("bg.png"),(SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('darkblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    
    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision of Sprites")
all_sprites = pygame.sprite.Group()

spr1 = Sprite(random.choice([BLUE,RED,GREEN,YELLOW,PINK,PURPLE]), 20, 30)
spr1.rect.x = random.randint(0, SCREEN_WIDTH - spr1.rect.width)
spr1.rect.y = random.randint(0, SCREEN_HEIGHT - spr1.rect.height)
all_sprites.add(spr1)
spr2 = Sprite(random.choice([BLUE,RED,GREEN,YELLOW,PINK,PURPLE]), 20, 30)
spr2.rect.x = random.randint(0, SCREEN_WIDTH - spr2.rect.width)
spr2.rect.y = random.randint(0, SCREEN_HEIGHT - spr2.rect.height)
all_sprites.add(spr2)

running, won = True, False
count = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPR_COL_CHANGE:
            spr1.image.fill(random.choice([BLUE,RED,YELLOW,GREEN,PINK,PURPLE]))
            spr2.image.fill(random.choice([BLUE,RED,YELLOW,GREEN,PINK,PURPLE]))
    if count < 6:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        spr1.move(x_change, y_change)
        if spr1.rect.colliderect(spr2.rect):
            won = True
            count += 1
            print(count)
            pygame.event.post(pygame.event.Event(SPR_COL_CHANGE))
            spr2.rect.x = random.randint(0, SCREEN_WIDTH - spr2.rect.width)
            spr2.rect.y = random.randint(0, SCREEN_HEIGHT - spr2.rect.height)
    screen.blit(bg_image, (0,0))
    all_sprites.draw(screen)
    if count == 6:
        win_text = font.render("You win", True, pygame.Color('black'))
        screen.blit(win_text, (130,200))
        pygame.mixer.music.load("scc.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
        pygame.event.wait()
    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()  