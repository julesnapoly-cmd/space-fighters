from entities.enemy import Enemy


class FastEnemy(Enemy):

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            "/Users/Jules/Projects/space-fighters/assets/sprites/enemies/sprite_fast_enemy.png"
        )

        self.speed = 6
        self.score = 200