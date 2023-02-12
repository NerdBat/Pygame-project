import pygame

# Initialisation de la fenêtre
pygame.init()
screen = pygame.display.set_mode((1500, 950))

# Définition des obstacles
obstacle_list = []
obstacle_width = 100
obstacle_height = 50
for i in range(10):
    x = i * 150
    y = 450
    obstacle = pygame.Rect(x, y, obstacle_width, obstacle_height)
    obstacle_list.append(obstacle)

# Boucle principale du niveau
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de la position de l'obstacle
    for obstacle in obstacle_list:
        obstacle.x -= 5

    # Vérification des collisions avec les obstacles
    ...

    # Affichage des obstacles
    for obstacle in obstacle_list:
        pygame.draw.rect(screen, (0, 0, 0), obstacle)

    pygame.display.update()

# Terminaison de pygame
pygame.quit()
