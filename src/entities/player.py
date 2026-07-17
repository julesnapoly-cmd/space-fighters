import os
import pygame
from weapons.semi_auto_weapon import SemiAutoWeapon

class Player:

    def __init__(self):

        # Position du joueur
        self.x = 400
        self.y = 300

        # Vitesse
        self.speed = 5

        # ------------------------------------------------------------------
        # Arme équipée
        # ------------------------------------------------------------------

        self.weapon = SemiAutoWeapon()

        # Chargement du sprite
        current_dir = os.path.dirname(__file__)

        image_path = os.path.join(
            current_dir,
            "/Users/Jules/Projects/space-fighters/assets/sprites/player/vaisseau_32.png"
        )

        self.image = pygame.image.load(image_path).convert_alpha()
        
        
        self.image = pygame.transform.scale(
           self.image,
             (64, 64)
        ) 
        # Taille du sprite
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # ------------------------------------------------------------------
        # Gameplay
        # ------------------------------------------------------------------

        self.max_health = 3
        self.health = self.max_health

        # ------------------------------------------------------------------
        # Invincibilité temporaire
        # ------------------------------------------------------------------

        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 120      # 2 secondes à 60 FPS

        # Clignotement
        self.blink_timer = 0
        self.visible = True

    def update(self, keys):

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed


    # ------------------------------------------------------------------
    # Gestion de l'arme
    # ------------------------------------------------------------------

    def shoot(self, is_trigger_pressed, projectile_manager):

        self.weapon.update(
            is_trigger_pressed,
            self,
            projectile_manager
        )

    # ------------------------------------------------------------------
    # Le joueur perd une vie
    # ------------------------------------------------------------------
    def take_damage(self):

        if self.invincible:
            return

        self.health -= 1

        self.invincible = True
        self.invincible_timer = self.invincible_duration

    # ------------------------------------------------------------------
    # Vérifie si le joueur est mort
    # ------------------------------------------------------------------

    def is_dead(self):

        return self.health <= 0

    def draw(self, screen):
    
        if self.visible:

            screen.blit(
                self.image,
                (self.x, self.y)
            )

    # ------------------------------------------------------------------
    # Gestion de l'invincibilité
    # ------------------------------------------------------------------

        if self.invincible:

            self.invincible_timer -= 1
            self.blink_timer += 1

            if self.blink_timer >= 5:

                self.visible = not self.visible
                self.blink_timer = 0

            if self.invincible_timer <= 0:

                self.invincible = False
                self.visible = True

    # ------------------------------------------------------------------
    # Nombre de vies restantes
    # ------------------------------------------------------------------

    def get_health(self):

        return self.health