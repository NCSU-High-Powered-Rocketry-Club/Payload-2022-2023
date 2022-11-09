import board
import adafruit_bno055


class BNOInterface:
    """
    This 
    """

    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)

    def get_acceleration():
        """
        This is a 3-tuple of X, Y, Z axis accelerometer values in meters per
        second squared.
        """
        return self.sensor.acceleration
    
    def get_linear_acceleration():
        """
        This is a 3-tuple of X, Y, Z linear acceleration values (i.e. without
        effect of gravity) in meters per second squared.
        """
        return self.sensor.linear_acceleration

    def get_magnetic():
        """
        This is a 3-tuple of X, Y, Z axis magnetometer values in micro-teslas.
        """
        return self.sensor.magnetic

    
    

