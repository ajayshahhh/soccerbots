from machine import Pin, PWM, UART
import time

# Find Baud Rate for Pico W
uart = UART(0, 9600)
# Experiment with Power Levels
POWER_LEVEL = 0 # Change Later
# Change Pins Later
RIGHT_FORWARD_PIN = p1
RIGHT_REVERSE_PIN = p2
LEFT_FORWARD_PIN = p3
LEFT_REVERSE_PIN = p4

right_forward = PWM(Pin(RIGHT_FORWARD_PIN))
right_reverse = PWM(Pin(RIGHT_REVERSE_PIN))
left_forward = PWM(Pin(LEFT_FORWARD_PIN))
left_reverse = PWM(Pin(LEFT_REVERSE_PIN))


def spin_wheel(pwm):
        pwm.duty_u16(POWER_LEVEL)
        time.sleep(3)
        pwm.duty_u16(0)
        time.sleep(2)

while True:
    if uart.any():
        command = uart.readline()
        print(command)