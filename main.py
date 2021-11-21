import requests

credentials = '---', '---'
session = requests.Session()
session.auth = credentials
zendesk = 'https://zccmichaelreeves.zendesk.com'

url = f'{zendesk}/api/v2/tickets/2.json'
response = session.get(url, params={'url': 'https://zccmichaelreeves.zendesk.com/api/v2/tickets/2.json'})
if response.status_code != 200:
    print(f'Error with status code {response.status_code}')
    print(response.reason)
    exit()
data = response.json()

print(data)
