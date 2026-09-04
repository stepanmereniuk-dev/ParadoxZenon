# Paradoxe d'Achille et de la tortue

## Context et problématique

Le paradoxe d'Achille et de la tortue est l'un des paradoxes de Zénon d'Élée.
Une tortue commence la course avec une avance sur Achille. Même si Achille
court plus vite, lorsqu'il atteint la position précédente de la tortue,
celle-ci a déjà avancé.


Le paradoxe suggère ainsi qu'Achille doit parcourir une infinité d'étapes
avant de pouvoir rattraper la tortue.

## Modélisation

Nous avons modélisé cette situation en Python.

Dans notre simulation, Achille commence à la position 0 et la tortue à la
position 1. La vitesse d'Achille est fixée à 10m/s et celle de la tortue à 1m/s.

À chaque étape, le programme :

1. calcule la distance entre Achille et la tortue:
distance = position_tortue - position_achille

2. calcule le temps nécessaire à Achille pour atteindre la position actuelle de la tortue: 
temps = distance/vitesse_achille

3. calcule la distance parcourue par la tortue pendant ce même temps, puis mettre à jour sa position:  distance_tortue = vitesse_tortue*temps
position_tortue = position_tortue + distance_tortue

4. place Achille à l'ancienne position de la tortue: 
position_achille = ancienne_position_tortue



## Résultats de la simulation

La simulation produit par exemple :

- Étape 1 : Achille = 1 ; Tortue = 1.1
- Étape 2 : Achille = 1.1 ; Tortue = 1.11
- Étape 3 : Achille = 1.11 ; Tortue = 1.111
- Étape 4 : Achille = 1.111 ; Tortue = 1.1111

Le programme affiche les 10 premières étapes, ce qui permet d'observer la convergence des positions d'Achille et de la tortue.

À chaque étape, la distance entre Achille et la tortue devient plus petite.

Les temps nécessaires à Achille pour effectuer les différentes étapes forment
une série géométrique :

0.1 + 0.01 + 0.001 + ...

Cette série converge vers 1/9. Une infinité d'étapes peut donc être réalisée
en un temps total fini.

Les positions convergent vers 10/9 ≈ 1.1111, qui correspond au point où
Achille rattrape la tortue.

La simulation permet ainsi d'illustrer que le paradoxe ne vient pas d'une
impossibilité physique de rattraper la tortue, mais de la division du
mouvement en une infinité d'étapes.

Une infinité d'etapes ne signifie donc pas une durée infinie.

## Visualisation avec Pygame

Une visualisation avec Pygame a été ajoutée afin de représenter graphiquement les différentes étapes de la simulation.

Achille et la tortue avancent selon les positions calculées dans `paradox_1.py`. La visualisation permet ainsi d'observer que la distance entre les deux devient de plus en plus petite à chaque étape.

### Contrôles

- `ESPACE` : lancer l'étape suivante
- `R` : recommencer la simulation

La logique mathématique et la visualisation sont séparées dans deux fichiers :
- `paradox_1.py` : calcul des positions
- `visual_1.py` : représentation graphique avec Pygame
