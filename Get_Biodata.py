from email import header
from turtle import pd
from xml.dom import NoModificationAllowedErr
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import urllib3


http = urllib3.PoolManager()
base_url_pindahan = 'https://forlap.kemdikbud.go.id/mahasiswa/detail/RTAyMTE1RDctNjlFMS00NDRGLUJBQTUtQTBCMkQ5REU1OTJB/0'
base_url_aktif = 'https://forlap.kemdikbud.go.id/mahasiswa/detail/MDJBRUUyRDktRDhCOS00QUI2LUEyMDgtRDlBMEIzMDExMEJG/0'
base_url_lulus = 'https://forlap.kemdikbud.go.id/mahasiswa/detail/RkI3RjA1RUYtQkY4MS00RDlFLTg2RjktQTlGOTA3OERBRkU4/0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

df = pd.read_csv('Data/Genap 2016/Url_Profile_Genap_2016.csv')
link = df['url_profile']
datas=[]
for i in link:
    req = requests.get(i, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    biodata = soup.findAll('tr', class_=False, id=False, colspan=False)
    for index1, it in enumerate(biodata):
        if index1 == 11:
            break
        cols = it.find_all('td')
        for index, t in enumerate(cols):
            a = t.text.strip()
            # if index == 7:
            if a == '':
                break
            if a == '-':
                break
            # if a == 'Lulus':
            #     break
            if index == 2:
                datas.append(a)
                # print(a)
        

kepala = ['data']
writer = csv.writer(open('Data/Genap 2016/Base_Genap_2016.csv', 'w', newline=''))
writer.writerow(kepala)
for d in datas: writer.writerow(d)
# kepala = ['nim']
# writer = csv.writer(open('biodata_scraping.csv', 'w', newline=''))
# writer.writerow(kepala)
# for d in datas: writer.writerow(d)
