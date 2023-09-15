from scapy.all import *

target_ip = ""

port_range = (1, 1024)





open_ports = []

for port in range(port_range[0], port_range[1] + 1):

    syn_packet = IP(dst=target_ip)/TCP(dport=port, flags="S")

    response = sr1(syn_packet, timeout=1, verbose=0)

    if response and TCP in response and response[TCP].flags == "SA":

        open_ports.append(port)



#Print the results



if len(open_ports) == 0:

    print("No open ports found.")

else:

    print(f"Open ports: {', '.join(str(port) for port in open_ports)}")

