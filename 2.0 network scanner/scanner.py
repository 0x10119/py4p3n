import nmap
import sys
import socket

target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]

gethostby_ = socket.gethostbyname(target)
# print(gethostby_)
scan_v = nmap.PortScanner()
print("\nScanning ", target, "for ports 21, 22, 80, 139, 443, 8080...\n")

for port in ports:
    portscan = scan_v.scan(gethostby_, str(port))
    print("Port", port, " is ", portscan['scan'][gethostby_]['tcp'][port]['state'])

print("\nHost ", target, " is ", portscan['scan'][gethostby_]['status']['state'])
