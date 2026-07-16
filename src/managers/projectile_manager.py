from entities.projectile import Projectile


class ProjectileManager:

    def __init__(self):

        self.projectiles = []

    # ------------------------------------------------------------------
    # Création d'un projectile
    # ------------------------------------------------------------------

    def fire(self, x, y):

        self.projectiles.append(
            Projectile(x, y)
        )

    # ------------------------------------------------------------------
    # Mise à jour de tous les projectiles
    # ------------------------------------------------------------------

    def update(self):

        for projectile in self.projectiles:
            projectile.update()

    # ------------------------------------------------------------------
    # Dessin des projectiles
    # ------------------------------------------------------------------

    def draw(self, screen):

        for projectile in self.projectiles:
            projectile.draw(screen)

    # ------------------------------------------------------------------
    # Suppression des projectiles hors écran
    # ------------------------------------------------------------------

    def clean(self, screen_width):

        self.projectiles = [
            projectile
            for projectile in self.projectiles
            if not projectile.is_outside_screen(screen_width)
        ]
    # ------------------------------------------------------------------
    # Suppression d'un projectile
    # ------------------------------------------------------------------

    def remove(self, projectile):

        if projectile in self.projectiles:
            self.projectiles.remove(projectile)
    # ------------------------------------------------------------------
    # Accès à la liste des projectiles
    # ------------------------------------------------------------------

    def get_projectiles(self):

        return self.projectiles