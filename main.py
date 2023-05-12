import gnutella as g
import threading
import arp
import time
import global_data as gd
import network


def shut_down():
    pass


def start():
    # Start the arp thread
    at = threading.Thread(target=arp.find_arp_hosts())
    at.start()

    # Start the ping/heartbeat thread
    st = threading.Thread(target=network.gnutella_heartbeat())
    st.start()

    # Start the listening (server) thread
    lt = threading.Thread(target=network.gnutella_listen())
    lt.start()

    # Start the main loop
    while True:
        # Wait for keyboard input (a message to send)
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
