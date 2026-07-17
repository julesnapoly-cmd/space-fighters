
import pygame


class Enemy:

    def __init__(self, x, y, sprite_path):

        # Position de l'ennemi
        self.x = x
        self.y = y

        
        self.image = pygame.image.load(
                sprite_path
        ).convert_alpha()

        # Taille d'affichage du sprite
        self.image = pygame.transform.scale(
            self.image,
            (96, 96)
        )

        # Dimensions utilisées pour le dessin et les collisions
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # --------------------------------------------------------------
        # Valeurs définies par les classes filles
        # --------------------------------------------------------------

        self.speed = 0
        self.score = 0

    def update(self):

        self.x -= self.speed

    def draw(self, screen):

        screen.blit(
            self.image,
            (self.x, self.y)
        )

    def is_outside_screen(self):

        return self.x + self.width < 0