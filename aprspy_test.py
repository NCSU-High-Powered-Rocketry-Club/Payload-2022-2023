from aprspy import APRS
packet = APRS.parse('XX1XX>APRS,TCPIP*,qAC,FOURTH:=5030.50N/10020.30W$221/000/A=005Test packet')
print(f'Packet: {packet}')
print(f'Latitude {packet.latitude}')
print(f'Longitude: {packet.longitude}')
print(f'Course: {packet.course}')

print(type(packet))
