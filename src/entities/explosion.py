import os
import pygame


class Explosion:

    def __init__(self, x, y):

        # Position du centre de l'explosion
        self.x = x
        self.y = y

        # Durée de vie (30 frames ≈ 0,5 seconde à 60 FPS)
        self.life = 30

        # Taille actuelle du sprite
        self.size = 20

        # Taille maximale
        self.max_size = 164


        # Chargement du sprite
        current_dir = os.path.dirname(__file__)

        image_path = os.path.join(
            current_dir,
            "/Users/Jules/Projects/space-fighters/assets/sprites/effects/sprite-explosion-soucoupe.png"
        )

        self.original_image = pygame.image.load(image_path).convert_alpha()

    def update(self):

        # L'explosion grandit progressivement
        if self.size < self.max_size:
            self.size += 3

        # La durée de vie diminue
        self.life -= 1

    def draw(self, screen):

        # Redimensionnement du sprite selon la taille actuelle
        image = pygame.transform.scale(
            self.original_image,
            (self.size, self.size)
        )

        # Centrage du sprite sur le point d'impact
        screen.blit(
            image,
            (
                self.x - self.size // 2,
                self.y - self.size // 2
            )
        )

    def is_finished(self):

        return self.life <= 0