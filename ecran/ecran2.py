import pygame
import sys
import subprocess

pygame.init()

WIDTH, HEIGHT = 1800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TRIVIA TAKEDOWN")

try:
    background = pygame.image.load("assets/glo.jpeg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    pygame.mixer.music.load("assets/music.mp3")
    pygame.mixer.music.play(-1)
except pygame.error:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((20, 20, 40))

WHITE = (255, 255, 255)
TRANSLUCENT_BLUE = (0, 80, 200, 180)
HOVER_BLUE = (0, 140, 255, 180)
SHADOW = (0, 0, 0)

try:
    FONT_TITLE = pygame.font.Font("assets/pixels.ttf", 72)
    FONT_BUTTON = pygame.font.Font("assets/pixels.ttf", 36)
except:
    FONT_TITLE = pygame.font.SysFont("Arial", 72, bold=True)
    FONT_BUTTON = pygame.font.SysFont("Arial", 36)


# --- Button Class ---
class Button:
    def __init__(self, text, center_y, action):
        self.text = text
        self.action = action
        self.width, self.height = 320, 70
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (WIDTH // 2, center_y)

    def draw(self, win, mouse_pos):
        is_hover = self.rect.collidepoint(mouse_pos)
        color = HOVER_BLUE if is_hover else TRANSLUCENT_BLUE
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, (0, 0, self.width, self.height), border_radius=10)
        win.blit(button_surface, self.rect)
        text_surf = FONT_BUTTON.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        shadow_surf = FONT_BUTTON.render(self.text, True, SHADOW)
        win.blit(shadow_surf, (text_rect.x + 2, text_rect.y + 2))
        win.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]
buttons = [
    Button("Nouvelle partie", 320, "new"),
    Button("Charger partie", 400, "load"),
    Button("Options", 480, "options"),
    Button("Quitter", 560, "quit"),
]

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                for btn in buttons:
                    if btn.rect.collidepoint(mouse_pos):
                        if btn.action == "new":
                            print("Starting New Game...")
                            # subprocess.run(["python", "main.py"])
                        elif btn.action == "quit":
                            running = False
    title_text = "TRIVIA TAKEDOWN"
    title = FONT_TITLE.render(title_text, True, WHITE)
    title_shadow = FONT_TITLE.render(title_text, True, SHADOW)
    title_x = WIDTH // 2 - title.get_width() // 2

    screen.blit(title_shadow, (title_x + 3, 103))
    screen.blit(title, (title_x, 100))
    for btn in buttons:
        btn.draw(screen, mouse_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
