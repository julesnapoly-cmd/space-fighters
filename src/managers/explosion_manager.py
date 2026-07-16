from entities.explosion import Explosion


class ExplosionManager:

    def __init__(self):

        self.explosions = []

    # ------------------------------------------------------------------
    # Création d'une explosion
    # ------------------------------------------------------------------

    def create(self, x, y):

        self.explosions.append(
            Explosion(x, y)
        )

    # ------------------------------------------------------------------
    # Mise à jour des explosions
    # ------------------------------------------------------------------

    def update(self):

        for explosion in self.explosions:
            explosion.update()

    # ------------------------------------------------------------------
    # Dessin des explosions
    # ------------------------------------------------------------------

    def draw(self, screen):

        for explosion in self.explosions:
            explosion.draw(screen)

    # ------------------------------------------------------------------
    # Suppression des explosions terminées
    # ------------------------------------------------------------------

    def clean(self):

        self.explosions = [
            explosion
            for explosion in self.explosions
            if not explosion.is_finished()
        ]

    # ------------------------------------------------------------------
    # Accès à la liste
    # ------------------------------------------------------------------

    def get_explosions(self):

        return self.explosions