#!/usr/bin/python

import sys
import requests  
from requests.auth import HTTPBasicAuth  
import json  
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pprint
import argparse
import logging


parser = argparse.ArgumentParser(description='Get the status of the nodes in a named simulation.')
parser.add_argument('--host', required='True', dest='virl_host', action='store', help='IP address or FQDN the VIRL host.')
parser.add_argument('-u', '--user', required='True', dest='virl_user', action='store', help='VIRL user name.')
parser.add_argument('-p', '--password', required='True', dest='virl_pwd', action='store', help='VIRL password.')
parser.add_argument('-s', '--simulation', required='True', dest='sim_name', action='store', help='Simulation name.')
args = parser.parse_args()
parser.format_help()

try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

http_client.HTTPConnection.debuglevel = 1

# Initialize the logging function data structures

logging.basicConfig() 
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def main():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    r = get_node_status(args.virl_host, args.virl_user, args.virl_pwd, args.sim_name)
    p = r.json()
    pprint.pprint(p) 

    exit(0)

def get_node_status(virl_host, virl_user, virl_pwd, sim_name):
    url       = "http://%s:19399/simengine/rest/nodes/%s" % (virl_host, sim_name)
    headers   = {'content-type': 'text/xml'}
    r = requests.get(url, auth=(virl_user, virl_pwd), headers=headers) 
    return r

main()
