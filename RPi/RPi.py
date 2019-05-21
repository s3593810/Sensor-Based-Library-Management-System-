#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
import json
import sqlite3
import sys
import struct
sys.path.append("..")


class ReceptionPi:
    def login(self, user):
        socket_utils = Socket_utils()
        with open("config.json", "r") as file:
            data = json.load(file)
        HOST = data["masterpi_ip"]
        PORT = 63001
        ADDRESS = (HOST, PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to {}...".format(ADDRESS))
            s.connect(ADDRESS)
            print("Connected.")

            print("Logging in as {}".format(user["username"]))
            socket_utils.sendJson(s, user)

            print("Waiting for Master Pi...")
            while(True):
                object = socket_utils.recvJson(s)
                if("logout" in object):
                    print("Master Pi logged out.")
                    print()
                    break


class Socket_utils:

    def sendJson(socket, object):
        jsonString = json.dumps(object)
        data = jsonString.encode("utf-8")
        jsonLength = struct.pack("!i", len(data))
        socket.sendall(jsonLength)
        socket.sendall(data)

    def recvJson(socket):
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
