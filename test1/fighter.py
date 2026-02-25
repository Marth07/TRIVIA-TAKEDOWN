import pygame


class Fighter:

    def __init__(self, name, x, y, hp, power, style, image):
        self.name = name
        self.hp = hp
        self.power = power
        self.style = style
        self.image = image
        self.rect = pygame.Rect((x, y, image.get_width(), image.get_height()))
        self.attacking = False
        self.health = 100

    def move(self, surface, target, screen_width=1280):
        SPEED = 10
        dx = 0

        key = pygame.key.get_pressed()

        if not self.attacking:
            if key[pygame.K_LEFT]:
                dx = -SPEED
            if key[pygame.K_RIGHT]:
                dx = SPEED

        if key[pygame.K_r] or key[pygame.K_t]:
            self.attack(target)

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        self.rect.x += dx
        self.attacking = False

    def attack(self, target):
        self.attacking = True

        attacking = pygame.Rect(
            self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height
        )

        if attacking.colliderect(target.rect):
            target.health -= self.power
            if target.health < 0:
                target.health = 0

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
