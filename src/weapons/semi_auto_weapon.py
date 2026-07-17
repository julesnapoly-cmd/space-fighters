from weapons.weapon import Weapon


class SemiAutoWeapon(Weapon):

    def __init__(self):

        self.trigger_released = True

    def update(
        self,
        is_trigger_pressed,
        player,
        projectile_manager
    ):

        # Un seul tir par appui

        if is_trigger_pressed and self.trigger_released:

            projectile_manager.fire(
                player.x + player.width,
                player.y + player.height // 2
            )

            self.trigger_released = False

        if not is_trigger_pressed:

            self.trigger_released = True