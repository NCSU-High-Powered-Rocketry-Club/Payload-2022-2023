import board
import busio
import adafruit_bno055
import time


class BNOInterface:
    """
    This class can be used to pull all the information from the BNO055. You can
    initialize this class by classing `sensor = BNOInterface()`.
    """

    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x28)

    def get_acceleration(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z axis accelerometer values in meters per
        second squared.
        """
        while True:
            # only break once any of the values are not 0
            if not all(val == 0 for val in self.sensor.acceleration):
                break
        return self.sensor.acceleration
    
    def get_linear_acceleration(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z linear acceleration values (i.e. without
        effect of gravity) in meters per second squared.
        """
        while True:
            # only break once any of the values are not 0
            if not all(val == 0 for val in self.sensor.linear_acceleration):
                break
        return self.sensor.linear_acceleration

    def get_gravity(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z gravity acceleration values (i.e. without
        the effect of linear acceleration) in meters per second squared.
        """
        # this is the initialized value of gravity for the IMU
        initial_gravity = 9.8
        # counter in case IMU is perfectly level
        counter = 0
        while counter < 100:
            # only break once any of the values are not 0
            if not all(val == 0.0 for val in self.sensor.gravity):
                if self.sensor.gravity[2] != initial_gravity:
                    break
            counter += 1
        return self.sensor.gravity
    
    def get_euler(self) ->  tuple:
        """
        This is a 3-tuple of orientation Euler angle values.
        """
        while True:
            # only break once any of the values are not 0
            if not all(angle == 0.0 for angle in self.sensor.euler):
                break
        return self.sensor.euler

    def get_quaternion(self) -> tuple:
        """
        This is a 4-tuple of orientation quaternion values.
        """
        while True:
            # only break once any of the values are not 0
            if not all(angle == 0.0 for angle in self.sensor.quaternion):
                break
        return self.sensor.quaternion

    def get_magnetic(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z axis magnetometer values in micro-teslas.
        """
        while True:
            # only break once any of the values are not 0.0
            if not all(mag == 0 for mag in self.sensor.magnetic):
                break
        return self.sensor.magnetic

    def get_gyro(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z axis gyroscope values in degrees per
        second.
        """
        while True:
            # only break once any of the values are not 0
            if not all(val == 0.0 for val in self.sensor.gyro):
                break
        return self.sensor.gyro

    def get_temperature(self) -> float:
        """
        The sensor temperature in degrees Celsius. The
        """
        while self.sensor.temperature < 0:
            continue
        return self.sensor.temperature
