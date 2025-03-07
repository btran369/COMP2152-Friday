import platform
import socket
import os
import sys

print(f"\nMachine Type: {platform.machine()}")
print(f"\nProcessor Type: {platform.architecture()}")

socket.setdefaulttimeout(50)
print(f"\nDefault Socket Timeout: {socket.getdefaulttimeout()}")

print(f"\nOperating System Type: {os.name}")
print(f"\nOperating System Name: {platform.system()}")
print(f"\nCurrent PID: {os.getpid()}")

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
file_obj_textIO = os.fdopen(file_handle, "w+")

file_obj_textIO.write("This is a test string, this does nothing...")
file_obj_textIO.flush()

#UNIX ONLY
#pid = os.fork()

pid = 1
if pid == 0:
    print(f"\nChild PID: {os.getpid()}, Parent PID: {os.getppid}")
    os.lseek(file_handle, 0, 0)
    print(f"\nChild PID: {os.getpid()}; File Content: {os.read(file_handle, 100)}")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\nParent PID: {os.getpid}, Child PID: {os.pid}")
    print("Wait for child...")
    os.wait()
    print("Child finished.")
    file_obj_textIO.close()
sys.exit(0)
