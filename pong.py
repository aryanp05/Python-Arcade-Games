import pygame 
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

    def update(self, screen_height):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

class Enemy(Paddle):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(x, y, width, height, speed, color)

    def update(self, ball, screen_height):
        if ball.rect.centery > self.rect.centery and self.rect.bottom < screen_height:
            self.rect.y += self.speed
        if ball.rect.centery < self.rect.centery and self.rect.top > 0:
            self.rect.y -= self.speed

class Ball:
    def __init__(self, size, x, y, speed, color):
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.color = color
        self.game_over = False
        self.winner = None

    def update(self, screen_width, screen_height, player, enemy):
        if self.game_over:
            return

        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed.y *= -1
        if self.rect.left <= 0:
            self.game_over = True
            self.winner = "YOU LOSE"
        if self.rect.right >= screen_width:
            self.game_over = True
            self.winner = "YOU WIN"

        if self.rect.colliderect(player.rect) or self.rect.colliderect(enemy.rect):
            self.speed.x *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

pygame.init()
clock = pygame.time.Clock()

# window setup
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = Ball(10, screen_width // 2 - 5, screen_height // 2 - 5, Vector2D(4, 4), WHITE)
player = Player(50, screen_height // 2 - 75, 10, 150, 8, WHITE)
enemy = Enemy(screen_width - 60, screen_height // 2 - 75, 10, 150, 8, WHITE)

font = pygame.font.Font(None, 74)
running = True
while running:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed = -player.i_speed
            if event.key == pygame.K_DOWN:
                player.speed = player.i_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.speed = 0

    # logic
    if not ball.game_over:
        player.update(screen_height)
        ball.update(screen_width, screen_height, player, enemy)
        enemy.update(ball, screen_height)

    # drawing
    screen.fill(BLACK)
    ball.draw(screen)
    player.draw(screen)
    enemy.draw(screen)

    if ball.game_over:
        text = font.render(ball.winner, True, RED if ball.winner == "YOU LOSE" else GREEN)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

    # update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
