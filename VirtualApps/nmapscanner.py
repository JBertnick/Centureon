import nmap
import nmapapi
import json
import objectpath

# Python Nmap Scanner for Netscan

# API downloads the list of networks to scan

# Snip below to help understand JSON loading data
# network = networks_json['objects'][]['network'] - prints the networks 

def loaddata():

    networks = [] # Sets networks to empty
    networks_json = nmapapi.get_clientnetworks()

    # Loads the networks for scaning from the JSON data stored from the API.

    for network in networks_json['objects']:
        networks.append(network['cidr'])
    print (networks)

def add_data(host, hostname, data, mac, lastboot, os, tcp_ports, udp_port, type):
    id = nmapapi.lookupdevice(host)

    # Looks up exsiting devices in database and checks 

    if id == None :
        nmapapi.add_device(host, hostname, data, mac, lastboot, os, tcp_ports, udp_port, type)
        print('Device does not exist adding to database')
    else:
        nmapapi.update_device(id, host, hostname, data, mac, lastboot, os, tcp_ports, udp_port, type)
        print('Device exists updated data in database')

    # nmapapi.add_device(hostname, host, client)

def add_port(type, port):
    id = nmapapi.lookupport(type, port)

    # Looks up exsiting devices in database and checks 

    if id == None :
        nmapapi.add_port(type, port)
        print('Port does not exist adding to database')
    else:
        pass

def scan(network, port_range):
    nm = nmap.PortScanner()
    nm.scan(network)

    for host in nm.all_hosts():
        hostname = nm[host].hostname()
        add_data(host, hostname)
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())

def scanbasic(client):
    networks_json = nmapapi.get_clientnetworks(client)
    nm = nmap.PortScanner()

    # Loads the networks for scaning from the JSON data stored from the API.
    # Loops though networks and scans for hosts up.

    for network in networks_json['objects']:
        nm.scan(network['network'], arguments='--disable-arp-ping -n -sP -PA21,23,80,443,3389')
        
        for host in nm.all_hosts():
            hostname = nm[host].hostname()
            add_data(host, hostname, client)
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())

def scanfull():
    networks_json = nmapapi.get_clientnetworks()
    nm = nmap.PortScanner()
    
    # Loads the networks for scaning from the JSON data stored from the API.
    # Loops though networks and scans for hosts up.
    # Checks with API for existance and adds or updates.

    for network in networks_json['objects']:
        nm.scan(network['cidr'], arguments='-O --disable-arp-ping')
        
        for host in nm.all_hosts():
            hostname = nm[host].hostname()
            data = nm[host]
            try:
                mac = nm[host]['addresses']['mac']
            except KeyError:
                mac = 'none'
            try: 
                lastboot = nm[host]['uptime']['lastboot']
            except KeyError:
                lastboot = 'Null'
            try:
                os = nm[host]['osmatch'][0]['name']
            except KeyError:
                os = 'none'
            except IndexError:
                os = 'none'
            tcp_ports = nm[host].all_tcp()
            udp_port = nm[host].all_udp()
            try:
                type = nm[host]['osmatch'][0]['osclass'][0]['type']
            except KeyError:
                type = 'none'
            except IndexError:
                type = 'none'
            
            add_data(host, hostname, data, mac, lastboot, os, tcp_ports, udp_port, type)

    
# scan(loaddata.networks(1), '0-21')
# scan('192.168.1.1/24', '0-8000')
#scanfull()
# scanbasic('1')
#add_data('192.168.0.1','test.com','1')
loaddata()
