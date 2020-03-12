import json
import requests

#### CDC Base Config ####

username = "test@comtact2.com"
apikey = "7ce692f2e471835b0376dda218819053379ea171"

api_token = username + ":" + apikey
api_url_base = 'https://comtact.azurewebsites.net/api/v1/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'ApiKey {0}'.format(api_token)}

def getdevices(table):
    api_url = ('{0}'+ table +'').format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def get_data(table):
    account_info = getdevices(table)

    if account_info is not None:
        print(account_info)
    else:
        print('[!] Request Failed')

def get_clientnetworks():
    
    api_url = '{0}networks/'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] Request Failed')

def get_clientnetworksdata():
    account_info = get_clientnetworks()

    if account_info is not None:
        print(account_info)
    else:
        print('[!] Request Failed')

def add_device(host, hostname, data, mac, lastboot, os, tcp_ports, udp_port, type):

    # Adds device to database
    api_url = '{0}devices/'.format(api_url_base)
    device = {'ip_address': host, 'fqdn': hostname, 'external_asset': "False", 'scan_data': data, 'mac': mac, 'last_boot': lastboot, 'operating_system': os, 'device_type': type}
    
    response = requests.post(api_url, headers=headers, json=device)
    
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(response.content )
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 201:
        print('Device Added')
        return None
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

def update_device(id, host, hostname, data, mac, lastboot, os, tcp_ports, udp_port, type):

    # updates device in database
    api_url = '{0}devices/{1}/'.format(api_url_base, id)
    device = {'ip_address': host, 'fqdn': hostname, 'external_asset': "False", 'scan_data': data, 'mac': mac, 'last_boot': lastboot, 'operating_system': os, 'device_type': type}
    
    response = requests.put(api_url, headers=headers, json=device)
    
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(response.content )
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 201:
        print('Device Added')
        return None
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

def lookupdevice(ipaddr):
    api_url = '{0}devices/{1}{2}'.format(api_url_base, '?ip_address=', ipaddr)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        for id in data['objects']:
            return (id['id'])
    else:
        print('[!] Request Failed')

def lookupport(type, port):
    api_url = '{0}ports/{1}{2}{3}{4}'.format(api_url_base, '?type=', type, '&number=', port)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        for id in data['objects']:
            return (id['id'])
    else:
        print('[!] Request Failed')

def add_port(type, port):

    # Adds device to database
    api_url = '{0}ports/'.format(api_url_base)
    port = {'type': type, 'number': port}
    
    response = requests.post(api_url, headers=headers, json=port)
    
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(response.content )
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 201:
        print('Device Added')
        return None
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None


