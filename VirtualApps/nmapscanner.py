import nmap
import nmapapi
import json
import objectpath

# Python Nmap Scanner for Netscan

# API downloads the list of networks to scan

# Snip below to help understand JSON loading data
# network = networks_json['objects'][]['network'] - prints the networks 

def loaddata(client):

    networks = [] # Sets networks to empty
    client = client # Defines client ID in database
    networks_json = nmapapi.get_clientnetworks(client)

    # Loads the networks for scaning from the JSON data stored from the API.

    for network in networks_json['objects']:
        networks.append(network['network'])
    print (networks)

def add_data(host, hostname, client):
    id = nmapapi.lookupdevice(client, host)

    # Looks up exsiting devices in database and checks 

    if id == None :
        nmapapi.add_device(hostname, host, client)
        print('Device does not exist adding to database')
    else:
        nmapapi.update_device(id, hostname, host, client)
        print('Device exists updated data in database')

    # nmapapi.add_device(hostname, host, client)


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

def scanfull(client):
    networks_json = nmapapi.get_clientnetworks(client)
    nm = nmap.PortScanner()
    
    # Loads the networks for scaning from the JSON data stored from the API.
    # Loops though networks and scans for hosts up.

    for network in networks_json['objects']:
        nm.scan(network['network'], arguments='--disable-arp-ping')
        
        for host in nm.all_hosts():
            hostname = nm[host].hostname()
            # add_data(host, hostname, client)
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            
            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)

                lport = nm[host][proto].keys()
                sorted(lport)
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    
# scan(loaddata.networks(1), '0-21')
# scan('192.168.1.1/24', '0-8000')
# scanfull('1')
scanbasic('1')
#add_data('192.168.0.1','test.com','1')