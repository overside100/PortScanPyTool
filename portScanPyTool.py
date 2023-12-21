import sys
import socket
import threading

print("PORT SCANNER PYTHON TOOL")

target = input("Target IP: ")

def scan_port(target, port):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = scanner.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        scanner.close()

    except KeyboardInterrupt:
        print("\nExit :(")
        sys.exit()

    except socket.error:
        print("\nHost has no response")
        sys.exit()

try:
    for port in range(1, 65535):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

except KeyboardInterrupt:
    print("\nExit :(")
    sys.exit()

