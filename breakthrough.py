77% of storage used … If you run out, you can't create, edit and upload files. Get 100 GB of storage for $2.79 $0.69/month for 3 months.
import pygame 
import random
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Paddle:
    def __init__(self, x, y, width, height, speed, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Player(Paddle):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(x, y, width, height, speed, color)
        self.i_speed = speed
        self.speed = 0

    def update(self):
        self.rect.x += self.speed


class Ball:

    def __init__(self, size, x, y, speed, color):
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.color = color
        self.x = x
        self.y = y

    def update(self, screen_width, screen_height, player):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed.y *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed.x *= -1

        if self.rect.colliderect(player.rect):
            self.speed.y *= -1
      
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Block:
    def __init__(self, x, y, width, height, color, isDead):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isDead = isDead
        self.isDead = False
    
    def update(self, ball):
        if (self.isDead == False):
            if ball.rect.colliderect(self.rect):
                #ball.speed.y *= -1
                #ball.speed.x *= -1
                self.isDead = True

    def draw(self, surface):
        if (self.isDead == False):
            pygame.draw.rect(surface, self.color, self.rect)

pygame.init()
clock = pygame.time.Clock()

# window setup
screen_width = 1281
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = Ball(10, screen_width / 2 - 5, screen_height /
            2 - 5, Vector2D(4, 4), WHITE)

player = Player(screen_width / 2 - 50, screen_height - 70, 150, 10, 15, WHITE)

blocks = []
ChangeX = 125
ChangeY = -75
x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4]

for d in y:
    for c in x:
        blocks.append(Block(28 + (c*ChangeX), (screen_height / 2 + 25) + (d*ChangeY), 100, 50, RED, False))


while True:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed -= abs(player.i_speed)
            if event.key == pygame.K_RIGHT:
                player.speed += abs(player.i_speed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speed += abs(player.i_speed)
            if event.key == pygame.K_RIGHT:
                player.speed -= abs(player.i_speed)
    if ball.rect.bottom >= screen_height:
        pygame.quit()
    # logic
    player.update()
    ball.update(screen_width, screen_height, player)
    for block in blocks:
        block.update(ball)
    # drawing
    screen.fill(BLACK)

    ball.draw(screen)
    player.draw(screen)
    for block in blocks:
        block.draw(screen)


    # update screen
    pygame.display.flip()
    clock.tick(60)
