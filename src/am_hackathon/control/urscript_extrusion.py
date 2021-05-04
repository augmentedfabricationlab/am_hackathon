import sys, time
sys.path.append("C:/Users/Gido/Documents/workspace/development/ur_fabrication_control/src")

from ur_fabrication_control.direct_control import URScript
from .extruder_mixins import ExtruderMixins

__all__ = [
    "URScript_Extrusion",
    "stop_extruder",
    "set_extruder_digital_out",
    "toggle_fan",
    "toggle_air",
    "toggle_drv8825",
    "toggle_extruder",
    "set_extruder_data",
    "get_extruder_info"
]      

class URScript_Extrusion(ExtruderMixins, URScript):
    def __init__(self, ur_ip = None, ur_port = None, ext_ip = None, ext_port = None):
        super(URScript_Extrusion, self).__init__(ur_ip, ur_port)
        self.ext_setup(ext_ip, ext_port)

def __wrap(func, *args, **kwargs):
    urscript = URScript_Extrusion(*args)
    urscript.start()
    urscript.open_socket_extruder()
    func(urscript, **kwargs)
    urscript.close_socket_extruder()
    urscript.end()
    urscript.generate()
    urscript.send_script()
    return urscript

def stop_extruder(ur_ip, ur_port, ext_ip, ext_port):
    urscript = __wrap(URScript_Extrusion.stop_extruder, ur_ip, ur_port, ext_ip, ext_port)

def set_extruder_digital_out(ur_ip, ur_port, ext_ip, ext_port, pin=0, state=0, wait_for_response = True):
    urscript = __wrap(URScript_Extrusion.set_extruder_digital_out, ur_ip, ur_port, ext_ip, ext_port, pin=pin, state=state, wait_for_response = wait_for_response)

def toggle_fan(ur_ip, ur_port, ext_ip, ext_port, pin=34, state=0, wait_for_response = True):
    urscript = __wrap(URScript_Extrusion.toggle_fan, ur_ip, ur_port, ext_ip, ext_port, pin=pin, state=state, wait_for_response = wait_for_response)

def toggle_air(ur_ip, ur_port, ext_ip, ext_port, pin=32, state=0, wait_for_response = True):
    urscript = __wrap(URScript_Extrusion.toggle_air, ur_ip, ur_port, ext_ip, ext_port, pin=pin, state=state, wait_for_response = wait_for_response)

def toggle_drv8825(ur_ip, ur_port, ext_ip, ext_port, pin=30, state=0, wait_for_response = True):
    urscript = __wrap(URScript_Extrusion.toggle_drv8825, ur_ip, ur_port, ext_ip, ext_port, pin=pin, state=state, wait_for_response = wait_for_response)

def toggle_extruder(ur_ip, ur_port, ext_ip, ext_port, state=0, wait_for_response = True):
    urscript = __wrap(URScript_Extrusion.toggle_extruder, ur_ip, ur_port, ext_ip, ext_port, state=state, wait_for_response = wait_for_response)

def set_extruder_data(ur_ip, ur_port, ext_ip, ext_port, motor_id, state, max_speed, speed, acceleration):
    urscript = __wrap(URScript_Extrusion.set_extruder_data, ur_ip, ur_port, ext_ip, ext_port, motor_id=motor_id, state=state, max_speed=max_speed, speed=speed, acceleration=acceleration)

def get_extruder_info(ur_ip, ur_port, ext_ip, ext_port, wait_for_response = True):
    urscript = __wrap(URScript_Extrusion.get_extruder_info, ur_ip, ur_port, ext_ip, ext_port, wait_for_response = wait_for_response)

if __name__ == "__main__":
    #get_extruder_info("192.168.10.20",30002,"192.168.10.50",50004)
    stop_extruder("192.168.10.20",30002,"192.168.10.50",50004)
    # time.sleep(2)
    toggle_fan("192.168.10.20", 30002, "192.168.10.50", 50004, state=1, wait_for_response = False)
    # time.sleep(2)
    # toggle_air("192.168.10.20", 30002, "192.168.10.50", 50004, state=1, wait_for_response = False)
    # time.sleep(2) 
    # toggle_drv8825("192.168.10.20", 30002, "192.168.10.50", 50004, state=1, wait_for_response = False)
    # toggle_extruder("192.168.10.20", 30002, "192.168.10.50", 50004, state=1, wait_for_response = False)
    # time.sleep(10)
    # toggle_extruder("192.168.10.20", 30002, "192.168.10.50", 50004, state=0, wait_for_response = False)
    # toggle_drv8825("192.168.10.20", 30002, "192.168.10.50", 50004, state=0, wait_for_response = False)
    # time.sleep(2)
    # toggle_air("192.168.10.20", 30002, "192.168.10.50", 50004, state=0, wait_for_response = False)
    # time.sleep(2)
    toggle_fan("192.168.10.20", 30002, "192.168.10.50", 50004, state=0, wait_for_response = False)

