import logging
import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/0/250K'


logging.basicConfig(level=logging.ERROR)
distance = 0.2 #Change distance here

if __name__ == '__main__':
    try:
        print("Loading drivers")
        cflib.crtp.init_drivers(enable_debug_driver=False)
        with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
            with MotionCommander(scf) as mc:
                mc.forward(distance) #Fly forward
            scf.close_link()
    except Exception as e:
        print("Collecting information...")
        if str(e) == "Too many packets lost":
            print("Maybe quadrocopter turned off?")
        else:
            print(str(e))
