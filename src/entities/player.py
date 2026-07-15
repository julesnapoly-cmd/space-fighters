import pygame


class Player:

    def __init__(self):

        self.x = 400
        self.y = 300

        self.width = 50
        self.height = 30

        self.speed = 5

        self.color = (0, 255, 0)

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

        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )