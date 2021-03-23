import requests

'''
Source:  https://dbader.org/blog/pythonic-loops

'''

url = "https://mashvisor-api.p.rapidapi.com/rental-rates"
headers = {
    'x-rapidapi-key': "d5e95517a2msh75c98018c625d82p12ab5ejsndd559dc778fd",
    'x-rapidapi-host': "mashvisor-api.p.rapidapi.com"
    }
def query_string_Builder(**kwargs):
    '''Builds Query String'''
    query_string = dict()
    query_string.update(kwargs)
    return query_string

def fetch(req_type,url, headers, params):
    response = requests.request(req_type, url=url ,headers= headers,params=params )
    return response.text





query_string = query_string_Builder(state='RI',zipcode ='02282',city='Narragansett',source=None)

print(fetch('GET',url,headers,query_string))
