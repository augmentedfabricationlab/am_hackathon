# -*- coding: UTF-8 -*-
import socket
import struct
import time
from message_types import msg_types_dict
from message_types import MSG_RECEIVED, MSG_EXECUTED, MSG_STOP, MSG_INFO, MSG_DODATA, MSG_MOTORDATA, MSG_MOTORSTATE

__all__ = [
    "ExtruderClient"
]

class ExtruderClient():
    def __init__(self, host = "192.168.10.50", port = 50004):
        self.host = host
        self.port = port
        self.connected = False

        self.msg_rcv = bytearray([])
        self.info_msg = ""
        self.header_byteorder = ">lll"

    def clear(self):
        self.msg_rcv = bytearray([])

    def connect(self):
        if not self.connected:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            print("Connected to server {} on port {}".format(self.host, self.port))
            self.connected = True
    
    def close(self):
        self.sock.close()
        self.connected = False

    # Send commands

    def send_stop(self, wait_for_response=True):
        return self.__send(MSG_STOP, wait_for_response=wait_for_response)

    def send_set_do(self, pin=0, state=0, wait_for_response=True):
        msg = [pin, state]
        return self.__send(MSG_DODATA, 8, msg, wait_for_response)

    def send_motordata(self, motor_id, state, max_speed, speed, acceleration, wait_for_response=True):
        msg = [motor_id, state, max_speed, speed, acceleration]
        return self.__send(MSG_MOTORDATA, 20, msg, wait_for_response)
    
    def send_motorstate(self, motor_id, state, wait_for_response=True):
        msg = [motor_id, state]
        return self.__send(MSG_MOTORSTATE, 8, msg, wait_for_response)

    def send_get_arduino_info(self, wait_for_response=True):
        return self.__send(MSG_INFO, wait_for_response=wait_for_response)

    # Get commands

    def get_msg_stop(self, wait_for_response=True):
        return self.__get_msg(MSG_STOP, wait_for_response=wait_for_response)

    def get_msg_set_do(self, pin=0, state=0, wait_for_response=True):
        msg = [pin, state]
        return self.__get_msg(MSG_DODATA, 8, msg, wait_for_response)

    def get_msg_motordata(self, motor_id, state, max_speed, speed, acceleration, wait_for_response=True):
        msg = [motor_id, state, max_speed, speed, acceleration]
        return self.__get_msg(MSG_MOTORDATA, 20, msg, wait_for_response)
    
    def get_msg_motorstate(self, motor_id, state, wait_for_response=True):
        msg = [motor_id, state]
        return self.__get_msg(MSG_MOTORSTATE, 8, msg, wait_for_response)

    def get_msg_arduino_info(self, wait_for_response=True):
        return self.__get_msg(MSG_INFO, wait_for_response=wait_for_response)

    # Internal commands

    def __get_msg(self, msg_type, msg_len = 0, msg = None, wait_for_response = True, packed=False):
        msg_list = [msg_type, msg_len, int(wait_for_response)]
        if msg is not None:
            msg_list.extend(msg)
        if packed:
            packed_msg = struct.pack(self.header_byteorder + msg_types_dict[msg_type][1], *msg_list)
            return packed_msg
        else:
            return msg_list

    def __send(self, msg_type, msg_len = 0, msg = None, wait_for_response = True):
        self.sock.send(self.__get_msg(msg_type, msg_len, msg, wait_for_response, True))
        headers, msgs = [], []
        while wait_for_response:
            header, msg = self.__read()
            if header is not None:
                print("{} received from Arduino.".format(msg_types_dict[header[0]][0]))
                print("Message: {}".format(msg))
                headers.append(header)
                msgs.append(msg)
                wait_for_response = header[0] != MSG_EXECUTED
                print("Still waiting? -> ", wait_for_response)
            time.sleep(0.1)
        else:
            return(headers, msgs)
            
    def __read(self):
        try: 
            self.msg_rcv.extend(self.sock.recv(1))
            print(self.msg_rcv)
            hdr = struct.unpack_from(self.header_byteorder, self.msg_rcv)
            print(hdr)
        except:
            return None, None
        else:
            if hdr[1] > 0: 
                msg = struct.unpack_from(msg_types_dict[hdr[0]][2], self.sock.recv(hdr[1]))
            else:
                msg = ""
            print(msg)
            self.clear()
            return hdr, msg

if __name__ == "__main__":
    ec = ExtruderClient()
    ec.connect()
    time.sleep(0.5)
    print("Connection: ", ec.connected)
    #ec.send_get_arduino_info()
    pin = 32
    state = 1
    wait = False
    for i in range(5):
        ec.send_set_do(pin-2,1,wait)
        ec.send_set_do(pin,1,wait)
        ec.send_set_do(pin+2,1,wait)
        ec.send_set_do(pin-2,0,wait)
        ec.send_set_do(pin,0,wait)
        ec.send_set_do(pin+2,0,wait)
        time.sleep(1)
    # ec.send_set_do(30,1,wait)
    # time.sleep(0.5)
    # ec.send_motordata(0, 0, 1600, 800, 200, wait)
    # ec.send_motorstate(0, 1, wait)
    #executed = False
    # while not executed:
    #     raw_hdr = bytearray([])
    #     [raw_hdr.extend(ec.sock.recv(1)) for i in range(12)]
    #     #print(raw_hdr)
    #     hdr = struct.unpack(ec.header_byteorder, raw_hdr)
    #     #print(hdr)
    #     if hdr[0] == MSG_EXECUTED:
    #         executed = True
    #     elif hdr[0] == MSG_INFO:
    #         raw_msg = bytearray()
    #         raw_msg.extend(ec.sock.recv(hdr[1]))
    #         #[raw_msg.extend(ec.sock.recv(1)) for i in range(hdr[1])]
    #         msg = struct.unpack(msg_types_dict[MSG_INFO][2], raw_msg)
    #         for m in msg[:3]:
    #             clean_msg = m[:m.index(0)] 
    #             #print(clean_msg.decode())
    #     else:
    #         pass
    #     time.sleep(0.1)

    # time.sleep(5)
    # ec.send_motorstate(0, 0, wait)
    # time.sleep(0.5)
    # ec.send_set_do(30,0,wait)
    ec.close()
    print("Connection: ", ec.connected)
