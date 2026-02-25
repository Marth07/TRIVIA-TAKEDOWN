import pygame
import sys
import random
from moteur import start_fight
from fighter import Fighter

pygame.init()

# IMAGES
peter_img = pygame.image.load("assets/Personnages/Peter_clean.png")
steve_img = pygame.image.load("assets/Personnages/Steve_clean.png")
nyra_img = pygame.image.load("assets/Personnages/Nyra_clean.png")
brian_img = pygame.image.load("assets/Personnages/Brian_clean.png")

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Takedown - Brain Strikers")

WHITE = (255, 255, 255)
BLUE = (65, 105, 225)

font_title = pygame.font.SysFont("Arial", 80, bold=True)
font_menu = pygame.font.SysFont("Arial", 40)

peter = Fighter("Peter", 150, 500, 120, 15, "Lames", peter_img)
steve = Fighter("Steve", 1100, 500, 100, 20, "Angles", steve_img)
nyra = Fighter("Nyra", 150, 500, 150, 10, "Boucliers", nyra_img)
brian = Fighter("Brian", 1100, 500, 80, 25, "Frappe", brian_img)

characters = [peter, steve, nyra, brian]


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x - img.get_width() // 2, y))


def select_character():
    running = True
    positions = [
        (WIDTH // 4 - 100, HEIGHT // 2 - 200),
        (3 * WIDTH // 4 - 100, HEIGHT // 2 - 200),
        (WIDTH // 4 - 100, HEIGHT // 2 + 50),
        (3 * WIDTH // 4 - 100, HEIGHT // 2 + 50),
    ]

    boxes = [pygame.Rect(x, y, 200, 200) for x, y in positions]

    while running:
        screen.fill((20, 20, 40))
        draw_text("CHOISIS TON COMBATTANT", font_title, BLUE, WIDTH // 2, 80)

        mouse = pygame.mouse.get_pos()

        for i, rect in enumerate(boxes):
            char = characters[i]
            color = BLUE if rect.collidepoint(mouse) else WHITE
            pygame.draw.rect(screen, color, rect, 3)

            char_img = pygame.transform.scale(char.image, (180, 180))
            screen.blit(char_img, (rect.x + 10, rect.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(boxes):
                    if rect.collidepoint(mouse):
                        return characters[i]

        pygame.display.update()


def main_menu():
    while True:
        screen.fill((15, 15, 35))

        draw_text("TRIVIA TAKEDOWN", font_title, BLUE, WIDTH // 2, 100)
        draw_text("Par Brain Strikers", font_menu, WHITE, WIDTH // 2, 180)

        mouse = pygame.mouse.get_pos()

        options = [("COMBATTRE (1v1)", 300), ("QUITTER", 380)]
        buttons = []

        for text, y in options:
            hovered = (
                WIDTH // 2 - 150 < mouse[0] < WIDTH // 2 + 150 and y < mouse[1] < y + 50
            )
            color = BLUE if hovered else WHITE
            draw_text(text, font_menu, color, WIDTH // 2, y)
            buttons.append(pygame.Rect(WIDTH // 2 - 150, y, 300, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(mouse):
                    player = select_character()
                    enemy = random.choice([c for c in characters if c != player])
                    start_fight(player, enemy)

                if buttons[1].collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
