import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

class Ball:
    def __init__(self, size, x, y, speed, color):
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.color = color

    def update(self, screen_width, screen_height, player, blocks):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed.y *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed.x *= -1

        if self.rect.colliderect(player.rect):
            self.speed.y *= -1

        for block in blocks:
            if not block.isDead and self.rect.colliderect(block.rect):
                block.isDead = True
                self.speed.y *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Block:
    def __init__(self, x, y, width, height, color):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.isDead = False

    def draw(self, surface):
        if not self.isDead:
            pygame.draw.rect(surface, self.color, self.rect)

def put_text(text, font, surface, center):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=center)
    surface.blit(text_surface, text_rect)

pygame.init()
clock = pygame.time.Clock()

# window setup
screen_width = 1281
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Break Through!')

font = pygame.font.SysFont('comicsans', 40)

ball = Ball(10, screen_width / 2 - 5, screen_height / 2 - 5, Vector2D(4, 4), WHITE)
player = Player(screen_width / 2 - 50, screen_height - 70, 150, 10, 15, WHITE)

blocks = []
ChangeX = 125
ChangeY = -75
x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4]

for d in y:
    for c in x:
        blocks.append(Block(28 + (c * ChangeX), (screen_height / 2 + 25) + (d * ChangeY), 100, 50, RED))

running = True
while running:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
                
    # logic
    player.update()
    ball.update(screen_width, screen_height, player, blocks)

    if ball.rect.bottom >= screen_height:
        put_text("YOU LOSE", font, screen, (screen_width / 2, screen_height / 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    if all(block.isDead for block in blocks):
        put_text("YOU WIN", font, screen, (screen_width / 2, screen_height / 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # drawing
    screen.fill(BLACK)
    ball.draw(screen)
    player.draw(screen)
    for block in blocks:
        block.draw(screen)

    # update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
