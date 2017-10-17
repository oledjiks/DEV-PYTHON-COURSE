import socket, struct

def ip2int(addr):
	return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


def strToSock(*args):
    try:
        addr, port = ''.join(args).split(':')
        return ip2int(addr), int(port)
    except Exception as e:
        print(e)

addr, port = strToSock('192.168.77.2:80')

print(addr, port)
print(int2ip(addr))