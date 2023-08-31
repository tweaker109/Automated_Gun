from pyfirmata import Arduino, util
import pyfirmata
import time

print("Homing Motors...")

board = Arduino('COM3')  # Replace 'COMX' with the actual serial port of your Arduino board

# Set home coordinates
home = 200

step_pin_x = 5
dir_pin_x = 2
en_pin_x = 8

step_pin_y = 9
dir_pin_y = 3
en_pin_y = 10

board.digital[step_pin_y].mode = pyfirmata.OUTPUT
board.digital[dir_pin_y].mode = pyfirmata.OUTPUT
board.digital[en_pin_y].mode = pyfirmata.OUTPUT
board.digital[en_pin_y].write(0)  # Set the EN pin LOW to enable the motor

board.digital[step_pin_x].mode = pyfirmata.OUTPUT
board.digital[dir_pin_x].mode = pyfirmata.OUTPUT
board.digital[en_pin_x].mode = pyfirmata.OUTPUT
board.digital[en_pin_x].write(0)  # Set the EN pin LOW to enable the motor

def home_motors(steps, delay_time):
    board.digital[dir_pin_x].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin_x].write(1)
        time.sleep(delay_time)
        board.digital[step_pin_x].write(0)
        time.sleep(delay_time)
    board.digital[dir_pin_y].write(1)  # Set the DIR pin HIGH to move in a particular direction
    for _ in range(steps):
        board.digital[step_pin_y].write(1)
        time.sleep(delay_time)
        board.digital[step_pin_y].write(0)
        time.sleep(delay_time)

# Home motors
home_motors(home, 0.0002)

print("Homing Completed")

board.exit()

