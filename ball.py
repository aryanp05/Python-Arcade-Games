77% of storage used … If you run out, you can't create, edit and upload files. Get 100 GB of storage for $2.79 $0.69/month for 3 months.
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def put_textA(text, font, surface):
    text = font.render(text, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (100, 70)
    surface.blit(text, text_rect)

def put_textA2(text, font, surface):
    text = font.render(text, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (225, 70)
    surface.blit(text, text_rect)

def put_textS(text, font, surface):
    text = font.render(text, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (131, 20)
    surface.blit(text, text_rect)

def put_textS2(text, font, surface):
    text = font.render(text, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (215, 20)
    surface.blit(text, text_rect)

class Clicker:
    def __init__(self) -> None:
        pass
clicks = 1
score = 0
accuracy = ((score/clicks)*100)
pygame.init()
clock = pygame.time.Clock()

# window setup
screen_width = 1280
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


font = pygame.font.SysFont('comicsans',  40)

while True:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # logic

    # drawing
    screen.fill((0, 0, 0))


    put_textA(str("Accuracy: "), font, screen)
    put_textA2(str(accuracy), font, screen)
    put_textS(str("Score: "), font, screen)
    put_textS2(str(score), font, screen)
    # update screen
    pygame.display.flip()
    clock.tick(60)
