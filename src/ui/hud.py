import pygame

from config.settings import (
    HUD_MARGIN,
    HUD_ICON_SIZE,
    HUD_ICON_SPACING,
    HUD_SCORE_Y
)


class Hud:

    def __init__(self, player, font):

        self.player = player
        self.font = font

        # --------------------------------------------------------------
        # Préparation de l'icône des vies (une seule fois)
        # --------------------------------------------------------------

        self.life_icon = pygame.transform.scale(
            self.player.image,
            (
                HUD_ICON_SIZE,
                HUD_ICON_SIZE
            )
        )

    # --------------------------------------------------------------
    # Dessin du HUD
    # --------------------------------------------------------------

    def draw(self, screen, score):

        # --------- Vies ---------

        for i in range(self.player.get_health()):

            screen.blit(
                self.life_icon,
                (
                    HUD_MARGIN + i * HUD_ICON_SPACING,
                    HUD_MARGIN
                )
            )

        # --------- Score ---------

        score_text = self.font.render(
            str(score),
            True,
            (255, 255, 255)
        )

        screen.blit(
            score_text,
            (
                screen.get_width()
                - score_text.get_width()
                - HUD_MARGIN,
                HUD_SCORE_Y
            )
        )