from email import header
from turtle import pd
from xml.dom import NoModificationAllowedErr
import requests
from bs4 import BeautifulSoup
import csv
import urllib3

http = urllib3.PoolManager()
base_url = 'https://forlap.kemdikbud.go.id/mahasiswa/detailsemester/MTQyMjlCRDItMkIzNy00NDdGLUEzRUEtNTMyQzJBNUUzN0Yw/20171/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
datas=[]
for page in range(0, 1000, 20):
    req = requests.get(base_url+str(page), headers=headers)
    # print(req)
    soup = BeautifulSoup(req.text, 'html.parser')
    item_mahasiswa = soup.findAll('tr', 'tmiddle')
    for it in item_mahasiswa:
        nim = it.find({'td'}, class_=False, id=False).text
        # nama = it.find({'a'}).text
        url_profile = it.find({'a'})['href']
        datas.append([nim, url_profile])
        # print(url_profile)
        # print(nim)
    # print('INI PAGE BARU')

kepala = ['nim', 'url_profile']
writer = csv.writer(open('Data/Ganjil 2017/Url_Profile_Ganjil_2017.csv', 'w', newline=''))
writer.writerow(kepala)
for d in datas: writer.writerow(d)

###################################################
# url10 = 'https://forlap.kemdikbud.go.id/perguruantinggi/detail/NDJGMjA3MjEtMDNCNy00QTMzLUFEMjYtOTY4QUFENjZFMjUz'
# url10 = 'https://forlap.kemdikbud.go.id/prodi/detail/MTQyMjlCRDItMkIzNy00NDdGLUEzRUEtNTMyQzJBNUUzN0Yw/0'
# pilih = ['Mahasiswa']
# tahun_ajaran = ['Ganjil 2011', 'Genap 2011', 'Ganjil 2012', 'Genap 2012', 'Ganjil 2013', 'Genap 2013', 
#                 'Ganjil 2014', 'Genap 2014', 'Ganjil 2015', 'Genap 2015', 'Ganjil 2016', 'Genap 2016', 
#                 'Ganjil 2017', 'Genap 2017', 'Ganjil 2018', 'Genap 2018', 'Genap 2019', 'Ganjil 2019']
# req = http.request('GET', base_url)
####################################
# for link in url_profile:
#     req2 = requests.get(link)
#     print(req2)
#     soup2 = BeautifulSoup(req2.text, 'html.parser')
#     item_profile = soup.findAll('table', 'table1')
#     for dapat in item_profile:
#         Tahun_masuk = dapat.find({'td'}).text
#         print(Tahun_masuk)

# link_baru = 'https://forlap.kemdikbud.go.id/mahasiswa/detail/RkI3RjA1RUYtQkY4MS00RDlFLTg2RjktQTlGOTA3OERBRkU4/0'
# req2 = requests.get(link_baru)
# print(req2)

# Looping Hampir Bener
# for hitung in range(1, 3):
#     for link_baru in url_profile:
#         hitung = requests.get(link_baru)
#         print(hitung)
    

# COBA
# soup2 = BeautifulSoup(req2.text, 'html.parser')
# item_profile = soup.findAll('table', 'table1')
# for dapat in item_profile:
#     Tahun_masuk = dapat.find({'td'}).text
#     print(Tahun_masuk)        