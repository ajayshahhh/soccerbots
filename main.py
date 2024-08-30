import machine
import utime #importing time
from servo import Servo #importing servo 


#Defining UART channel and Baud Rate
uart = machine.UART(0,9900)

LED = machine.Pin("LED", machine.Pin.OUT)
IN1 = machine.Pin(21, machine.Pin.OUT)
IN2 = machine.Pin(20, machine.Pin.OUT)
IN3 = machine.Pin(19, machine.Pin.OUT)
IN4 = machine.Pin(18, machine.Pin.OUT)

def motor_forward():
    LED.toggle()
    IN1.on()
    LED.toggle()
    IN2.off()
    LED.toggle()
    IN3.off()
    LED.toggle()
    IN4.on()

# Define a function to move the motor backward
def motor_backward():
    IN1.off()
    LED.toggle()
    IN2.on()
    LED.toggle()
    IN3.on()
    LED.toggle()
    IN4.off()
    
def motor_left():
    LED.toggle()
    IN1.on()
    LED.toggle()
    IN2.off()
    LED.toggle()
    IN3.on()
    LED.toggle()
    IN4.off()

def motor_right():
    LED.toggle()
    IN1.off()
    LED.toggle()
    IN2.on()
    LED.toggle()
    IN3.off()
    LED.toggle()
    IN4.on()

def stop():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()

def party():
    motor_forward()
    utime.sleep(1)
    motor_backward()
    utime.sleep(1)
    motor_left()
    utime.sleep(3)
    motor_right()
    utime.sleep(3)
    stop()

my_servo = Servo(pin_id=16)
delay_ms = 1 # define speed
range_angle = 150 # define distance

def kick():
    for position in range(0, range_angle):
        print(position)
        my_servo.write(position)
        utime.sleep_ms(delay_ms)
    
    for position in reversed(range(0, range_angle)):
        print(position)
        my_servo.write(position)
        utime.sleep_ms(delay_ms)

while True:
    if uart.any(): #Checking if data available
        data_raw=uart.read() #Getting data
        data_raw=str(data_raw) #Converting bytes to str type
        data_raw = data_raw.split("'")
        data_raw = data_raw[1]
        data_raw = str(data_raw)
        data_raw = data_raw.split("\\")
        data = data_raw[0]
        print(data)
        if('forward' in data):
            motor_forward() #Forward
        elif('backward' in data):
            motor_backward() #Backward
        elif('right' in data):
            motor_right() #Turn Right
        elif('left' in data):
            motor_left() #Turn Left
        elif('kick' in data):
            kick() #Kicking Mechanism
        elif("stop" in data):
            stop() #Stop
        elif("party" in data):
            party() #Bonus
        else:
            stop() #Stop
        
        
    
