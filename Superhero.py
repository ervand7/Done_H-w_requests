import requests

def d_m_i_h(*args): # requested_name_1, requested_name_2, requested_name_3
    '''The abbreviation stands for "defining the most intelligent hero"'''
    common_dct = {}
    lst = [*args] # list of the requested names of the heroes
    for i in lst:

        response = requests.get(f"https://superheroapi.com/api/182920483421596/search/{i}")
        data = response.json()
        results = data["results"]
        intelligence = (int(results[0]["powerstats"]['intelligence']))
        common_dct[i] = intelligence

    hsbi = sorted(common_dct.items(), key=lambda x: x[1], reverse=True) # The abbreviation stands for heroes sorted by intelligence in reverse order
    print(f'The most intelligent hero is {hsbi[0][0]}, his IQ = {hsbi[0][1]}.')

d_m_i_h('Thanos', 'Hulk', 'Captain_America')
