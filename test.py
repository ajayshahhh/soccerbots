#Include the library files
import time
from machine import Pin, freq, PWM
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

#Define the IR receiver pin and motor pins
pin_ir = Pin(8, Pin.IN)
ENA = PWM(Pin(2))
IN1 = Pin(3,Pin.OUT)
IN2 = Pin(4,Pin.OUT)
IN3 = Pin(5,Pin.OUT)
IN4 = Pin(6,Pin.OUT)
ENB = PWM(Pin(7))

# speed of this car
speed = 60000 # 0 - 65025
ENA.duty_u16(speed)
ENB.duty_u16(speed)

Up = 0
Down = 0
Left = 0
Right = 0
Stop = 0

def decodeKeyValue(data):
    return data
    
# User callback
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(data)
        if data == Up:
            forward()
        elif data == Down:
            backward()
        elif data == Left:
            left()
        elif data == Right:
            right()
        elif data == Stop:
            stop()

def forward():
    IN1.on()
    IN2.off()
    IN3.on()
    IN4.off()
    
def backward():
    IN1.off()
    IN2.on()
    IN3.off()
    IN4.on()
    
def left():
    IN1.on()
    IN2.off()
    IN3.off()
    IN4.on()
    
def right():
    IN1.off()
    IN2.on()
    IN3.on()
    IN4.off()
    
def stop():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()
        

ir = NEC_8(pin_ir, callback)  # Instantiate receiver
ir.error_function(print_error)  # Show debug information

try:
    while True:
        pass
except KeyboardInterrupt:
    ir.close()
