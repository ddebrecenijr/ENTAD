#!/usr/bin/env python3

from Source.Facade.ArgParseHelper import ArgParseHelper
from Source.ProcessPacket import ProcessPacket
from Source.DomainInfoExtractor import Extractor
from Source.SVMModel import SVMModel
import json
import os

import socket
from Source.Sniffer.ethernet import Ethernet
from Source.Sniffer.ipv4 import IPv4

__author__ = "David Debreceni Jr"


def main():
    arg_parser = ArgParseHelper()
    kwargs = arg_parser.parse_args()
    #if kwargs['update']:
    #    # Handling Benign Domains
    #    domain_extractor = Extractor()
    #    benign_domains = domain_extractor.domain_reader('Source/benign_domains.txt')
    #    json_output = domain_extractor.multiprocess_extraction(
    #        benign_domains[:kwargs['num_domains']], kwargs['threads']
    #    )
    #    with open('JSON/benign_domain_dump.json', 'w') as file:
    #        file.write(json_output)

    #    # Handling Malicious Domains
    #    malicious_domains = domain_extractor.domain_reader('Source/malicious_domains.txt')
    #    json_output = domain_extractor.multiprocess_extraction(
    #        malicious_domains[:kwargs['num_domains']], kwargs['threads']
    #    )
    #    with open('JSON/malicious_domain_dump.json', 'w') as file:
    #        file.write(json_output)

#    svm = SVMModel()
#    svm.train_model()
    #print(svm.model_accuracy())
    #svm.show()

    #if 'malicious' in kwargs['file']:
    #    with open('JSON/malicious_test.json', 'r') as file:
    #        json_output = file.read()
    #else:
    #    process_packet = ProcessPacket(kwargs['file'], kwargs['ports'])
    #    json_output = json.dumps(process_packet.get_server_hello_data())

    #svm.test_model(json_output)

    #svm.show()

    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x003))
    try:
        while True:
            raw_buffer = sniffer.recvfrom(65565)[0]

            ethernet = Ethernet(raw_buffer[0:14])
            print('--- ETHERNET FRAME ---')
            print(f'Destination Address: {ethernet.Destination_Address}')
            print(f'Source Address: {ethernet.Source_Address}')
            print(f'Type: {ethernet.Type}')

            if ethernet.type == 8:
                ip = IPv4(raw_buffer[14:34])
                print('--- IPv4 FRAME ---')
                print(f'Version: {ip.Version}')
                print(f'IP Header Length: {ip.IP_Header_Length}')
                print(f'Type of Service: {ip.Type_of_Service}')
                print(f'Total Length: {ip.Total_Length}')
                print(f'Identification: {ip.Identification}')
                print(f'Time to Live: {ip.Time_to_Live}')
                print(f'Protocol: {ip.Protocol}')
                print(f'Header Checksum: {ip.Header_Checksum}')
                print(f'Source Address: {ip.Source_Address}')
                print(f'Destination Address: {ip.Destination_Address}')
            

    except KeyboardInterrupt:
        os.exit()
if __name__ == "__main__":
    main()
