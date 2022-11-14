import BNOInterface
import time

bno = BNOInterface.BNOInterface()


while True:
    grav = bno.get_gravity()
    grav_x = grav[0]
    grav_y = grav[1]
    grav_z = grav[2]

    print(f'Gravity x : {grav_x}')
    print(f'Gravity y : {grav_y}')
    print(f'Gravity z : {grav_z}')

    time.sleep(5)

