import pygame

# Démarre Pygame
pygame.init()

# Taille de la fenêtre
WIDTH = 800
HEIGHT = 600

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Titre de la fenêtre
pygame.display.set_caption("Space Fighters")

# Variable qui contrôle la boucle du jeu
running = True

# Boucle principale
while running:

    # Lecture des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fond noir
    screen.fill((0, 0, 0))

    # Affichage
    pygame.display.flip()

# Fermeture propre
pygame.quit()
