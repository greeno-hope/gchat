import threading


subnet_hosts = []
subnet_hosts_lock = threading.Lock()

gnutella_hosts = []
gnutella_hosts_lock = threading.Lock()
