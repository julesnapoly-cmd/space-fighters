from weapons.weapon import Weapon


class AutoWeapon(Weapon):

    def __init__(self):

        self.cooldown = 0
        self.fire_rate = 8

    def update(
        self,
        is_trigger_pressed,
        player,
        projectile_manager
    ):

        if self.cooldown > 0:
            self.cooldown -= 1

        if is_trigger_pressed and self.cooldown == 0:

            projectile_manager.fire(
                player.x + player.width,
                player.y + player.height // 2
            )

            self.cooldown = self.fire_rate