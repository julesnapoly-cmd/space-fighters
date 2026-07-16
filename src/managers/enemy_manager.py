import random

from entities.enemy import Enemy


class EnemyManager:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.enemies = []

        self.spawn_timer = 0
        self.spawn_delay = 90

    # ------------------------------------------------------------------
    # Apparition des ennemis
    # ------------------------------------------------------------------

    def spawn(self):

        self.spawn_timer += 1

        if self.spawn_timer >= self.spawn_delay:

            self.enemies.append(
                Enemy(
                    self.screen_width,
                    random.randint(
                        0,
                        self.screen_height - 40
                    )
                )
            )

            self.spawn_timer = 0

    # ------------------------------------------------------------------
    # Mise à jour
    # ------------------------------------------------------------------

    def update(self):

        for enemy in self.enemies:
            enemy.update()

    # ------------------------------------------------------------------
    # Dessin
    # ------------------------------------------------------------------

    def draw(self, screen):

        for enemy in self.enemies:
            enemy.draw(screen)

    # ------------------------------------------------------------------
    # Suppression des ennemis hors écran
    # ------------------------------------------------------------------

    def clean(self):

        self.enemies = [
            enemy
            for enemy in self.enemies
            if not enemy.is_outside_screen()
        ]

    
    # ------------------------------------------------------------------
    # Suppression d'un ennemi
    # ------------------------------------------------------------------

    def remove(self, enemy):

        if enemy in self.enemies:
            self.enemies.remove(enemy)
    # ------------------------------------------------------------------
    # Accès à la liste
    # ------------------------------------------------------------------
    

    def get_enemies(self):

        return self.enemies