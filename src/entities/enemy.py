import os
import pygame


class Enemy:

    def __init__(self, x, y):

        # Position de l'ennemi
        self.x = x
        self.y = y

        # Vitesse de déplacement
        self.speed = 3

        # Valeur de l'ennemi en points
        self.score = 100

        # Chargement du sprite
        current_dir = os.path.dirname(__file__)

        image_path = os.path.join(
            current_dir,
            "/Users/Jules/Projects/space-fighters/assets/sprites/sprite-soucoupe-ennemi.png"
        )

        self.image = pygame.image.load(image_path).convert_alpha()

        # Taille d'affichage du sprite
        self.image = pygame.transform.scale(
            self.image,
            (96, 96)
        )

        # Dimensions utilisées pour le dessin et les collisions
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):

        self.x -= self.speed

    def draw(self, screen):

        screen.blit(
            self.image,
            (self.x, self.y)
        )

    def is_outside_screen(self):

        return self.x + self.width < 0