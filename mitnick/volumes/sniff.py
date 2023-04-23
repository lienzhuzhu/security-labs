# This program sniffs packets on a TCP connection

from scapy.all import *

print("SNIFFING PACKETS........")

def process_packet(packet):
    if TCP in packet:
        print("Source IP:",         packet[IP].src)
        print("Destination IP:",    packet[IP].dst)
        print("Sequence Number:",   packet[TCP].seq)
        print("Flags:",             packet[TCP].flags)

        # Print out all the length fields in the packet
        print("IP Length:", packet[IP].len)
        print("TCP Length:", packet[TCP].dataofs)

        if Raw in packet:
            print("Payload Length:", len(packet[Raw].load))
        print("-" * 50)

# Use the sniff method with a callback function to capture packets
sniff(iface="br-e9669d80b341", filter="tcp", prn=process_packet)

