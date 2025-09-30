import serial
import visualization.radarneo as radarneo
import time

arduino = serial.Serial(port='COM4')
radar = radarneo.Radar(range_cm=10)

def run():
    while True:
        raw_data = arduino.readline().decode().rstrip('\n').split(',')
        angle, distance = int(raw_data[0]), int(raw_data[1])
        radar.update(angle, distance)
        time.sleep(0.01)

if __name__ == "__main__":
    run()