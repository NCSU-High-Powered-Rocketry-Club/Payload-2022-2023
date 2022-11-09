import board
import busio
import adafruit_bno055


class BNOInterface:
    """
    This class can be used to pull all the information from the BNO055. You can
    initialize this class by classing `sensor = BNOInterface()`.
    """

    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)

    def get_acceleration(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z axis accelerometer values in meters per
        second squared.
        """
        return self.sensor.acceleration
    
    def get_linear_acceleration(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z linear acceleration values (i.e. without
        effect of gravity) in meters per second squared.
        """
        return self.sensor.linear_acceleration

    def get_gravity(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z gravity acceleration values (i.e. without
        the effect of linear acceleration) in meters per second squared.
        """
        return self.sensor.gravity
    
    def get_euler(self) ->  tuple:
        """
        This is a 3-tuple of orientation Euler angle values.
        """
        return self.sensor.euler

    def get_quaternion(self) -> tuple:
        """
        This is a 4-tuple of orientation quaternion values.
        """
        return self.sensor.quaternion

    def get_magnetic(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z axis magnetometer values in micro-teslas.
        """
        return self.sensor.magnetic

    def get_gyro(self) -> tuple:
        """
        This is a 3-tuple of X, Y, Z axis gyroscope values in degrees per
        second.
        """
        return self.sensor.gyro

    def get_temperature(self) -> float:
        """
        The sensor temperature in degrees Celsius.
        """
        return self.sensor.temperature
