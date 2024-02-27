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
        self.rect.y += self.speed

class Enemy(Paddle):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(x, y, width, height, speed, color)

    def update(self, ball):
        self.rect.y = (ball.rect.top + ball.rect.height / 2) - \ 
            (self.rect.height / 2) 

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
            self.speed.x *= -1
      
    def draw(self, surface):
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

player = Player(50, screen_height / 2, 10, 150, 15, WHITE)

enemy = Enemy(screen_width - 50, screen_height / 2, 10, 150, 15, WHITE)

while True:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed -= abs(player.i_speed)
            if event.key == pygame.K_DOWN:
                player.speed += abs(player.i_speed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speed += abs(player.i_speed)
            if event.key == pygame.K_DOWN:
                player.speed -= abs(player.i_speed)
    # logic
    player.update()
    ball.update(screen_width, screen_height, player)
    enemy.update(ball)
  
    # drawing
    screen.fill(BLACK)

    ball.draw(screen)
    player.draw(screen)
    enemy.draw(screen)


    # update screen
    pygame.display.flip()
    clock.tick(60)
