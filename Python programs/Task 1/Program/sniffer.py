from scapy.all import sniff

# Callback function to process captured packets
def process_packet(packet):
    print(packet.summary())

# Start sniffing
print("Starting network sniffing...")
sniff(prn=process_packet, count=10)  # Adjust count or use timeout
