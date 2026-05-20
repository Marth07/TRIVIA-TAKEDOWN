import pygame
import os
import sys

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

class Fighter:
    def __init__(self, name, x, y, hp, power, special_damage, style, image, speed):
        self.name = name
        self.max_health = hp
        self.health = hp
        self.power = power
        self.special_damage = special_damage
        self.style = style
        self.speed = speed
        self.original_image = image

        self.idle_image = pygame.transform.scale(image, (250, 250))
        self.image = self.idle_image
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.direction = 1

        self.attack_frames = []

        self.attacking = False
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_speed = 80
        self.hit_timer = 0

def start_attack(self):
    print(f"start_attack appelé pour {self.name}, attacking={self.attacking}")
    if not self.attacking:
        self.attacking = True
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        if len(self.attack_frames) > 0:
            self.image = self.attack_frames[0]
            print(f"{self.name} ATTAQUE ! ({len(self.attack_frames)} frames chargées)")
        else:
            print(f"PROBLÈME : {self.name} n'a aucune frame d'attaque !")

    def move(self, screen, enemy, collision_box=None):
        if self.attacking:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen.get_width():
            self.rect.x += self.speed

        if self.rect.colliderect(enemy.rect):
            if self.rect.centerx < enemy.rect.centerx:
                self.rect.right = enemy.rect.left
            else:
                self.rect.left = enemy.rect.right

def ai_move(self, target, screen_width=1280, patrol_left=0, patrol_right=1280):
    if self.attacking:
        return

    dx = 0
    if self.rect.centerx < target.rect.centerx - 60:
        dx = self.speed
    elif self.rect.centerx > target.rect.centerx + 60:
        dx = -self.speed

    if self.rect.left + dx < 0:
        dx = -self.rect.left
    if self.rect.right + dx > screen_width:
        dx = screen_width - self.rect.right

    self.rect.x += dx

def attack(self, target):
    self.start_attack()
    attacking = pygame.Rect(
        self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height
    )
    if attacking.colliderect(target.rect):
        target.health -= self.power
        if target.health < 0:
            target.health = 0

def draw(self, screen):
    self.update_animation()
    screen.blit(self.image, self.rect)

def reset_to_menu_skin(self):
    self.image = self.idle_image
    self.attacking = False
    self.frame_index = 0

def apply_arena_skin(self, arena_path):
    pass
