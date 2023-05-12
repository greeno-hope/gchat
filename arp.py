import subprocess
import re
import time

import global_data as gd


def find_arp_hosts():

    while True:
        # run the arp -a command and capture its output
        arp_output = subprocess.check_output(['arp', '-a'])

        # decode the output into a string
        arp_output_str = arp_output.decode()

        ip_addresses = []
        ip_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        for line in arp_output_str.splitlines():
            ip_address = ip_regex.search(line).group(0)
            if ip_address is not None:
                ip_addresses.append(ip_address)
                # Testing
                print(ip_address)

        # Update the global arp hosts list
        with gd.subnet_hosts_lock:
            gd.subnet_hosts = ip_addresses

        time.sleep(120)
        break


