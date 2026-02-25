import pygame
import sys
from fighter import Fighter

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trivia Takedown - Combat")

clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

image_bg = pygame.image.load("assets/montagne bg.jpg")


def draw_background():
    scaled_bg = pygame.transform.scale(image_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400 * ratio, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


def start_fight(player, enemy):
    run = True

    while run:
        clock.tick(FPS)
        draw_background()

        draw_health_bar(player.health, 20, 20)
        draw_health_bar(enemy.health, 860, 20)

        player.move(screen, enemy)
        enemy.move(screen, player)

        player.draw(screen)
        enemy.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
