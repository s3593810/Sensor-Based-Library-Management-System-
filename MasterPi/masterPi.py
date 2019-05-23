#!/usr/bin/env python3
# Documentation: https://docs.python.org/3/library/socket.html
# from MasterMenu import Menu
from MasterMenu import Menu
import socket
import json
import sys
import struct
sys.path.append("..")


class MasterPi:
    """
    This class shows the connection through socket programming between
    master pi and reception pi.

    
    Attributes
    ----------

    HOST
        IP address of the Host device.
    PORT
        Port to listen on (non-privileged ports are > 1023).
    ADDRESS
        Address is the combination of the host ip and port number.
        
    Methods
    -------

    Main()
        Lets master py act as a listener for the reception pi.
        Maintains connectivity between master pi and reception pi using
        particular sockets.

    """
    # Empty string means to listen on all IP's on the machine, also works with IPv6.
    HOST = ""
    # Note "0.0.0.0" also works but only with IPv4.
    PORT = 65000  # Port to listen on (non-privileged ports are > 1023).
    ADDRESS = (HOST, PORT)

    def main(self):
        menu = Menu()
        socket_utils = Socket_utils()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(self.ADDRESS)
            s.listen()

            print("Listening on {}...".format(self.ADDRESS))
            while True:
                print("Waiting for Reception Pi...")
                conn, addr = s.accept()
                with conn:
                    print("Connected to {}".format(addr))
                    print()

                    user = socket_utils.recvJson(conn)
                    menu.runMenu(user)

                    socket_utils.sendJson(conn, {"logout": True})


class Socket_utils:
    """
    This class shows the connection through socket programming between
    master pi and reception pi.

    Methods
    -------

    sendJson()
        Lets master py and reception py act through particular
        socket and pass object between then using json.

    recvJson()
        Receives objects through socket.

    """
    def sendJson(self,socket, object):
        jsonString = json.dumps(object)
        data = jsonString.encode("utf-8")
        jsonLength = struct.pack("!i", len(data))
        socket.sendall(jsonLength)
        socket.sendall(data)

    def recvJson(self,socket):
        buffer = socket.recv(4)
        jsonLength = struct.unpack("!i", buffer)[0]

        # Reference: https://stackoverflow.com/a/15964489/9798310
        buffer = bytearray(jsonLength)
        view = memoryview(buffer)
        while jsonLength:
            nbytes = socket.recv_into(view, jsonLength)
            view = view[nbytes:]
            jsonLength -= nbytes

        jsonString = buffer.decode("utf-8")
        return json.loads(jsonString)


# Execute program.
if __name__ == "__main__":
    MasterPi().main()
