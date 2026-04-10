import argparse
import scapy

def main(pcap_file, output_file):
    ...

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to netmapper - turn pcap files into visual network diagrams")
    
    parser.add_argument("pcap-file", help="The pcap file that sniffed ")
    parser.add_argument("-o", "--output")

    args = parser.parse_args()
    main()