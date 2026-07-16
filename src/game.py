import pygame

from entities.player import Player

from managers.star_manager import StarManager
from managers.projectile_manager import ProjectileManager
from managers.explosion_manager import ExplosionManager
from managers.enemy_manager import EnemyManager

from systems.collision_system import CollisionSystem


class Game:

    def __init__(self):

        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Fighters")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", 28)

        # --------------------------------------------------------------
        # Joueur
        # --------------------------------------------------------------

        self.player = Player()

        # --------------------------------------------------------------
        # Managers
        # --------------------------------------------------------------

        self.star_manager = StarManager(
            self.WIDTH,
            self.HEIGHT
        )

        self.projectile_manager = ProjectileManager()

        self.enemy_manager = EnemyManager(
            self.WIDTH,
            self.HEIGHT
        )

        self.explosion_manager = ExplosionManager()

        # --------------------------------------------------------------
        # Systems
        # --------------------------------------------------------------

        self.collision_system = CollisionSystem()

        # --------------------------------------------------------------
        # Gameplay
        # --------------------------------------------------------------

        self.running = True

        self.score = 0

    def run(self):

        while self.running:

            # ==========================================================
            # Gestion des événements
            # ==========================================================

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        self.projectile_manager.fire(
                            self.player.x + self.player.width,
                            self.player.y + self.player.height // 2
                        )

            # ==========================================================
            # Lecture clavier
            # ==========================================================

            keys = pygame.key.get_pressed()

            self.player.update(keys)

            # Limites du joueur

            self.player.x = max(
                0,
                min(
                    self.player.x,
                    self.WIDTH - self.player.width
                )
            )

            self.player.y = max(
                0,
                min(
                    self.player.y,
                    self.HEIGHT - self.player.height
                )
            )

            # ==========================================================
            # Update
            # ==========================================================

            self.star_manager.update()

            self.projectile_manager.update()

            self.enemy_manager.spawn()
            self.enemy_manager.update()

            self.explosion_manager.update()

            destroyed_enemies = self.collision_system.update(
                self.player,
                self.projectile_manager,
                self.enemy_manager,
                self.explosion_manager
            )

            for enemy in destroyed_enemies:
                self.score += enemy.score

            self.projectile_manager.clean(self.WIDTH)
            self.enemy_manager.clean()
            self.explosion_manager.clean()

            # ==========================================================
            # Draw
            # ==========================================================

            self.screen.fill((0, 0, 0))

            self.star_manager.draw(self.screen)

            self.player.draw(self.screen)

            self.projectile_manager.draw(self.screen)

            self.enemy_manager.draw(self.screen)

            self.explosion_manager.draw(self.screen)

            score_text = self.font.render(
                f"Score : {self.score}",
                True,
                (255, 255, 255)
            )

            self.screen.blit(
                score_text,
                (20, 20)
            )

            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()