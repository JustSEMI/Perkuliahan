def decode_ip_to_ascii(data_string):
    lines = data_string.strip().split('\n')
    decoded_flag = ""
    
    for line in lines:
        ip_part = line.split(' ')[0] 

        octets = ip_part.split('.')
        
        if len(octets) >= 2:
            try:
                octet1 = int(octets[0])
                octet2 = int(octets[1])
                
                char1 = chr(octet1)
                char2 = chr(octet2)
                
                decoded_flag += char1 + char2
                
            except ValueError:
                continue
            except UnicodeEncodeError:
                continue

    return decoded_flag

ip_data = """
192.100.100.1
"""

final_decode = decode_ip_to_ascii(ip_data)

print("=========================================")
print(f"{final_decode}")
print("=========================================")