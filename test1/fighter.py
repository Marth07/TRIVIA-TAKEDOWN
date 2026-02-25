import pygame


class Fighter:

    def __init__(self, name, x, y, hp, power, style, image):
        self.flip = False
        self.name = name
        self.hp = hp
        self.power = power
        self.style = style
        self.image = image
        self.rect = pygame.Rect((x, y, image.get_width(), image.get_height()))
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        

    def move(self, surface, target, screen_width=1280, screen_height=720):
        SPEED = 10
        dx = 0

        key = pygame.key.get_pressed()

        if not self.attacking:
            if key[pygame.K_LEFT]:
                dx = -SPEED
            if key[pygame.K_RIGHT]:
                dx = SPEED

        if key[pygame.K_r] or key[pygame.K_t]:
            self.attack(surface, target)

        if key[pygame.K_r]:
            self.attack_type = 1
        if key[pygame.K_t]:
            self.attack_type = 2

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        self.rect.x += dx
        self.attacking = False

    def attack(self, surface, target):
        self.attacking = True
        attacking = pygame.Rect(
            self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height
        )
        pygame.draw.rect(surface, (0, 255, 0), attacking)

        if attacking.colliderect(target.rect):
            target.health -= self.power
            print(f"{self.name} attaque ! {target.name} a {target.health} HP restants.")

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
