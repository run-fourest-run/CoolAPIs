import requests
import yaml
import re

def build_payload_getSearchResults(**parameters):
    new_parameters = {k:v.replace("'","") for (k,v) in parameters.items()}
    payload = ''.join('{!s}={!s}'.format(key, val) for (key, val) in new_parameters.items())
    return payload





if __name__ == '__main__':
    cfg = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
    _zwsid = cfg['zwsid']
    urls = cfg['url']
    url = urls[0]
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "d5e95517a2msh75c98018c625d82p12ab5ejsndd559dc778fd",
    'x-rapidapi-host': "ZillowdimashirokovV1.p.rapidapi.com"
    }
    zip = 'tempe arizona'
    address = '818 E Drake Dr'

    payload = build_payload_getSearchResults(zwsid=_zwsid, citystatezip=zip, address=address, rentzestimate='false')
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)







