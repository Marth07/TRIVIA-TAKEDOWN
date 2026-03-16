import pygame
import random
from fighter import Fighter

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trivia Takedown - Combat")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

image_bg = pygame.image.load("../assets/fond_de_map_desert.png")

font_q = pygame.font.SysFont("Arial", 32)


def draw_background():
    scaled_bg = pygame.transform.scale(image_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


def draw_health_bar(current_health, max_health, x, y):
    ratio = max(0, current_health / max_health)
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400 * ratio, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

    # Affichage des points de vie sous la barre
    hp_text = font_q.render(
        f"{int(max(0, current_health))}/{int(max_health)}", True, WHITE
    )
    screen.blit(
        hp_text,
        (x + 200 - hp_text.get_width() // 2, y + 35),
    )


def draw_choice_box(text, x, y, width=400, height=60):
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(x, y, width, height)

    color = (0, 255, 0) if rect.collidepoint(mouse) else (255, 255, 255)
    pygame.draw.rect(screen, color, rect, 3)

    txt = font_q.render(text, True, WHITE)
    screen.blit(txt, (x + width // 2 - txt.get_width() // 2, y + 15))

    return rect


def victory_screen(winner):
    running = True
    font_big = pygame.font.SysFont("Arial", 80, bold=True)
    font_small = pygame.font.SysFont("Arial", 40)

    while running:
        screen.fill((0, 0, 0))

        text = font_big.render(f"{winner.name} a gagné !", True, (255, 215, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150))

        img = pygame.transform.scale(winner.image, (300, 300))
        screen.blit(img, (SCREEN_WIDTH // 2 - 150, 300))

        text2 = font_small.render("Appuie sur ESPACE pour revenir au menu", True, WHITE)
        screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, 650))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        pygame.display.update()


questions_logique = [
    {
        "question": "Si tu as 5 barres de chocolat dans un bol et que t’en prends 3. Combien il t’en reste ?",
        "choix": ["2", "3", "5", "0"],
        "reponse": "5",
    },
    {
        "question": "Si tu entres dans un restaurant et qu’il y a 3 personnes de 30 ans et 6 personnes de 40 ans. Combien y’en a-t-il au total ?",
        "choix": ["9", "10", "6", "12"],
        "reponse": "10",
    },
    {
        "question": "Certains mois ont 31 jours, d'autres en ont 30. Combien de mois en ont 28 ?",
        "choix": ["1", "12", "6", "0"],
        "reponse": "12",
    },
    {
        "question": "À combien est égale la multiplication de tous les chiffres du numéro de téléphone ?",
        "choix": ["0", "1", "Impossible", "10"],
        "reponse": "0",
    },
    {
        "question": "Qu’est-ce qu’on met dans un toaster ?",
        "choix": ["Pain", "Toast", "Biscotte", "Rien"],
        "reponse": "pain",
    },
]


def start_fight(player, enemy):
    run = True

    player.health = player.max_health
    enemy.health = enemy.max_health

    player.image = pygame.transform.scale(player.image, (250, 250))
    enemy.image = pygame.transform.scale(enemy.image, (250, 250))

    player.rect = player.image.get_rect(midbottom=(250, 650))
    enemy.rect = enemy.image.get_rect(midbottom=(1030, 650))

    collision_box = pygame.Rect(SCREEN_WIDTH // 2 - 50, 500, 100, 200)

    question_interval = 5000
    last_question_time = pygame.time.get_ticks()
    question_active = False
    current_question = None
    time_left = 0
    enemy_answer_delay = 0

    enemy.direction = -1
    patrol_left = 700
    patrol_right = 1100

    choice_boxes = []

    while run:
        dt = clock.tick(FPS)
        draw_background()

        current_time = pygame.time.get_ticks()

        # Nouvelle question
        if (
            not question_active
            and current_time - last_question_time >= question_interval
        ):
            current_question = random.choice(questions_logique)
            question_active = True
            time_left = 10000
            last_question_time = current_time
            enemy_answer_delay = 3000  # IA répond après 5 sec
            choice_boxes = []

        # IA + timer
        if question_active:
            enemy_answer_delay -= dt
            if enemy_answer_delay <= 0:
                if random.random() < 0.5:
                    enemy_answer = current_question["reponse"].lower()
                else:
                    enemy_answer = random.choice(current_question["choix"]).lower()

                if enemy_answer == current_question["reponse"].lower():
                    # L'ennemi répond bien : dégâts basés sur sa compétence
                    player.health -= enemy.damage
                else:
                    # L'ennemi se trompe : il prend les dégâts du joueur
                    enemy.health -= player.damage

                question_active = False

            time_left -= dt
            if time_left <= 0:
                question_active = False

        # Barres de vie
        draw_health_bar(player.health, player.max_health, 20, 20)
        draw_health_bar(enemy.health, enemy.max_health, 860, 20)

        # Mouvements
        if not question_active:
            player.move(screen, enemy)

            enemy.rect.x += 4 * enemy.direction
            if enemy.rect.x <= patrol_left:
                enemy.direction = 1
            elif enemy.rect.x >= patrol_right:
                enemy.direction = -1

        # Collision barrière
        if player.rect.colliderect(collision_box):
            player.rect.x -= 10
        if enemy.rect.colliderect(collision_box):
            enemy.rect.x += 10

        # Dessin des fighters
        player.draw(screen)
        enemy.draw(screen)

        # Affichage question
        if question_active:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            text = font_q.render(current_question["question"], True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150))

            choice_boxes = [
                draw_choice_box(current_question["choix"][0], 150, 300),
                draw_choice_box(current_question["choix"][1], 730, 300),
                draw_choice_box(current_question["choix"][2], 150, 400),
                draw_choice_box(current_question["choix"][3], 730, 400),
            ]

            timer_text = font_q.render(
                f"Temps restant : {time_left // 1000}", True, RED
            )
            screen.blit(
                timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, 550)
            )

        # Fin du combat
        if player.health <= 0:
            victory_screen(enemy)
            return

        if enemy.health <= 0:
            victory_screen(player)
            return

        # Clic sur les choix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if question_active and event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for i, rect in enumerate(choice_boxes):
                    if rect.collidepoint(mouse):
                        if (
                            current_question["choix"][i].lower()
                            == current_question["reponse"].lower()
                        ):
                            # Le joueur répond bien : dégâts basés sur sa compétence
                            enemy.health -= player.damage
                        else:
                            # Mauvaise réponse : dégâts basés sur la compétence de l'ennemi
                            player.health -= enemy.damage
                        question_active = False
                        break

        pygame.display.update()

