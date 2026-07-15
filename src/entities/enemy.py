import pygame


class Enemy:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.width = 40
        self.height = 40

        self.speed = 3

        self.color = (255, 0, 0)

    def update(self):

        self.x -= self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

    def is_outside_screen(self):

        return self.x + self.width < 0