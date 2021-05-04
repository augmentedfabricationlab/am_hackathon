import sys, time
sys.path.append("C:/Users/Gido/Documents/workspace/development/mobile_additive_manufacturing/src/mobile_additive_manufacturing/control")
from clay_extruder_control import ExtruderClient

# globals
enable_pin = 34
max_speed = 51200
run_speed = 10
acceleration = 0.1

# extruderclient connect
ec = ExtruderClient()
ec.connect()
time.sleep(0.5)
print("Connection: ", ec.connected)

# set the motordata
ec.send_motordata(0, 0, max_speed, run_speed, acceleration, False)

# enable the motor
ec.send_set_do(enable_pin, 0, False)

time.sleep(0.5)
ec.close()
print("Connection: ", ec.connected)