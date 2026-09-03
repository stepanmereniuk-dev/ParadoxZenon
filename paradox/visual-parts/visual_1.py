import pygame
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from logic.paradox_1 import calculer_etape


pygame.init()

# Fenêtre
LARGEUR = 1000
HAUTEUR = 300

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Achille et la Tortue")

clock = pygame.time.Clock()

# Police
font = pygame.font.SysFont("Arial", 24)

font_emoji = pygame.font.SysFont("Segoe UI Emoji", 40)

emoji_achille = font_emoji.render("🏃", True, (0, 0, 0))
emoji_tortue = font_emoji.render("🐢", True, (0, 0, 0))
emoji_achille = pygame.transform.flip(emoji_achille, True, False)

# Conditions initiales
pos_achille = 0
pos_tortue = 1

vit_achille = 10
vit_tortue = 1

etape = 0

animation = False

debut_achille = pos_achille
debut_tortue = pos_tortue

cible_achille = pos_achille
cible_tortue = pos_tortue

progression = 0

# Conversion des positions mathématiques en pixels
echelle = 400

running = True


while running:

    # Événements
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not animation:

                debut_achille = pos_achille
                debut_tortue = pos_tortue

                cible_achille, cible_tortue = calculer_etape(
                    pos_achille,
                    pos_tortue,
                    vit_achille,
                    vit_tortue
                )

                

                progression = 0
                animation = True

                etape += 1

                print(
                    etape,
                    pos_achille,
                    pos_tortue
                )

            if event.key == pygame.K_r:
                pos_achille = 0
                pos_tortue = 1

                debut_achille = pos_achille
                debut_tortue = pos_tortue

                cible_achille = pos_achille
                cible_tortue = pos_tortue

                progression = 0
                animation = False
                etape = 0    

        # Animation
    if animation:
        progression += 0.01

        if progression >= 1:
            progression = 1

        pos_affichee_achille = (
            debut_achille
            + (cible_achille - debut_achille) * progression
        )

        pos_affichee_tortue = (
            debut_tortue
            + (cible_tortue - debut_tortue) * progression
        )

        if progression == 1:
            pos_achille = cible_achille
            pos_tortue = cible_tortue
            animation = False

    else:
        pos_affichee_achille = pos_achille
        pos_affichee_tortue = pos_tortue            

    # Fond
    ecran.fill((255, 255, 255))

    # Piste
    pygame.draw.line(
        ecran,
        (80, 80, 80),
        (80, 210),
        (920, 210),
        4
    )

    # Ligne de départ
    pygame.draw.line(
        ecran,
        (0, 0, 0),
        (100, 175),
        (100, 245),
        2
    )

    # Conversion en pixels
    x_achille = 100 + int(pos_affichee_achille * echelle)
    x_tortue = 100 + int(pos_affichee_tortue * echelle)

    # Achille
    ecran.blit(
        emoji_achille,

        (x_achille - 20, 165)
    )

    # Tortue
    ecran.blit(
        emoji_tortue,
        (x_tortue - 20, 200)

    )

    # Textes
    texte_etape = font.render(
        f"Étape : {etape}",
        True,
        (0, 0, 0)
    )

    texte_achille = font.render(
        f"Achille : {pos_achille:.4f}",
        True,
        (0, 0, 0)
    )

    texte_tortue = font.render(
        f"Tortue : {pos_tortue:.4f}",
        True,
        (0, 0, 0)
    )

    texte_controles = font.render(
        "ESPACE : étape suivante   |   R : recommencer",
         True,
        (0, 0, 0)
    )

    ecran.blit(texte_controles, (500, 30))

    ecran.blit(texte_etape, (30, 30))
    ecran.blit(texte_achille, (30, 65))
    ecran.blit(texte_tortue, (30, 100))

    pygame.display.flip()

    clock.tick(60)


pygame.quit()