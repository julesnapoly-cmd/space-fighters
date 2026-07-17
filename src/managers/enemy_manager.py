import random
import pygame

from entities.basic_enemy import BasicEnemy
from entities.fast_enemy import FastEnemy


class EnemyManager:

    def __init__(self, screen_width, screen_height):

        self.enemies = []

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.spawn_delay = 1200
        self.last_spawn = 0

        # Types d'ennemis disponibles
        self.enemy_types = [
            BasicEnemy,
            FastEnemy
        ]

    def spawn_enemy(self, enemy):

        self.enemies.append(enemy)

    def spawn_random(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_spawn >= self.spawn_delay:

            enemy_class = random.choice(self.enemy_types)

            enemy = enemy_class(
                self.screen_width,
                random.randint(
                    0,
                    self.screen_height - 96
                )
            )

            self.spawn_enemy(enemy)

            self.last_spawn = current_time

    def get_enemies(self):

        return self.enemies

    def remove(self, enemy):

        if enemy in self.enemies:
            self.enemies.remove(enemy)
            
    def update(self):

        for enemy in self.enemies:
            enemy.update()

    def clean(self):

        self.enemies = [
            enemy
            for enemy in self.enemies
            if not enemy.is_outside_screen()
        ]

    def draw(self, screen):

        for enemy in self.enemies:
            enemy.draw(screen)