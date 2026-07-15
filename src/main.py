import pygame

from entities.player import Player


# Initialisation de Pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fighters")

player = Player()

running = True

while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lecture du clavier
    keys = pygame.key.get_pressed()

    # Mise à jour
    player.update(keys)

    # Contraintes temporaires (elles seront déplacées plus tard)
    if player.x < 0:
        player.x = 0

    if player.x > WIDTH - player.width:
        player.x = WIDTH - player.width

    if player.y < 0:
        player.y = 0

    if player.y > HEIGHT - player.height:
        player.y = HEIGHT - player.height

    # Dessin
    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()