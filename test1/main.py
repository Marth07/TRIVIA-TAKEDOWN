import pygame
import sys
import random
from moteur import start_fight
from fighter import Fighter

pygame.init()
# Chargement des images
peter_img = pygame.image.load("assets/Personnages/Peter.png")
steve_img = pygame.image.load("assets/Personnages/Steve.png")
nyra_img = pygame.image.load("assets/Personnages/Nyra.png")
brian_img = pygame.image.load("assets/Personnages/Brian.png")


WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Takedown - Brain Strikers")

WHITE = (255, 255, 255)
BLUE = (65, 105, 225)

font_title = pygame.font.SysFont("Arial", 80, bold=True)
font_menu = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 30)

peter = Fighter("Peter", 200, 400, 120, 15, "Lames d'énergie", peter_img)
steve = Fighter("Steve", 400, 400, 100, 20, "Angles et Trajectoires", steve_img)
nyra = Fighter("Nyra", 600, 400, 150, 10, "Boucliers de chiffres", nyra_img)
brian = Fighter("Brian", 800, 400, 80, 25, "Frappe lourde", brian_img)


characters = [peter, steve, nyra, brian]


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x - img.get_width() // 2, y))


def select_character():
    running = True

    positions = [
        (WIDTH // 4 - 100, HEIGHT // 2 - 150),
        (2 * WIDTH // 4 - 100, HEIGHT // 2 - 150),
        (3 * WIDTH // 4 - 100, HEIGHT // 2 - 150),
        (WIDTH // 2 - 100, HEIGHT // 2 + 100),
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

            draw_text(char.name, font_menu, WHITE, rect.centerx, rect.y + 10)
            draw_text(f"HP : {char.hp}", font_small, WHITE, rect.centerx, rect.y + 60)
            draw_text(
                f"Power : {char.power}", font_small, WHITE, rect.centerx, rect.y + 100
            )
            draw_text(char.style, font_small, WHITE, rect.centerx, rect.y + 150)

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
