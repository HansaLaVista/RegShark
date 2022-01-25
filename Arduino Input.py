import serial


def input():
    arduino = serial.Serial('COM3', 115200)

    check = True
    while check:
        arduino_data = arduino.readline().decode('ascii').strip()
