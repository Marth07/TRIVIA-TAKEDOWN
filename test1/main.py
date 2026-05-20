import copy
import pygame
import sys
import random
import math
import os
from moteur import start_fight, play_menu_music, stop_music
from fighter import Fighter

def get_asset_path(relative_path):
    
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.abspath(".")
    path = os.path.join(base, relative_path)
    if os.path.exists(path):
        return path
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return path

pygame.init()

peter_img = pygame.image.load(get_asset_path("assets/Personnages/Clean/Peter_clean.png"))
steve_img = pygame.image.load(get_asset_path("assets/Personnages/Clean/Steve_clean.png"))
nyra_img = pygame.image.load(get_asset_path("assets/Personnages/Clean/Nyra_clean.png"))
brian_img = pygame.image.load(get_asset_path("assets/Personnages/Clean/Brian_clean.png"))

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Takedown - Brain Strikers")

WHITE = (255, 255, 255)
BLUE = (65, 105, 225)
NYRA_COLOR = (123,  47, 190)
STEVE_COLOR = (255, 127,   0)
PETER_COLOR = (0,  200, 255)
BRIAN_COLOR = (60,  52, 137)

font_title = pygame.font.SysFont(
    ["Orbitron", "Agency FB", "Bahnschrift"], 80, bold=True
)
font_menu = pygame.font.SysFont(["Eurostile", "Consolas", "Bahnschrift"], 38)

peter = Fighter("Peter", 150, 500, 100, 18, 32, "Lames", peter_img, 12)
nyra = Fighter("Nyra", 150, 500, 90, 16, 40, "Boucliers", nyra_img, 7)
brian = Fighter("Brian", 1100, 500, 130, 15, 30, "Frappe", brian_img, 11)
steve = Fighter("Steve", 1100, 500, 110, 20, 35, "Angles", steve_img, 10)

characters = [peter, nyra, brian, steve]

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x - img.get_width() // 2, y))

def select_character():
    running = True
    play_menu_music("main")

    positions = [
        (WIDTH // 4 - 100, HEIGHT // 2 - 200),
        (3 * WIDTH // 4 - 100, HEIGHT // 2 - 200),
        (WIDTH // 4 - 100, HEIGHT // 2 + 50),
        (3 * WIDTH // 4 - 100, HEIGHT // 2 + 50),
    ]

    boxes = [pygame.Rect(x, y, 200, 200) for x, y in positions]

    while running:
        screen.fill((20, 20, 40))
        draw_text("CHOISIS TON COMBATTANT", font_title, BLUE, WIDTH // 2, 60)
        draw_text("PETER", font_menu, PETER_COLOR, WIDTH // 4, HEIGHT // 2)
        draw_text("NYRA", font_menu, NYRA_COLOR, 3 * WIDTH // 4, HEIGHT // 2)
        draw_text("BRIAN", font_menu, BRIAN_COLOR, WIDTH // 4, HEIGHT // 2 + 250)
        draw_text("STEVE", font_menu, STEVE_COLOR, 3 * WIDTH // 4, HEIGHT // 2 + 250)

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

def show_credits():
    running = True
    play_menu_music("credits")

    credits = [
        "",
        "Développé par :",
        "Brain Strikers",
        "",
        "Question :",
        "Marthen Ghoson",
        "",
        "Graphismes :",
        "Hedi Mzali",
        "",
        "Musique et IA:",
        "Vincent Mongobert",
        "",
        "Ecran :",
        "Gloria Essomba",
        "",
        "",
        "Merci d'avoir joué !",
    ]

    y_offset = HEIGHT
    scroll_speed = 0.5

    while running:
        screen.fill((10, 10, 25))

        for i, line in enumerate(credits):
            text_surface = font_menu.render(line, True, WHITE)
            screen.blit(
                text_surface,
                (WIDTH // 2 - text_surface.get_width() // 2, y_offset + i * 60),
            )

        y_offset -= scroll_speed

        if y_offset < -len(credits) * 60:
            draw_text(
                "Appuie sur ESPACE pour revenir",
                font_menu,
                BLUE,
                WIDTH // 2,
                HEIGHT - 100,
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        pygame.display.update()

def main_menu():
    play_menu_music("main")

    clock = pygame.time.Clock()
    while True:
        for y in range(HEIGHT):
            ratio = y / HEIGHT
            r = int(15 + (40 - 15) * ratio)
            g = int(15 + (20 - 15) * ratio)
            b = int(35 + (70 - 35) * ratio)
            pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

        pulse = (pygame.time.get_ticks() // 4) % 255
        glow_color = (pulse, 120, 255)
        title_y = 90 + int(10 * math.sin(pygame.time.get_ticks() * 0.002))

        shadow = font_title.render("TRIVIA TAKEDOWN", True, (0, 0, 0))
        screen.blit(shadow, (WIDTH // 2 - shadow.get_width() // 2 + 4, title_y + 4))

        glow = font_title.render("TRIVIA TAKEDOWN", True, glow_color)
        screen.blit(glow, (WIDTH // 2 - glow.get_width() // 2, title_y))

        title = font_title.render("TRIVIA TAKEDOWN", True, BLUE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, title_y))

        draw_text("Par Brain Strikers", font_menu, WHITE, WIDTH // 2, 190)

        mouse = pygame.mouse.get_pos()
        options = [("COMBATTRE (1v1)", 320), ("CREDITS", 400), ("QUITTER", 480)]
        buttons = []

        for text, y in options:
            rect = pygame.Rect(WIDTH // 2 - 170, y, 340, 60)
            hovered = rect.collidepoint(mouse)
            base_color = (25, 25, 60)
            hover_color = (65, 105, 225)
            outline_color = (120, 160, 255) if hovered else (200, 200, 255)

            pygame.draw.rect(
                screen,
                hover_color if hovered else base_color,
                rect,
                border_radius=15,
            )
            pygame.draw.rect(screen, outline_color, rect, width=2, border_radius=15)

            if hovered:
                inner_rect = rect.inflate(-10, -10)
                pygame.draw.rect(screen, (30, 30, 90), inner_rect, border_radius=12)

            draw_text(text, font_menu, WHITE, WIDTH // 2, y + 8)
            buttons.append(rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(mouse):
                    player = select_character()
                    enemy = random.choice([c for c in characters if c != player])
                    start_fight(player, enemy)
                    # Arrêter la musique de l'arène et relancer celle du menu
                    stop_music()
                    play_menu_music("main")
                if buttons[1].collidepoint(mouse):
                    show_credits()
                    play_menu_music("main")
                if buttons[2].collidepoint(mouse):
                    stop_music()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main_menu()


