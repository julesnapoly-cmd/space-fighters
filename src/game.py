import random
import pygame

from entities.player import Player
from entities.projectile import Projectile
from entities.enemy import Enemy


class Game:

    def __init__(self):

        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Fighters")

        self.clock = pygame.time.Clock()

        self.player = Player()

        self.projectiles = []
        self.enemies = []

        self.running = True

        self.enemy_spawn_timer = 0
        self.enemy_spawn_delay = 120

    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        projectile = Projectile(
                            self.player.x + self.player.width,
                            self.player.y + self.player.height // 2
                        )

                        self.projectiles.append(projectile)

            keys = pygame.key.get_pressed()

            self.player.update(keys)

            self.player.x = max(
                0,
                min(self.player.x, self.WIDTH - self.player.width)
            )

            self.player.y = max(
                0,
                min(self.player.y, self.HEIGHT - self.player.height)
            )

            # --------- Apparition ennemis ---------

            self.enemy_spawn_timer += 1

            if self.enemy_spawn_timer >= self.enemy_spawn_delay:

                enemy = Enemy(
                    self.WIDTH,
                    random.randint(0, self.HEIGHT - 40)
                )

                self.enemies.append(enemy)

                self.enemy_spawn_timer = 0

            # --------- Update ---------

            for projectile in self.projectiles:
                projectile.update()

            for enemy in self.enemies:
                enemy.update()

            # ------------------------------------------------------------------
            # Gestion des collisions entre les projectiles et les ennemis
            # ------------------------------------------------------------------

            projectiles_to_remove = []
            enemies_to_remove = []

            for projectile in self.projectiles:

                projectile_rect = pygame.Rect(
                    projectile.x,
                    projectile.y,
                    projectile.width,
                    projectile.height
                )

                for enemy in self.enemies:

                    enemy_rect = pygame.Rect(
                        enemy.x,
                        enemy.y,
                        enemy.width,
                        enemy.height
                    )

                    if projectile_rect.colliderect(enemy_rect):

                        projectiles_to_remove.append(projectile)
                        enemies_to_remove.append(enemy)

            # ------------------------------------------------------------------
            # Suppression des objets détruits et hors écran
            # ------------------------------------------------------------------

            self.projectiles = [
                projectile
                for projectile in self.projectiles
                if (
                    projectile not in projectiles_to_remove
                    and not projectile.is_outside_screen(self.WIDTH)
                )
            ]

            self.enemies = [
                enemy
                for enemy in self.enemies
                if (
                    enemy not in enemies_to_remove
                    and not enemy.is_outside_screen()
                )
            ]

            # --------- Draw ---------

            self.screen.fill((0, 0, 0))

            self.player.draw(self.screen)

            for projectile in self.projectiles:
                projectile.draw(self.screen)

            for enemy in self.enemies:
                enemy.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()