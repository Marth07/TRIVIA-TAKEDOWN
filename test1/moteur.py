import pygame
import random
from fighter import Fighter
import sys
import os

def get_asset_path(relative_path):
    if getattr(sys, "frozen", False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.abspath(".")
    path = os.path.join(base, relative_path)
    if os.path.exists(path):
        return path
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return path

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trivia Takedown - Combat")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

image_bg = None

font_q = pygame.font.SysFont("Arial", 32)

def choose_random_arena():
    arenas = [
        {"image": get_asset_path("assets/Arene/arene_plage.png"), "music": get_asset_path("assets/Musique/Plage.mp3")},
        {"image": get_asset_path("assets/Arene/arene_desert2.png"), "music": get_asset_path("assets/Musique/Desert.mp3")},
        {"image": get_asset_path("assets/Arene/arene_cristaux.png"), "music": get_asset_path("assets/Musique/Cristaux.mp3")},
        {"image": get_asset_path("assets/Arene/arene_Glace.png"), "music": get_asset_path("assets/Musique/Fortnite.mp3")},
        {"image": get_asset_path("assets/Arene/arene_futuriste.png"), "music": get_asset_path("assets/Musique/Ville.mp3")},
        {"image": get_asset_path("assets/Arene/Dojo.png"), "music": get_asset_path("assets/Musique/Dojo.mp3")},
    ]
    chosen = random.choice(arenas)
    return chosen["image"], chosen["music"]

def play_menu_music(menu_type="main"):
    music_path = get_asset_path("assets/Musique/Rocky theme song.mp3")
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.6)
    except Exception as e:
        print(f"Erreur musique menu: {e}")

def play_arena_music(music_path):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.7)
    except Exception as e:
        print(f"Erreur musique arène: {e}")

def stop_music():
    pygame.mixer.music.stop()

