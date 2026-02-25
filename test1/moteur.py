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

image_bg = pygame.image.load("assets/fond_de_map_desert.png")

# --------------------------
# QUESTIONS AVEC CHOIX
# --------------------------
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
    {
        "question": "Si un avion s'écrase sur la frontière entre la France et la Belgique, où enterre-t-on les rescapés ?",
        "choix": ["France", "Belgique", "Nulle part", "Les deux"],
        "reponse": "nulle part",
    },
    {
        "question": "Un coq pond un œuf sur le toit d’une maison. De quel côté tombe l’œuf ?",
        "choix": ["Gauche", "Droite", "Aucun", "Devant"],
        "reponse": "Aucun",
    },
    {
        "question": "Combien d’animaux de chaque espèce Moïse a-t-il pris dans son arche ?",
        "choix": ["2", "4", "Aucun", "6"],
        "reponse": "Aucun",
    },
    {
        "question": "Qu’est-ce qui pèse le plus lourd : 1 kg de plumes ou 1 kg de plomb ?",
        "choix": ["Plomb", "Plumes", "Les deux", "Aucun"],
        "reponse": "Les deux",
    },
    {
        "question": "Combien font 7 × 8 ?",
        "choix": ["54", "56", "58", "64"],
        "reponse": "56",
    },
    {
        "question": "Si un carré a un côté de 4 cm, quel est son périmètre ?",
        "choix": ["8 cm", "12 cm", "16 cm", "20 cm"],
        "reponse": "16 cm",
    },
    {
        "question": "Quel est le résultat de 15 + 27 ?",
        "choix": ["32", "42", "40", "52"],
        "reponse": "42",
    },
    {
        "question": "Si tu divises 100 par 0.5, tu obtiens :",
        "choix": ["50", "200", "150", "100"],
        "reponse": "200",
    },
    {
        "question": "Quel est le carré de 12 ?",
        "choix": ["124", "144", "132", "156"],
        "reponse": "144",
    },
    {
        "question": "Quelle est la capitale de l’Italie ?",
        "choix": ["Rome", "Milan", "Naples", "Venise"],
        "reponse": "Rome",
    },
    {
        "question": "Quel est l’océan le plus grand du monde ?",
        "choix": ["Atlantique", "Indien", "Arctique", "Pacifique"],
        "reponse": "Pacifique",
    },
    {
        "question": "Qui a peint la Joconde ?",
        "choix": ["Van Gogh", "Picasso", "Léonard de Vinci", "Monet"],
        "reponse": "Léonard de Vinci",
    },
    {
        "question": "Quel est le plus grand désert du monde ?",
        "choix": ["Sahara", "Gobi", "Antarctique", "Arabie"],
        "reponse": "Antarctique",
    },
    {
        "question": "Combien de continents existe-t-il ?",
        "choix": ["5", "6", "7", "8"],
        "reponse": "7",
    },
    {
        "question": "Quel est l’animal terrestre le plus rapide ?",
        "choix": ["Guépard", "Lion", "Antilope", "Tigre"],
        "reponse": "Guépard",
    },
    {
        "question": "Quel est le plus long fleuve du monde ?",
        "choix": ["Nil", "Amazone", "Yangtsé", "Mississippi"],
        "reponse": "Amazone",
    },
    {
        "question": "Quel pays a inventé les Jeux Olympiques ?",
        "choix": ["Italie", "Grèce", "France", "Turquie"],
        "reponse": "Grèce",
    },
    {
        "question": "Quel est l’organe principal du système nerveux ?",
        "choix": ["Cœur", "Poumons", "Cerveau", "Foie"],
        "reponse": "Cerveau",
    },
]

font_q = pygame.font.SysFont("Arial", 32)


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
    # Réinitialiser la vie au début du combat
    player.health = 100
    enemy.health = 100

    player.image = pygame.transform.scale(player.image, (250, 250))
    enemy.image = pygame.transform.scale(enemy.image, (250, 250))

    player.rect = player.image.get_rect(midbottom=(250, 650))
    enemy.rect = enemy.image.get_rect(midbottom=(1030, 650))
    # Barrière centrale

    collision_box = pygame.Rect(SCREEN_WIDTH // 2 - 50, 500, 100, 200)

    # QUIZ
    question_interval = 5000
    last_question_time = pygame.time.get_ticks()
    question_active = False
    current_question = None
    time_left = 0

    # ROUND
    round_time = 60000
    round_start = pygame.time.get_ticks()

    while run:
        dt = clock.tick(FPS)
        draw_background()

        current_time = pygame.time.get_ticks()

        # FIN DU ROUND
        if current_time - round_start >= round_time:
            print("FIN DU ROUND")
            run = False

        # LANCER QUESTION
        if (
            not question_active
            and current_time - last_question_time >= question_interval
        ):
            current_question = random.choice(questions_logique)
            question_active = True
            time_left = 5000
            last_question_time = current_time

        # AFFICHAGE QUESTION
        if question_active:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            text = font_q.render(current_question["question"], True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150))

            for i, choix in enumerate(current_question["choix"], start=1):
                c = font_q.render(f"{i}. {choix}", True, WHITE)
                screen.blit(c, (SCREEN_WIDTH // 2 - c.get_width() // 2, 250 + i * 50))

            timer_text = font_q.render(f"Temps restant : {time_left//1000}", True, RED)
            screen.blit(
                timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, 550)
            )

            time_left -= dt

            if time_left <= 0:
                question_active = False

        # HEALTH
        draw_health_bar(player.health, 20, 20)
        draw_health_bar(enemy.health, 860, 20)

        # MOUVEMENT UNIQUEMENT SI PAS DE QUESTION
        if not question_active:
            player.move(screen, enemy)
            # Collision avec la barrière centrale
        if player.rect.colliderect(collision_box):
            player.rect.x -= 10

        if enemy.rect.colliderect(collision_box):
            enemy.rect.x += 10

        # AFFICHAGE FIGHTERS
        player.draw(screen)
        enemy.draw(screen)

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if question_active and event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    choix_index = int(event.unicode) - 1
                    reponse_user = current_question["choix"][choix_index].lower()

                    if reponse_user == current_question["reponse"].lower():
                        enemy.health -= 10
                    else:
                        player.health -= 10

                    question_active = False

        pygame.display.update()

    return
