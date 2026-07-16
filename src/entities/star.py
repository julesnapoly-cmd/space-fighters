import random
import pygame


class Star:

    def __init__(self, width, height):

        # Position initiale de l'étoile
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        # Taille aléatoire
        self.size = random.randint(1, 3)

        # Vitesse de déplacement des étoiles
        self.speed = 2

    def update(self, width, height):

        # Déplacement vers la gauche
        self.x -= self.speed

        # Si l'étoile sort de l'écran,
        # elle réapparaît à droite
        if self.x < 0:

            self.x = width
            self.y = random.randint(0, height)

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            self.size
        )