#_*_ coding: UTF-8 _*_
import requests
import json

# r = requests.get('https://api.github.com/events')
# r = requests.get('https://www.naver.com/')
headers = {
    'Authorization': 'Bearer tttttttttttt',
    'Content-Type': 'application/pdf'
}
url = 'https://recruit.brich.co.kr/api/resume'
# url = 'http://localhost:9897'
print("김현하")
#files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# files = {'file': open('D:\\khh\git\\book-hibernate\\hibernate5.x.pdf', 'rb')}
files = {'file': ('hibernate5.x.pdf', open('D:\\khh\git\\book-hibernate\\hibernate5.x.pdf', 'rb'), 'application/pdf', {'Expires': '0'})}
r = requests.post(url,headers=headers, files=files)
print(r.encoding)
print(r.headers['Content-Type'])
print(r.content.decode('UTF-8'))