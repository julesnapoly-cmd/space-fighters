import os
import pygame


class Player:

    def __init__(self):

        # Position du joueur
        self.x = 400
        self.y = 300

        # Vitesse
        self.speed = 5

        # Chargement du sprite
        current_dir = os.path.dirname(__file__)

        image_path = os.path.join(
            current_dir,
            "/Users/Jules/Projects/space-fighters/assets/sprites/vaisseau_32.png"
        )

        self.image = pygame.image.load(image_path).convert_alpha()
        
        
        self.image = pygame.transform.scale(
           self.image,
             (64, 64)
        ) 
        # Taille du sprite
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, keys):

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):

        screen.blit(
            self.image,
            (self.x, self.y)
        )