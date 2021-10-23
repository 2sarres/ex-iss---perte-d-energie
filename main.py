from sense_hat import SenseHat
import time
import datetime
import random

s = SenseHat()

color = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (200, 10, 80)]

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
file.write("date" + ", " + "temperature" + ", " + "humiditer" + "\n")
file.close()

red = (255, 0, 0)
blue = (0, 0, 255)

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()

while now_time < start_time + datetime.timedelta(hours=3):
    s.set_pixels(led())

    temp = s.get_temperature()
    temp = repr(temp)

    now = datetime.datetime.now()
    now = str(now)

    humidity = s.get_humidity()
    humidity = str(humidity)

    file = open("data.txt", "a")
    file.write(now + ", " + temp + ", " + humidity + "\n")
    file.close()

    time.sleep(600)
    now_time = datetime.datetime.now()










