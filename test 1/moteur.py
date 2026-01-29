import pygame
import sys

from fighter import Fighter



SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Trivia Takedown - Brain Strikers")

#framerate
clock = pygame.time.Clock()
FPS = 60
#Couleurs
RED = (255,0,0)
YELLOW =(255,255,0)
WHITE = (255,255,255)

#image background

image_bg = pygame.image.load("montagne bg.jpg").convert()


#fonction pour image_bg

def draw_background():
    scaled_bg = pygame.transform.scale(image_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    #Fonction pour la barre de vie
def draw_health_bar(health, x, y):
    ratio = health/100
    pygame.draw.rect(screen,WHITE,(x-2,y-2,404,34))
    pygame.draw.rect(screen,RED,(x,y,400*ratio,30))
    pygame.draw.rect(screen,YELLOW,(x,y,400*ratio,30))

    
peter = Fighter("Peter", 200, 400, 120, 15, "Lames d'énergie")
steve = Fighter("Steve", 400, 400, 100, 20, "Angles et Trajectoires")
nyra = Fighter("Nyra", 600, 400, 150, 10, "Boucliers de chiffres")
brian = Fighter("Brian", 800, 400, 80, 25, "Frappe lourde")

draw_background()



run = True

while  run:
    clock.tick(FPS)

   

    #draw background

    draw_background()
    #show player stats
    draw_health_bar(peter.health, 20, 20)
    draw_health_bar(steve.health, 860, 20)
    draw_health_bar(nyra.health, 20, 60)
    draw_health_bar(brian.health, 860, 60)
    
    #move Fighters
    peter.move(screen,steve or nyra or brian,SCREEN_WIDTH,SCREEN_HEIGHT,)
    steve.move(screen,peter or nyra or brian,SCREEN_WIDTH,SCREEN_HEIGHT,)
    nyra.move(screen,peter or steve or brian,SCREEN_WIDTH,SCREEN_HEIGHT,)
    brian.move(screen,peter or steve or nyra,SCREEN_WIDTH,SCREEN_HEIGHT,)

    #draw Fighters
    peter.draw(screen)
    steve.draw(screen)
    nyra.draw(screen)
    brian.draw(screen)
    
   

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

           

           

    #chargement screen

    pygame.display.update()



pygame.quit()