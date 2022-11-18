from BNOInterface import BNOInterface
import time


sensor = BNOInterface()

while True:
    print(f"Accelerometer (m/s^2): {sensor.get_acceleration()}")
    print(f"Magnetometer (microteslas): {sensor.get_magnetic()}")
    print(f"Gyroscope (rad/sec): {sensor.get_gyro()}")
    print(f"Euler angle: {sensor.get_euler()}")
    print(f"Quaternion: {sensor.get_quaternion()}")
    print(f"Linear acceleration (m/s^2): {sensor.get_linear_acceleration()}")
    print(f"Gravity (m/s^2): {sensor.get_gravity()}")
    print()
    time.sleep(1)
