import requests
# THIS IS THE FIRST SOLUTION. HERE AT LEAST FOR MAC USERS AS SPECIFIED IN ARGUMENT
# FUNCTIONS OF THE ABSOLUTE WAY LOSES THE NECESSITY OF ADDITIONALLY ENTER THE NAME OF THE FILE WHICH
# USERS WANT TO SEE THE TOTAL ON YANDEX DISK, AS WITH THE HELP OF THE SITE
# CODE ON ROWS 15-24 THIS RECORD IS AUTOMATICALLY.

# Put here your token, from https://yandex.ru/dev/disk/poligon/
TOKEN = ''

class YaUploader:
    def __init__(self, frpnf, token=TOKEN): # frpnf is file relative path NOT formatted in url style
        self.token = token
        self.frpnf = frpnf

        counter = []
        for i in reversed(self.frpnf):
            if i == '/': # for MAC OS, linux, if the path is absolute
                break
            elif i == "\\": # for Windows (may be... if this does not fit then see the second solution)
                break
            counter.append(i)
        a_1 = list(reversed(''.join(counter)))
        a_2 = ''.join(a_1)
        self.fn = a_2 # fn is a file name, which you want see in Yandex.Disk'''

        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": self.fn},
            headers={"Authorization": f"OAuth {TOKEN}"}
        )
        url = response.json()['href'] # the link for future uploading
        print(f'URL-address successfully received. Code status is {response.status_code}.')

        files = {'file': open(self.frpnf, 'rb')}
        r = requests.post(url, files=files) # the start of writing data on Yandex.Disk
        r.text
        print(f'The file is successfully uploaded on Yandex.Disk.')
a = YaUploader('/Users/USER/Desktop/Безносиков.gif')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # THIS IS THE SECOND OPTION OF THE SOLUTION. YOU NEED THE DESIRED FILE NAME FOR YANDEX.DISK ENTER MANUALLY

# import requests
# from pprint import pprint
# # Put here your token, from https://yandex.ru/dev/disk/poligon/
# TOKEN = ''
#
# class YaUploader:
#     def __init__(self, fn, frpnf, token=TOKEN):
#         '''● fn is file name, wich you want see in Yandex.Disk
#            ● frpnf is file relative path NOT formatted in url style'''
#         self.token = token
#         self.fn = fn
#         self.frpnf = frpnf
#         response = requests.get(
#             "https://cloud-api.yandex.net/v1/disk/resources/upload",
#             params={"path": self.fn},
#             headers={"Authorization": f"OAuth {TOKEN}"}
#         )
#         print(response.status_code)
#         url = response.json()['href'] # the link for future uploading
#         pprint(url)
#
#         files = {'file': open(self.frpnf, 'rb')}
#         r = requests.post(url, files=files)
#         r.text
# a = YaUploader('Пример имени.gif', '/Users/USER/Desktop/Спиридонов.gif')

