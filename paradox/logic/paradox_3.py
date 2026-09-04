import time
import random
import math

# def paradox_32 ():
#     zenon_dis = int(input("entrer le nombre de fois ou nous allons observer la fleche entre le point A et le point B : ")) 
#     distance_cible = int(input("entrer la distance entre le point A et le point B : "))
#     x = float(random.randint(0, distance_cible))
#     s_start = 0
#     d_distance_div = 0.5
#     F_arrive = 1
#     while s_start <= F_arrive:
        
#         s_start= s_start + d_distance_div
#         d_distance_div = d_distance_div/2
#         time.sleep(1)
#         print(s_start)
#         pass
#         if F_arrive == 1 :    
#             return print("la fleche touche la cible")

#     for i in range (zenon_dis) :
#         Position_fleche = x
#         t_initial = 0
#         t_final = 1
#         x_initial = 0
#         x_final = Position_fleche
#         delta_T = t_final - t_initial
#         delta_x = x_final - x_initial
#         v = delta_x / delta_T
        
#         print("position de la fleche x =  ", Position_fleche)
#         print("distance parcourue = ", delta_x)
#         print("vitesse de la fleche = ", v)
#         print("zenon conclut que la fleche ne bouge pas")
#         print(   "......>>--->   "  )

        


def paradox_3():
    distance1 = 0
    distance2 = int(input("entrer la distance entre le point A et le point B en mètres : "))
    time1 = 0
    time2 = int(input("choisir quand observer la fleche entre le point A et le point B (en secondes) : "))
    vitesse = (distance2 - distance1) / (time2 - time1)

    for i in range(5):
        time.sleep(1)
        
        print("....."*i,">>--->   ")

    print("vitesse de la fleche = ", vitesse, "m/s ce qui prouve que la fleche bouge")

paradox_3()

         
        
