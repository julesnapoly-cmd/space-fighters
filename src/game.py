import pygame

from entities.player import Player

from managers.star_manager import StarManager
from managers.projectile_manager import ProjectileManager
from managers.explosion_manager import ExplosionManager
from managers.enemy_manager import EnemyManager
from systems.collision_system import CollisionSystem
from weapons.auto_weapon import AutoWeapon
from config.game_state import PLAYING, GAME_OVER
from ui.hud import Hud

class Game:


    def __init__(self):

        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60
        self.game_state = PLAYING

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Fighters")

        self.clock = pygame.time.Clock()

       
        self.font = pygame.font.Font(
             "/Users/Jules/Projects/space-fighters/assets/fonts/PressStart2P-Regular.ttf",
            16
        )
    
        # --------------------------------------------------------------
        # Joueur
        # --------------------------------------------------------------

        self.player = Player()


        # --------------------------------------------------------------
        # Interface (HUD)
        # --------------------------------------------------------------

        self.hud = Hud(
            self.player,
            self.font
        )

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
        # --------------------------------------------------------------
        # Test de l'arme automatique
        # --------------------------------------------------------------

        self.player.weapon = AutoWeapon()

    def update(self):

            if self.game_state == GAME_OVER:
                return

            keys = pygame.key.get_pressed()

            is_trigger_pressed = keys[pygame.K_SPACE]



            self.player.update(keys)
            self.player.shoot(
                is_trigger_pressed,
                self.projectile_manager
            )
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

            self.enemy_manager.spawn_random()
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

            if self.player.is_dead():

                self.game_state = GAME_OVER

            self.projectile_manager.clean(self.WIDTH)
            self.enemy_manager.clean()
            self.explosion_manager.clean()

    def draw(self):
            # ==========================================================
            # Draw
            # ==========================================================

            self.screen.fill((0, 0, 0))

            self.star_manager.draw(self.screen)

            self.player.draw(self.screen)
            self.projectile_manager.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            self.explosion_manager.draw(self.screen)

            self.hud.draw(
                self.screen,
                self.score
            )

            if self.game_state == GAME_OVER:

                title = self.font.render(
                    "GAME OVER",
                    True,
                    (255, 0, 0)
                )

                retry = self.font.render(
                    "Press R to Retry",
                    True,
                    (255, 255, 255)
                )

                self.screen.blit(
                    title,
                    (
                        self.WIDTH // 2 - title.get_width() // 2,
                        220
                    )
                )

                self.screen.blit(
                    retry,
                    (
                        self.WIDTH // 2 - retry.get_width() // 2,
                        280
                    )
                )

            pygame.display.flip()


    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if (
                self.game_state == GAME_OVER
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_r
            ):

                self.__init__()
                
    def run(self):

       

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(self.FPS)

        pygame.quit()
           

           
