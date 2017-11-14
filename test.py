import UDP
udp = UDP.UDP(9876)



packet = 15*[3.14,1,1]

print udp.send_packet(37,packet)


