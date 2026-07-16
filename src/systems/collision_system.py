import pygame


class CollisionSystem:

    def update(
        self,
        player,
        projectile_manager,
        enemy_manager,
        explosion_manager
    ):

        destroyed_enemies = []

        # --------------------------------------------------------------
        # Collision Projectile <-> Ennemi
        # --------------------------------------------------------------

        for projectile in projectile_manager.get_projectiles():

            projectile_rect = pygame.Rect(
                projectile.x,
                projectile.y,
                projectile.width,
                projectile.height
            )

            for enemy in enemy_manager.get_enemies():

                enemy_rect = pygame.Rect(
                    enemy.x,
                    enemy.y,
                    enemy.width,
                    enemy.height
                )

                if projectile_rect.colliderect(enemy_rect):

                    projectile_manager.remove(projectile)
                    enemy_manager.remove(enemy)

                    explosion_manager.create(
                        enemy.x + enemy.width // 2,
                        enemy.y + enemy.height // 2
                    )

                    destroyed_enemies.append(enemy)

                    break

        # --------------------------------------------------------------
        # Collision Joueur <-> Ennemi
        # --------------------------------------------------------------

        player_rect = pygame.Rect(
            player.x,
            player.y,
            player.width,
            player.height
        )

        for enemy in enemy_manager.get_enemies()[:]:

            enemy_rect = pygame.Rect(
                enemy.x,
                enemy.y,
                enemy.width,
                enemy.height
            )

            if player_rect.colliderect(enemy_rect):

                enemy_manager.remove(enemy)

                explosion_manager.create(
                    enemy.x + enemy.width // 2,
                    enemy.y + enemy.height // 2
                )

        return destroyed_enemies