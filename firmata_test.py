from pyfirmata import Arduino, util
import pyfirmata
import time

board = Arduino('COM3')  # Replace 'COMX' with the actual serial port of your Arduino board

step_pin = 5
dir_pin = 2
en_pin = 8

board.digital[step_pin].mode = pyfirmata.OUTPUT
board.digital[dir_pin].mode = pyfirmata.OUTPUT
board.digital[en_pin].mode = pyfirmata.OUTPUT
board.digital[en_pin].write(0)  # Set the EN pin LOW to enable the motor

def step_motor(steps, delay_time):
    board.digital[dir_pin].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin].write(1)
        time.sleep(delay_time)
        board.digital[step_pin].write(0)
        time.sleep(delay_time)

    time.sleep(1)  # One second delay

    board.digital[dir_pin].write(0)  # Set the DIR pin LOW to change the direction of rotation
    for _ in range(steps):
        board.digital[step_pin].write(1)
        time.sleep(delay_time)
        board.digital[step_pin].write(0)
        time.sleep(delay_time)

    time.sleep(1)

step_motor(1600, 0.0002)  # Call the step_motor function with the desired number of steps and delay time

board.exit()

