import requests
import json

#################################################################
#       CRM Access Details                                      #
#################################################################

site = 'https://comtactltd.crm4.dynamics.com/'
siteid = '00000000-0000-0000-0000-000000000000'
username = 'user@comtact.co.uk'
userpassword = 'P@ssw0rd'
tokenendpoint = 'https://login.microsoftonline.com/' + siteid + '/oauth2/token'
apiversion = 'v9.1'

crmwebapi = site + '/api/data/' + apiversion
crmwebapiquery = '/contacts?$select=fullname,contactid'

#build the authorization token request
tokenpost = {
        'client_id':clientid,
        'resource':crmorg,
        'username':username,
        'password':userpassword,
        'grant_type':'password'
}





