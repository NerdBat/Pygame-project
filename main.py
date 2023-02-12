import pygame

# Initialisation de la fenêtre de jeu
pygame.init()
width, height = 1500, 950
screen = pygame.display.set_mode((width, height))

# Définition des couleurs utilisées
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Chargement des polices utilisées
font = pygame.font.Font(None, 30)

# Définition des boutons
play_button = pygame.Rect(width / 2 - 50, height / 2 - 25, 100, 50)
quit_button = pygame.Rect(width / 2 - 50, height / 2 + 25, 100, 50)
info_button = pygame.Rect(width / 2 - 150, height / 2 + 75, 300, 50)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Détection de clics sur les boutons
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            if play_button.collidepoint(mouse_pos):
                # Code pour lancer le jeu
                pass
            elif quit_button.collidepoint(mouse_pos):
                running = False
            elif info_button.collidepoint(mouse_pos):
                # Code pour afficher le message
                pass

    # Affichage des boutons
    screen.fill(white)
    pygame.draw.rect(screen, black, play_button)
    pygame.draw.rect(screen, black, quit_button)
    pygame.draw.rect(screen, black, info_button)

    # Ajout du texte aux boutons
    play_text = font.render("Lancer le jeu", True, white)
    quit_text = font.render("Quitter", True, white)
    info_text = font.render("J'ai été codé sans l'aide de Chat GPT", True, red)

    screen.blit(play_text, (width / 2 - 40, height / 2 - 10))
    screen.blit(quit_text, (width / 2 - 35, height / 2 + 40))
    screen.blit(info_text, (width / 2 - 145, height / 2 + 90))

    pygame.display.update()
# Définition des niveaux
levels = ['level1.py', 'level2.py', 'level3.py']
current_level = 0

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Détection de clics sur les boutons
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            if play_button.collidepoint(mouse_pos):
                # Chargement du niveau actuel
                exec(open(levels[current_level]).read())
            elif quit_button.collidepoint(mouse_pos):
                running = False
            elif info_button.collidepoint(mouse_pos):
                # Code pour afficher le message
                pass
    # Affichage de l'interface du jeu
    ...

# Terminaison de pygame
pygame.quit()

# Terminaison de pygame
pygame.quit()
