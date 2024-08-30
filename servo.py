import time
from servo import Servo

my_servo = Servo(pin_id=16)

delay_ms = 1 # define speed
range_angle = 150 # define distance

# define kicking mechanism 
def kick():
    for position in range(0, range_angle):
        print(position)
        my_servo.write(position)
        time.sleep_ms(delay_ms)
    
    for position in reversed(range(0, range_angle)):
        print(position)
        my_servo.write(position)
        time.sleep_ms(delay_ms)
        
        
kick()
