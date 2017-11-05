import socket
import sys
import base64
import struct
import array
import  pickle
from struct import *
import random
import time


class UDP_client():
    """docstring fo UDP_client."""
    def __init__(self, port):
        self._port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._server_address = ('localhost', self._port)


    def send_packet(self, id, packet):
        id_packet = [id,0,0,0]
        buf = struct.pack('%sf' % len(packet), *packet)
        buf_id = struct.pack('%si' % len(id_packet), *id_packet)
        sent = self._sock.sendto(buf_id+buf, self._server_address)
        sys.stderr
        data, server = self._sock.recvfrom(self._port)
        return array.array('f',data )


udp = UDP_client(9876)

theta =  3.14
vel = 0
accel = 0

packet = 4*[200,vel,accel]
t0 = time.time()
udp.send_packet(37,packet)
t1 = time.time()
print (t1-t0)*1000


