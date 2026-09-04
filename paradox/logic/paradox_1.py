
def calculer_etape(pos_achille, pos_tortue, vit_achille, vit_tortue):
    pos_tortue_0 = pos_tortue

    dis = pos_tortue - pos_achille
    temps = dis / vit_achille

    dis_tortue = vit_tortue * temps
    pos_tortue += dis_tortue

    pos_achille = pos_tortue_0

    return pos_achille, pos_tortue


if __name__ == "__main__":

    pos_achille = 0
    pos_tortue = 1
    vit_achille = 10
    vit_tortue = 1

    for i in range(10):
        pos_achille, pos_tortue = calculer_etape(
        pos_achille,
        pos_tortue,
        vit_achille,
        vit_tortue
       )

        print(f"Étape {i + 1}: Achille = {pos_achille}, Tortue = {pos_tortue}")


