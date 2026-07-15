import pygame


class Projectile :

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.width = 16
        self.height = 4

        self.speed = 10

        self.color = (255, 255, 0)

    def update(self):

        self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

    def is_outside_screen(self, screen_width):

        return self.x > screen_width