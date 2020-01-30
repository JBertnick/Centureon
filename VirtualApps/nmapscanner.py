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

def add_data(host, hostname):
    id = nmapapi.lookupdevice(host)

    # Looks up exsiting devices in database and checks 

    if id == None :
        nmapapi.add_device(host, hostname)
        print('Device does not exist adding to database')
    else:
        nmapapi.update_device(id, host, hostname)
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

    for network in networks_json['objects']:
        nm.scan(network['cidr'], arguments='--disable-arp-ping')
        
        for host in nm.all_hosts():
            hostname = nm[host].hostname()
            print(hostname)
            print(nm[host])
            #add_data(host, hostname)
            #print('----------------------------------------------------')
            #print('Host : %s (%s)' % (host, nm[host].hostname()))
            #print('State : %s' % nm[host].state())
            #
            #for proto in nm[host].all_protocols():
            #    print('----------')
            #    print('Protocol : %s' % proto)
            #
            #    lport = nm[host][proto].keys()
            #    sorted(lport)
            #    for port in lport:
            #        print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
            #        if proto == 'tcp':
            #            add_port('1', port)
            #        if proto == 'udp':
            #            add_port('2', port)
            #        else:
            #            pass

    
# scan(loaddata.networks(1), '0-21')
# scan('192.168.1.1/24', '0-8000')
scanfull()
# scanbasic('1')
#add_data('192.168.0.1','test.com','1')
#loaddata()
