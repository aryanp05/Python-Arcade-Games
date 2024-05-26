import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Ball:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = Vector2D(random.choice([-1, 1]), random.choice([-1, 1]))

    def move(self, screen_width, screen_height):
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.direction.x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.direction.y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), self.radius)

    def reset_position(self, screen_width, screen_height):
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)

    def is_clicked(self, mouse_pos):
        return (self.x - mouse_pos[0]) ** 2 + (self.y - mouse_pos[1]) ** 2 < self.radius ** 2

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def put_text(text, font, surface, center):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=center)
    surface.blit(text_surface, text_rect)

class Clicker:
    def __init__(self):
        self.clicks = 0
        self.score = 0

    @property
    def accuracy(self):
        return (self.score / self.clicks) * 100 if self.clicks > 0 else 0

    def increment_clicks(self):
        self.clicks += 1

    def increment_score(self):
        self.score += 1
        self.increment_clicks()

clicker = Clicker()

pygame.init()
clock = pygame.time.Clock()

# window setup
screen_width = 1280
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Click the Ball')

font = pygame.font.SysFont('comicsans', 40)

ball = Ball(random.randint(50, screen_width - 50), random.randint(50, screen_height - 50), 20, 5)

running = True
while running:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ball.is_clicked(event.pos):
                clicker.increment_score()
                ball.reset_position(screen_width, screen_height)
            else:
                clicker.increment_clicks()

    # logic
    ball.move(screen_width, screen_height)

    # drawing
    screen.fill(BLACK)
    ball.draw(screen)
    put_text(f"Accuracy: {clicker.accuracy:.2f}%", font, screen, (200, 70))
    put_text(f"Score: {clicker.score}", font, screen, (200, 20))

    # update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
