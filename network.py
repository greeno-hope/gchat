import time
import socket

import global_data as gd
import gnutella as g

UDP_PORT = 666


def gnutella_heartbeat():
    """
    Thread function
    Sends a gnutella ping to every host in the
    subnet hosts table every 5s
    :return:
    """
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with gd.subnet_hosts_lock:
            for host in gd.subnet_hosts:
                p = g.encode_ping()
                dest = (host, 666)
                sock.sendto(p, dest)
        sock.close()
        time.sleep(10)


def gnutella_listen():
    """
    Thread function
    Listens for incoming gnutella traffic
    :return:
    """

    pass

