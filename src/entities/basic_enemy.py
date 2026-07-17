from entities.enemy import Enemy


class BasicEnemy(Enemy):

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            "/Users/Jules/Projects/space-fighters/assets/sprites/enemies/sprite_basic_enemy.png"
        )

        # --------------------------------------------------------------
        # Gameplay
        # --------------------------------------------------------------

        self.speed = 3
        self.score = 100