import logging
import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/0/250K'


logging.basicConfig(level=logging.ERROR)
distance = 0.2 #Change distance here
time_delay = 1 #Change to increase/decrease time delay. 

if __name__ == '__main__':
    try:
        print("Loading drivers")
        cflib.crtp.init_drivers(enable_debug_driver=False)
        print('Scanning interfaces for Crazyflies...')
        available = cflib.crtp.scan_interfaces()
        print('Crazyflies found:')
        for i in available:
            print(i[0])
        with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
            with MotionCommander(scf) as mc:
                mc.forward(distance) #Fly forward
                time.sleep(time_delay)
                mc.right(distance) #Fly right
                time.sleep(time_delay)
                mc.back(distance) #Fly back
                time.sleep(time_delay)
                mc.left(distance) #Fly left
                time.sleep(time_delay)
            scf.close_link()
    except Exception as e:
        print("Collecting information...")
        if str(e) == "Too many packets lost":
            print("Maybe quadrocopter turned off?")
        else:
            print(str(e))
