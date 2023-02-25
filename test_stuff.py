import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT)

#create PWM instance with frequency
pwm = GPIO.PWM(21, 100)

# start PWM of required Duty Cycle
pwm.start(15) 

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

print(f"Rotating for 0.1 second")
start = time.time_ns()
end = start + (1.0e9*0.1)

pwm.ChangeDutyCycle(1)
while time.time_ns() < end:
    pass
print("Done!")
pwm.ChangeDutyCycle(15)
pwm.stop()
