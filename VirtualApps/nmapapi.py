import json
import requests

#### CDC Base Config ####

api_token = 'your_api_token'
api_url_base = 'http://127.0.0.1:8000/api/v1/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

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

def get_clientnetworks(client):
    
    api_url = '{0}client_networks/{1}{2}'.format(api_url_base, '?client=', client)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] Request Failed')

def get_clientnetworksdata(client):
    account_info = get_clientnetworks(client)

    if account_info is not None:
        print(account_info)
    else:
        print('[!] Request Failed')

def add_device(name, ipaddress, client):

    # Adds device to database
    api_url = '{0}device/'.format(api_url_base)
    device = {'dns_name': name, 'ip_address': ipaddress, 'client': ('/api/v1/client/' + client + "/")}
    
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

def update_device(device_id, name, ipaddress, client):

    # updates device in database
    api_url = '{0}device/'.format(api_url_base)
    device = {'id': device_id, 'dns_name': name, 'ip_address': ipaddress, 'client': ('/api/v1/client/' + client + "/")}
    
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

def lookupdevice(client, ipaddr):
    api_url = '{0}device/{1}{2}{3}{4}'.format(api_url_base, '?client=', client, '&ip_address=', ipaddr)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        for id in data['objects']:
            return (id['id'])
    else:
        print('[!] Request Failed')
