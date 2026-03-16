import pygame


class Fighter:
    def __init__(self, name, x, y, health, damage, special_damage, style, image, speed):
        self.name = name
        self.max_health = health
        self.health = health
        self.damage = damage
        self.special_damage = special_damage
        self.style = style
        self.image = image
        self.speed = speed

        self.rect = self.image.get_rect(midbottom=(x, y))
        self.direction = 1

    def move(self, screen, enemy):
        keys = pygame.key.get_pressed()

        # Gauche
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        # Droite
        if keys[pygame.K_RIGHT] and self.rect.right < screen.get_width():
            self.rect.x += self.speed

        # Collision avec l'ennemi
        if self.rect.colliderect(enemy.rect):
            if self.rect.centerx < enemy.rect.centerx:
                self.rect.right = enemy.rect.left
            else:
                self.rect.left = enemy.rect.right

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def ai_move(self, target, screen_width=1280):
        dx = 0

        # Approche du joueur
        if self.rect.centerx < target.rect.centerx - 60:
            dx = self.speed
        elif self.rect.centerx > target.rect.centerx + 60:
            dx = -self.speed
        else:
            # Attaque si proche
            self.attack(target)

        # Limites écran
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        self.rect.x += dx

    def attack(self, target):
        target.health -= self.damage

    def special_attack(self, target):
        """Attaque spéciale, plus puissante que l'attaque simple."""
        target.health -= self.special_damage
