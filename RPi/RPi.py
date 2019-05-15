#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket, json, sqlite3, sys
sys.path.append("..")
import socket_utils

with open("config.json", "r") as file:
    data = json.load(file)
    
HOST = data["masterpi_ip"] # The server's hostname or IP address.
PORT = 63001               # The port used by the server.
ADDRESS = (HOST, PORT)

def login(user):
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