def draw_background():
    if image_bg is None:
        screen.fill((0, 0, 0))
        return
    scaled_bg = pygame.transform.scale(image_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(current_health, max_health, x, y, bar_color=BLUE):
    ratio = max(0, current_health / max_health)
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400 * ratio, 30))
    pygame.draw.rect(screen, bar_color, (x, y, 400 * ratio, 30))
    hp_text = font_q.render(f"{int(max(0, current_health))}/{int(max_health)}", True, WHITE)
    screen.blit(hp_text, (x + 200 - hp_text.get_width() // 2, y + 35))

def draw_choice_box(text, x, y, width=400, height=60):
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(x, y, width, height)
    color = (0, 255, 0) if rect.collidepoint(mouse) else (255, 255, 255)
    pygame.draw.rect(screen, color, rect, 3)
    txt = font_q.render(text, True, WHITE)
    screen.blit(txt, (x + width // 2 - txt.get_width() // 2, y + 15))
    return rect

def show_final_victory_screen(winner, player_wins, enemy_wins, is_player_winner):
    running = True
    font_big = pygame.font.SysFont("Arial", 80, bold=True)
    font_medium = pygame.font.SysFont("Arial", 50)
    font_small = pygame.font.SysFont("Arial", 30)
    stop_music()

    if is_player_winner:
        victory_music_path = get_asset_path("assets/Musique/Street Fighter.mp3")
        try:
            pygame.mixer.music.load(victory_music_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Erreur musique victoire: {e}")
    else:
        defeat_music_path = get_asset_path("assets/Musique/Lose.mp3")
        try:
            pygame.mixer.music.load(defeat_music_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Erreur musique défaite: {e}")

    while running:
        screen.fill((0, 0, 0))
        victory_text = font_big.render(f"{winner.name} GAGNE LE BEST OF !", True, (255, 215, 0))
        screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, 100))
        score_text = font_medium.render(f"Score Final: {player_wins} - {enemy_wins}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 250))
        img = pygame.transform.scale(winner.idle_image, (300, 300))
        screen.blit(img, (SCREEN_WIDTH // 2 - 150, 350))
        instruction = font_small.render("Appuie sur ESPACE pour revenir au menu", True, (255, 255, 255))
        screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, 650))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                stop_music()
                return
        pygame.display.update()

def victory_screen(winner, is_player_winner):
    running = True
    font_big = pygame.font.SysFont("Arial", 80, bold=True)
    font_small = pygame.font.SysFont("Arial", 40)
    stop_music()

    if is_player_winner:
        victory_music_path = get_asset_path("assets/Musique/victory_fanfare.mp3")
        try:
            pygame.mixer.music.load(victory_music_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Erreur musique victoire round: {e}")
    else:
        defeat_music_path = get_asset_path("assets/Musique/MMM.mp3")
        try:
            pygame.mixer.music.load(defeat_music_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Erreur musique défaite round: {e}")

    while running:
        screen.fill((0, 0, 0))
        text = font_big.render(f"{winner.name} a gagné !", True, (255, 215, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150))
        img = pygame.transform.scale(winner.idle_image, (300, 300))
        screen.blit(img, (SCREEN_WIDTH // 2 - 150, 300))
        text2 = font_small.render("Appuie sur ESPACE pour revenir au menu", True, WHITE)
        screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, 650))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                stop_music()
                return
        pygame.display.update()

questions_logique = [
    {"question": "Un coq pond un œuf au sommet d'un toit. De quel côté tombe l'œuf ?", "choix": ["Gauche", "Droite", "En bas", "Nulle part"], "reponse": "Nulle part"},
    {"question": "Tu as une allumette. Dans la pièce : une bougie, un poêle, une lampe. Qu'allumes-tu en premier ?", "choix": ["La bougie", "Le poêle", "La lampe", "L'allumette"], "reponse": "L'allumette"},
    {"question": "Un avion s'écrase à la frontière France-Espagne. Où enterre-t-on les survivants ?", "choix": ["France", "Espagne", "Les deux", "On n'enterre pas les survivants"], "reponse": "On n'enterre pas les survivants"},
    {"question": "Dans une course, tu dépasses le 2ème. Quelle est ta position ?", "choix": ["1er", "2ème", "3ème", "4ème"], "reponse": "2ème"},
    {"question": "Combien de mois de l'année ont 30 jours ?", "choix": ["4", "6", "11", "12"], "reponse": "11"},
    {"question": "Un roi a 7 fils. Chaque fils a une sœur. Combien d'enfants a le roi ?", "choix": ["7", "8", "14", "15"], "reponse": "8"},
    {"question": "Si tu retires 1 de 19, tu obtiens ?", "choix": ["18", "20", "9", "1"], "reponse": "1"},
    {"question": "Tu conduis un bus. 10 montent, 3 descendent, 5 montent, 2 descendent. Quel âge a le conducteur ?", "choix": ["10 ans", "15 ans", "18 ans", "On ne sait pas"], "reponse": "On ne sait pas"},
    {"question": "Paul est deux fois plus vieux que sa sœur. Dans 10 ans, de combien sera-t-il plus vieux ?", "choix": ["20 ans", "10 ans", "La moitié", "Pareil qu'avant"], "reponse": "Pareil qu'avant"},
    {"question": "Si tu doubles la moitié de 20, tu obtiens ?", "choix": ["10", "40", "20", "5"], "reponse": "20"},
    {"question": "Combien y-at-il de troue dans un polo?", "choix": ["1", "4", "3", "2"], "reponse": "4"},
    {"question": "Tu as 1000€. Tu achètes une vache 300€, la revends 350€, la rachètes 400€, la revends 500€. Gain ?", "choix": ["100€", "50€", "200€", "150€"], "reponse": "150€"},
    {"question": "Certains mois ont 31 jours, d'autres 30. Combien en ont 28 ?", "choix": ["1", "0", "6", "12"], "reponse": "12"},
    {"question": "Si 5 machines font 5 pièces en 5 min, combien de min pour 100 machines de faire 100 pièces ?", "choix": ["100", "500", "1", "5"], "reponse": "5"},
    {"question": "Un carré a 4 coins. Si on coupe un coin, combien reste-t-il de coins ?", "choix": ["3", "4", "6", "5"], "reponse": "5"},
    {"question": "À combien est égale la multiplication de tous les chiffres de 1 à 9 ?", "choix": ["362880", "45", "0", "100"], "reponse": "362880"},
    {"question": "Tu as 3 pommes et tu en prends 2. Combien as-tu de pommes ?", "choix": ["1", "3", "0", "2"], "reponse": "2"},
    {"question": "Une bouteille et son bouchon coûtent 1,10€. La bouteille coûte 1€ de plus. Le bouchon coûte ?", "choix": ["0,10€", "0,20€", "0,15€", "0,05€"], "reponse": "0,05€"},
    {"question": "Quel est le seul mammifère capable de voler ?", "choix": ["L'écureuil", "La chauve-souris", "Le poisson volant", "Le lézard"], "reponse": "La chauve-souris"},
    {"question": "Combien y a-t-il de cordes sur une guitare classique ?", "choix": ["4", "5", "7", "6"], "reponse": "6"},
    {"question": "Quelle est la capitale de l'Australie ?", "choix": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "reponse": "Canberra"},
    {"question": "Combien de joueurs composent une équipe de basketball sur le terrain ?", "choix": ["6", "7", "5", "4"], "reponse": "5"},
    {"question": "Quel est l'os le plus long du corps humain ?", "choix": ["L'humérus", "Le radius", "Le tibia", "Le fémur"], "reponse": "Le fémur"},
    {"question": "Combien de continents y a-t-il sur Terre ?", "choix": ["5", "8", "6", "7"], "reponse": "7"},
    {"question": "Quel pays a la plus grande superficie du monde ?", "choix": ["Canada", "Chine", "USA", "Russie"], "reponse": "Russie"},
    {"question": "Quelle planète est la plus proche du Soleil ?", "choix": ["Vénus", "Terre", "Mercure", "Mars"], "reponse": "Mercure"},
    {"question": "Combien de faces a un cube ?", "choix": ["4", "8", "12", "6"], "reponse": "6"},
    {"question": "Quel animal est le plus rapide sur terre ?", "choix": ["Lion", "Guépard", "Faucon", "Antilope"], "reponse": "Guépard"},
    {"question": "À quelle température l'eau bout-elle au niveau de la mer ?", "choix": ["90°C", "95°C", "105°C", "100°C"], "reponse": "100°C"},
    {"question": "Combien d'os a un adulte humain ?", "choix": ["106", "206", "306", "406"], "reponse": "206"},
    {"question": "Quelle est la formule chimique de l'eau ?", "choix": ["HO", "H2O2", "H3O", "H2O"], "reponse": "H2O"},
    {"question": "Quel gaz les plantes absorbent-elles pour faire la photosynthèse ?", "choix": ["Oxygène", "Azote", "Hydrogène", "CO2"], "reponse": "CO2"},
    {"question": "Combien de dents a un adulte humain (dents de sagesse comprises) ?", "choix": ["28", "30", "36", "32"], "reponse": "32"},
    {"question": "Quelle est la vitesse de la lumière (approximativement) ?", "choix": ["150 000 km/s", "400 000 km/s", "100 000 km/s", "300 000 km/s"], "reponse": "300 000 km/s"},
    {"question": "Plus je sèche, plus je suis mouillée. Qu'est-ce que je suis ?", "choix": ["Une éponge", "Une serviette", "Une piscine", "Un nuage"], "reponse": "Une serviette"},
    {"question": "J'ai des villes sans maisons, des forêts sans arbres, de l'eau sans poissons. Qu'est-ce que je suis ?", "choix": ["Un rêve", "Un désert", "Une carte", "Un film"], "reponse": "Une carte"},
    {"question": "Plus je suis chaud, plus les gens m'enlèvent. Qu'est-ce que je suis ?", "choix": ["Un manteau", "Un radiateur", "Le soleil", "Un vêtement"], "reponse": "Un vêtement"},
    {"question": "Je parle sans bouche, j'entends sans oreilles. Qu'est-ce que je suis ?", "choix": ["Un robot", "Un écho", "Un miroir", "Une radio"], "reponse": "Un écho"},
    {"question": "Qu'est-ce qu'on jette quand on en a besoin et qu'on ramasse quand on n'en a plus besoin ?", "choix": ["De l'argent", "Un filet", "Une ancre", "Des ordures"], "reponse": "Une ancre"},
    {"question": "Un agriculteur a 10 vaches. Toutes sauf 4 meurent. Combien reste-t-il de vaches ?", "choix": ["6", "0", "10", "4"], "reponse": "4"},
    {"question": "Combien font 15076 × 145276 ?", "choix": ["2194567876", "2", "Flemme de calculer", "3"], "reponse": "2194567876"},
    {"question": "Quel est le carré de 12 ?", "choix": ["124", "121", "144", "132"], "reponse": "144"},
    {"question": "Combien font 15% de 200 ?", "choix": ["25", "20", "35", "30"], "reponse": "30"},
    {"question": "Si tu as 50€ et que tu dépenses la moitié, puis encore la moitié du reste, combien il te reste ?", "choix": ["0€", "10€", "25€", "12,5€"], "reponse": "12,5€"},
    {"question": "Combien de joueurs y a-t-il dans une équipe de foot sur le terrain ?", "choix": ["10", "12", "9", "11"], "reponse": "11"},
    {"question": "Combien de anneaux y a-t-il sur le drapeau olympique ?", "choix": ["4", "6", "3", "5"], "reponse": "5"},
    {"question": "Dans quel pays les Jeux Olympiques ont-ils été inventés ?", "choix": ["Italie", "Egypte", "Rome", "Grèce"], "reponse": "Grèce"},
    {"question": "Qui a peint la Joconde ?", "choix": ["Michel-Ange", "Picasso", "Raphaël", "Léonard de Vinci"], "reponse": "Léonard de Vinci"},
    {"question": "Combien de couleurs y a-t-il dans un arc-en-ciel ?", "choix": ["5", "6", "8", "7"], "reponse": "7"},
]

def best_of_series(player, enemy, rounds_to_win=3):
    player_wins = 0
    enemy_wins = 0
    round_number = 1

    while player_wins < rounds_to_win and enemy_wins < rounds_to_win:
        show_round_screen(round_number, player_wins, enemy_wins, rounds_to_win)
        round_winner = start_fight_round(player, enemy)
        if round_winner == player:
            player_wins += 1
        else:
            enemy_wins += 1
        round_number += 1

        player.reset_to_menu_skin()
        enemy.reset_to_menu_skin()

    final_winner = player if player_wins >= rounds_to_win else enemy
    is_player_winner = player_wins >= rounds_to_win
    show_final_victory_screen(final_winner, player_wins, enemy_wins, is_player_winner)
    return final_winner

def show_round_screen(round_number, player_wins, enemy_wins, rounds_to_win):
    running = True
    font_big = pygame.font.SysFont("Arial", 60, bold=True)
    font_small = pygame.font.SysFont("Arial", 30)
    stop_music()

    while running:
        screen.fill((0, 0, 0))
        text = font_big.render(f"Round {round_number}", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 200))
        score_text = font_small.render(f"Score: Joueur {player_wins} - {enemy_wins} Ennemi", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))
        bestof_text = font_small.render(f"Best of {rounds_to_win}", True, (255, 215, 0))
        screen.blit(bestof_text, (SCREEN_WIDTH // 2 - bestof_text.get_width() // 2, 400))
        instruction = font_small.render("Appuie sur ESPACE pour commencer", True, (255, 255, 255))
        screen.blit(instruction, (SCREEN_WIDTH // 2 - instruction.get_width() // 2, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        pygame.display.update()

def start_fight(player, enemy):
    return best_of_series(player, enemy, rounds_to_win=3)

def start_fight_round(player, enemy):
    run = True
    global image_bg

    arena_path, music_path = choose_random_arena()
    image_bg = pygame.image.load(arena_path)

    play_arena_music(music_path)

    player.health = player.max_health
    enemy.health = enemy.max_health

    player.apply_arena_skin(arena_path)
    enemy.apply_arena_skin(arena_path)

    player.image = pygame.transform.scale(player.idle_image, (250, 250))
    enemy.image = pygame.transform.scale(enemy.idle_image, (250, 250))

    player.rect = player.image.get_rect(midbottom=(250, 650))
    enemy.rect = enemy.image.get_rect(midbottom=(1030, 650))

    collision_box = pygame.Rect(SCREEN_WIDTH // 2 - 50, 500, 100, 200)

    question_interval = 5000
    last_question_time = pygame.time.get_ticks()
    question_active = False
    current_question = None
    time_left = 0
    enemy_answer_delay = 0
    choice_boxes = []

    player_streak = 0
    enemy_streak = 0

    player_hit_timer = 0
    enemy_hit_timer = 0
    player_special_timer = 0
    enemy_special_timer = 0

    remaining_questions = questions_logique.copy()
    random.shuffle(remaining_questions)

    enemy.direction = -1
    patrol_left = SCREEN_WIDTH // 2 + 50
    patrol_right = SCREEN_WIDTH - 300

    while run:
        dt = clock.tick(FPS)
        draw_background()

        current_time = pygame.time.get_ticks()

        if not question_active and remaining_questions and current_time - last_question_time >= question_interval:
            current_question = remaining_questions.pop()
            question_active = True
            time_left = 10000
            last_question_time = current_time
            enemy_answer_delay = random.randint(1500, 3500)
            choice_boxes = []

        if question_active:
            enemy_answer_delay -= dt
            if enemy_answer_delay <= 0:
                accuracy = 0.7
                if random.random() < accuracy:
                    enemy_answer = current_question["reponse"].lower()
                else:
                    wrong_choices = [c for c in current_question["choix"] if c.lower() != current_question["reponse"].lower()]
                    enemy_answer = random.choice(wrong_choices).lower()

                if enemy_answer == current_question["reponse"].lower():
                    enemy_streak += 1
                    player_streak = 0
                    print(f"{enemy.name} a bien répondu ! Combo : {enemy_streak}")

                    if enemy_streak >= 3:
                        enemy.start_attack()
                        player.health -= enemy.special_damage
                        enemy_streak = 0
                        player_special_timer = 250
                        print(f"{enemy.name} utilise son pouvoir spécial ! ({enemy.special_damage} dégâts)")
                    else:
                        enemy.start_attack()
                        player.health -= enemy.power
                        player_hit_timer = 180
                else:
                    enemy_streak = 0
                    enemy.health = max(0, enemy.health - enemy.power // 2)
                    player.health = min(player.max_health, player.health + 10)
                    print(f"{enemy.name} s'est trompé !")

                question_active = False

            time_left -= dt
            if time_left <= 0:
                print("Temps écoulé !")
                question_active = False

        if player_hit_timer > 0:
            player_hit_timer = max(0, player_hit_timer - dt)
        if enemy_hit_timer > 0:
            enemy_hit_timer = max(0, enemy_hit_timer - dt)
        if player_special_timer > 0:
            player_special_timer = max(0, player_special_timer - dt)
        if enemy_special_timer > 0:
            enemy_special_timer = max(0, enemy_special_timer - dt)

        draw_health_bar(player.health, player.max_health, 20, 20, BLUE)
        draw_health_bar(enemy.health, enemy.max_health, 860, 20, RED)

        if not question_active:
            player.move(screen, enemy, collision_box)
            enemy.ai_move(player, SCREEN_WIDTH, patrol_left, patrol_right)

        if enemy.rect.colliderect(collision_box):
            enemy.rect.x += 10 * (-enemy.direction)

        player.draw(screen)
        enemy.draw(screen)

        if player_hit_timer > 0 or player_special_timer > 0:
            overlay = pygame.Surface((player.rect.width, player.rect.height), pygame.SRCALPHA)
            color = (255, 0, 0, 120) if player_special_timer > 0 else (255, 255, 0, 100)
            overlay.fill(color)
            screen.blit(overlay, player.rect.topleft)

        if enemy_hit_timer > 0 or enemy_special_timer > 0:
            overlay = pygame.Surface((enemy.rect.width, enemy.rect.height), pygame.SRCALPHA)
            color = (0, 0, 255, 120) if enemy_special_timer > 0 else (255, 255, 0, 100)
            overlay.fill(color)
            screen.blit(overlay, enemy.rect.topleft)

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

            timer_text = font_q.render(f"Temps restant : {time_left // 1000}", True, RED)
            screen.blit(timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, 550))

        if player.health <= 0:
            victory_screen(enemy, is_player_winner=False)
            return enemy
        if enemy.health <= 0:
            victory_screen(player, is_player_winner=True)
            return player

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if question_active and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(choice_boxes):
                    if rect.collidepoint(mouse_pos):
                        selected = current_question["choix"][i].lower()
                        correct = current_question["reponse"].lower()

                        if selected == correct:
                            player_streak += 1
                            enemy_streak = 0
                            heal_amount = random.randint(5, 15)
                            player.health = min(player.max_health, player.health + heal_amount)

                            if player_streak >= 3:
                                player.start_attack()
                                enemy.health -= player.special_damage
                                player_streak = 0
                                enemy_special_timer = 250
                                print(f"{player.name} utilise son pouvoir spécial !")
                            else:
                                player.start_attack()
                                enemy.health -= player.power
                                enemy_hit_timer = 180
                        else:
                            player_streak = 0
                            player.health -= enemy.power
                            player_hit_timer = 180

                        question_active = False

        pygame.display.update()

    return None

