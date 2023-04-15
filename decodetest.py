import re

test_string = "CALLSIGN>APRS,TCPIP*:@123456z1234.56N/12345.67W_123/123g123t123r123p123P123h123b12300.0N/12300.0W:" + "kJ1sdfl C1 B2 C1 G4 H3_1"

def match_commnads(msg):
    # print("Original: " + msg)
    for i in range(len(msg)):
        sub_msg = msg[i:]
        # print(f"New {sub_msg}")
        if bool(re.match(r'^([A-Z]\d\s?)+(_1)?$', sub_msg, re.A)):
            return sub_msg

print(match_commnads(test_string))