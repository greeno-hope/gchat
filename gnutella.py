import uuid

# The payload descriptor for a PING
PING = bytes([0x00])

# The payload descriptor for a PONG
PONG = bytes([0x01])

# The payload descriptor for a PUSH
# We'll use PUSH to broadcast a message
PUSH = bytes([0x40])

# TTL is only one because we will be operating inside a broadcast domain
TTL = bytes([1])

# Descriptor ID is a 16 byte field. We'll create a globally unique ID
# for each packet sent by using a MAC address as the 1st 6 bytes and then
# the remaining 10 bytes will be a counter
ID_HEADER = uuid.getnode().to_bytes(6, 'big')

# The counter bit of the DescriptorID
PACKET_NO = 0


HOPS = (0).to_bytes(1, 'big')


def encode_ping():
    """
    Encodes a gnutella PING as a BYTE array
    :return: A BYTE array that can be sent over a UDP socket
    """
    # Create a BYTE array
    global ID_HEADER
    global PACKET_NO
    global PING
    global TTL
    global HOPS

    packet = bytearray()
    # Append the DescriptorID (first 6 bytes)
    packet.extend(ID_HEADER)
    # Append the DescriptorID (next 10 bytes a counter)
    packet.extend(PACKET_NO.to_bytes(10, 'big'))
    # Increment the counter
    PACKET_NO += 1
    # Append the Payload Descriptor
    packet.extend(PING)
    # Append the TTL (time to live)
    packet.extend(TTL)
    # Append the hop count
    packet.extend(HOPS)
    # Append the 4 byte data length field (zero for a PING)
    packet.extend((0).to_bytes(4, 'big'))
    return packet


def encode_broadcast(message):
    pass


def decode_packet():
    pass

