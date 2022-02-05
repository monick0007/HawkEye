# import jspcap
import nest_asyncio
import pyshark as ws
from scapy.all import rdpcap
import whois
import time
def wireshark_cap():
    nest_asyncio.apply()
    filter_string = "port 443"
    capture = ws.LiveCapture(output_file="packet_data.pcap",bpf_filter=filter_string,interface="Wi-Fi 2")
    capture.sniff(timeout=20)

    p=rdpcap("packet_data.pcap")
    field_value ={}

    for i in range(len(p)):
        
        field_value1 = getattr(p[i]['IP'],"dst")
        if "192.168" in field_value1:
            continue
        elif field_value1 in field_value.values():
            continue
        else:
            field_value.update({i+1:field_value1})

    for i in field_value.values():
        print(i)
        w=whois.whois(i)
        try:
            for i in w['name_servers']:
                if "GOOGLE" or "google" in i:
                    final="you opened google"

                    break
            break
        except:
            continue
    return final        
# data = "142.251.40.130"
# w = whois.whois(data)

# print(w)  
