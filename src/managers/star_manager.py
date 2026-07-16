from entities.star import Star


class StarManager:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.stars = []

        # Création des étoiles
        for _ in range(100):

            self.stars.append(
                Star(width, height)
            )

    def update(self):

        # Mise à jour de toutes les étoiles
        for star in self.stars:

            star.update(
                self.width,
                self.height
            )

    def draw(self, screen):

        # Dessin de toutes les étoiles
        for star in self.stars:

            star.draw(screen)