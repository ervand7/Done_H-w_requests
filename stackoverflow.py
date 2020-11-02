import requests
from pprint import pprint

response = requests.get(
    "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=python&site=stackoverflow"
)
data = response.json()
items = data['items']

for i in items:
    for s in i['tags']:
        if not 'ython' in s:
            continue
        pprint(s)
    pprint(i['creation_date'])
    print()
