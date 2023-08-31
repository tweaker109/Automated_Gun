from pyfirmata import Arduino, util
import pyfirmata
import time

print("Solenoid Actuation")

board = Arduino('COM3')  # Replace 'COMX' with the actual serial port of your Arduino board

trigger = 12

def actuate_solenoid(pin, duration):
    board.digital[pin].mode = pyfirmata.OUTPUT
    board.digital[pin].write(1)  # Activate the solenoid
    time.sleep(duration)
    board.digital[pin].write(0) # Deactivate the solenoid

# Actuate solenoid
actuate_solenoid(trigger, 1.5)

board.exit()