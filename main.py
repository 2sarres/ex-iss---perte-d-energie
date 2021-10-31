from sense_hat import SenseHat  # on importe le module sense hat
import time  # on importe le module time
import datetime  # on importe le module datetime
import random  # on importe le module random

s = SenseHat()  # on definie la variable s à SenseHat()

color = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (200, 10, 80)]  # on definie la liste color a plusieurs valeurs rgb

compteur1 = 0  # on definie la variable compteur1 à 0
compteur2 = 0  # on definie la variable compteur2 à 0
compteur3 = 0  # on definie la variable compteur3 à 0

resultat1L = []  # on definie la liste resultat1L à   (à rien)
resultat2L = []  # on definie la liste resultat2L à   (à rien)
resultatF = 0  # on definie la variable resultatF à 0
tempL = [0]  # on definie la liste tempL à 0
nowL = []  # on definie la liste nowL à   (à rien)


def led():  # on definie la fonction led
    B = random.choice(color)  # on definie la variable B à un element aleatoire de la liste color
    O = (0, 0, 0)  # on definie la variable O à la valeur rgb 0,0,0
    pix = [  # d'ici
        B, O, O, O, O, O, O, B,
        O, B, O, O, O, O, B, O,
        O, O, B, O, O, B, O, O,
        O, O, O, B, B, O, O, O,  # on definie la liste pix
        O, O, O, B, B, O, O, O,  # à la variable B ou la variable O
        O, O, B, O, O, B, O, O,
        O, B, O, O, O, O, B, O,
        B, O, O, O, O, O, O, B,
    ]  # à ici
    return pix  # on retourne la liste pix


file = open("data.csv", "a")  # on ouvre (et crée si le fichier n'etait pas encore crée) le fichier data.csv et on definie ce fichier a la variable fichier
file.write("date, temperature, humiditer \n")  # on ecrie dans ce fichier : 'date, temperature, humiditer' et on fait un retoure a la ligne
file.close()  # on ferme ce fichier

file = open("calorie.csv", "a")  # on ouvre (et crée si le fichier n'etait pas encore crée) le fichier calorie.csv et on definie ce fichier a la variable fichier
file.write("date, calories" + "\n") # on ecrie dans ce fichier : 'date, calorie' et on fait un retoure a la ligne
file.close()  # on ferme ce fichier

red = (255, 0, 0)  # on definie la variable red a la valeur rgb du rouge

start_time = datetime.datetime.now()  # on definie la variable start_time a l'heure minute seconde actuelle
now_time = datetime.datetime.now()  #on definie la variable now_time a l'heure minute seconde actuelle

while now_time < start_time + datetime.timedelta(minutes=179):  # tant que la variable now_time (temps actuelle) et plus petite que la variable start_time (temps du debut du programme) + 172 minutes (soit 2h59) alors on repete :
    s.set_pixels(led())  # on execute la fonction led et afficher les pixel de la liste pix retourner par la fonction led sur les led du sense hat

    temp = s.get_temperature()  # on definie la variable temp a la temperature en degras celcus du capteur de temperature du sense hat
    tempL.append(temp)  # on ajoute a la liste tempL la variable temp
    temp = repr(temp)  # on definie la variable temp a la variable temp transformer en chaine de caracteres

    now = datetime.datetime.now()  # on definie la variable now a l'annee, jour, mois, heure, minute, seconde, milliseconde
    now = str(now)  # on definie la variable now a la variable now transformer en chaine de caracteres
    nowL.append(now)  # on ajoute la variable now a la liste nowL

    humidity = s.get_humidity()  # on definie la variable humidity a l'humiditee en pourcent du capteur d'humiditer du sense hat
    humidity = str(humidity)  # on definie la variable humidity au conteue de la variable humidity transformer en chaine de caracteres

    file = open("data.csv", "a")  # on ouvre le fichier data.csv et on definie ce fichier a la variable fichier
    file.write(now + ", " + temp + ", " + humidity + "\n")  # on ecri dans ce fichier : la variable now ',' la variable temp ',' la variable humidity et on fait un retour a la ligne
    file.close()  # on ferme ce fichier

    time.sleep(600)  # on attend 600 secondes (soit 10 minutes)
    now_time = datetime.datetime.now()  # on definie la variable now_time a l'heure minute seconde actuelle

    compteur1 += 1  # on definie la variable compteur1 a la variable compteur1 + 1

compteur1 -= 1  # on definie la variable compteur1 a la variable compteur1 - 1

while compteur2 <= compteur1:  # tant que la variable compteur2 et plus petit ou egale a la variable compteur1 alors on repete :

    while compteur3 <= compteur1:  # tant que la variable compteur3 et plus petit ou egale a la variable compteur1 alors on repete :

        if tempL[compteur3] < tempL[compteur3 + 1]:  # si l'objet numero variable compteur3 de la liste tempL est plus petite que l'objet numero variable compteur3 de la liste tempL + 1 alors:
            resultat1L.append(tempL[compteur3 + 1] - tempL[compteur3])  # on ajoute l'objet numero varible compteur3 de la liste tempL  + 1 - l'objet numero variable compteur3 de la liste tempL a la liste resultat1L

        else:  # sinon
            resultat1L.append(tempL[compteur3] - tempL[compteur3 + 1])  # on ajoute l'objet numero varible compteur3 de la liste tempL - l'objet numero variable compteur3 de la liste tempL + 1 a la liste resultat1L

        resultat2L.append(2 * resultat1L[compteur3])  # on ajoute l'objet numero compteur3 de la liste resultat1L * 2 a la liste resultat2L (calcule factise)

        compteur3 += 1  # on definie la variable compteur3 a la variable compteur3 + 1

    file = open("calorie.csv", "a")  # on ouvre le fichier data.csv et on definie ce fichier a la variable fichier
    file.write(nowL[compteur2] + ", " + repr(resultat2L[compteur2]) + "\n")  # on ecrit dans ce fichier : objet numero variable compteur2 de la liste nowL ',' l'objet numero compteur2 de la liste resultat2L transformer en chaine de caracteres et on fait un retour a la ligne
    file.close()  # on ferme ce fichier
    compteur2 += 1  # on definie la variable compteur2 a la variable compteur2 + 1

resultatF = sum(resultat2L)  # on definie la variable resultatF a l'addition de tous les objet de la liste resultat2L

file = open("calorie.csv", "a")  # on ouvre le fichier calorie.csv et on definie ce fichier a la variable fichier
file.write(", total" + "\n")  # on ecrie dans ce fichier : ', total' et on fait un retour a la ligne
file.write(", " + str(resultatF) + "\n")  # on ecrie dans ce fichier : ',' la variable resultatF transformer en chaine de caracteres et on fit un retour a la ligne
file.close()  # on ferme ce fichier
s.show_message('experience terminer', text_colour=red)  # on affiche le message 'experience terminer' sur les led du sense hat
s.clear()  # on efface etein toutes les led du sense hat
