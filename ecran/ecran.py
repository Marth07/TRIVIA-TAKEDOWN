import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Takedown - Brain Strikers") 

WHITE = (255, 255, 255)
BLUE_LOGO = (65, 105, 225) 
BLACK = (0, 0, 0)

font_title = pygame.font.SysFont("Arial", 80, bold=True)
font_menu = pygame.font.SysFont("Arial", 40)

class Fighter:
    def __init__(self, name, hp, power, style):
        self.name = name
        self.hp = hp
        self.power = power
        self.style = style

peter = Fighter("Peter", 120, 15, "Lames d'énergie")
steve = Fighter("Steve", 100, 20, "Angles et Trajectoires")
barry = Fighter("Barry", 150, 10, "Boucliers de chiffres")
brian = Fighter("Brian", 80, 25, "Frappe lourde")

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x - img.get_width() // 2, y))

def main_menu():
    print(f"Nouveau combat prêt : Choisissez votre combattant !")
    
    while True:
        screen.fill((15, 15, 35)) 
        
        draw_text("TRIVIA TAKEDOWN", font_title, BLUE_LOGO, WIDTH // 2, 100)
        draw_text("Par Brain Strikers", font_menu, WHITE, WIDTH // 2, 180) 

        mouse_pos = pygame.mouse.get_pos()
        
        options = [
            ("COMBATTRE (1v1)", 300),
            ("TOURNOI", 380),
            ("CREDITS", 460),
            ("QUITTER", 540)
        ]

        buttons = []
        for text, y in options:
            is_hovered = WIDTH//2 - 150 < mouse_pos[0] and mouse_pos[0]< WIDTH//2 + 150 and y < mouse_pos[1]  and mouse_pos[1]< y + 50
            color = BLUE_LOGO if is_hovered else WHITE
            
            draw_text(text, font_menu, color, WIDTH // 2, y)
            buttons.append(pygame.Rect(WIDTH//2 - 150, y, 300, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(mouse_pos):
                    print(f"Lancement du Duel : {peter.name}, {steve.name}, {barry.name} et {brian.name} entre en scène !") 
                if buttons[1].collidepoint(mouse_pos):
                    print("Ouverture de l'arbre de Tournoi...") 
                if buttons[2].collidepoint(mouse_pos):
                    print("Equipe : Gloria, Hedi, Vincent, Marthen") 
                if buttons[3].collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
    
