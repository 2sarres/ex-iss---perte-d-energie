from sense_hat import SenseHat
import time
import datetime
import random

s = SenseHat()

color = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (200, 10, 80)]

compteur1 = 0
compteur2 = 0
compteur3 = 0

resultat1L = []
resultat2L = []
resultatF = 0
tempL = [0]
nowL = []

def led():
    B = random.choice(color)
    O = (0, 0, 0)
    pix = [
        B, O, O, O, O, O, O, B,
        O, B, O, O, O, O, B, O,
        O, O, B, O, O, B, O, O,
        O, O, O, B, B, O, O, O,
        O, O, O, B, B, O, O, O,
        O, O, B, O, O, B, O, O,
        O, B, O, O, O, O, B, O,
        B, O, O, O, O, O, O, B,
    ]
    return pix

file = open("data.csv", "a")
file.write("date, temperature, humiditer \n")
file.close()

file = open("calorie.csv", "a")
file.write("date, calories" + "\n")
file.close()

red = (255, 0, 0)
blue = (0, 0, 255)

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()

while now_time < start_time + datetime.timedelta(minutes=179):
    s.set_pixels(led())

    temp = s.get_temperature()
    tempL.append(temp)
    temp = repr(temp)


    now = datetime.datetime.now()
    now = str(now)
    nowL.append(now)



    humidity = s.get_humidity()
    humidity = str(humidity)

    file = open("data.csv", "a")
    file.write(now + ", " + temp + ", " + humidity + "\n")
    file.close()

    time.sleep(600)
    now_time = datetime.datetime.now()

    compteur1 += 1

compteur1 -= 1

while compteur2 <= compteur1 :

    while compteur3 <= compteur1:

        if tempL[compteur3] < tempL[compteur3 + 1]:
            resultat1L.append(tempL[compteur3 + 1] - tempL[compteur3])

        else:
            resultat1L.append(tempL[compteur3] - tempL[compteur3 + 1])

        
        resultat2L.append( 2 * resultat1L[compteur3])
        
        compteur3 += 1

    file = open("calorie.csv", "a")
    file.write(nowL[compteur2] + ", " + repr(resultat2L[compteur2]) + "\n")
    file.close()
    compteur2 += 1

resultatF = sum(resultat2L)

file = open("calorie.csv", "a")
file.write(", " + "total" + "\n")
file.write(", " + str(resultatF) + "\n")
file.close()
s.show_message('experience terminer', text_colour = red)
s.clear()



