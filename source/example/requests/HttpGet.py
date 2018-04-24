#_*_ coding: UTF-8 _*_
import requests
import json
import time

# r = requests.get('https://api.github.com/events')
# r = requests.get('https://www.naver.com/')
#curl -H "Referer: http://map.daum.net/"   "http://map.search.daum.net/mapsearch/map.daum?callback=jQuery18107186947884846974_1524545004058&q=심리상담&msFlag=S&page=3&sort=0"
headers = {
    'Referer': 'http://map.daum.net/',
    'Content-Type': 'application/pdf'
}

page = 1
keyword = "심리상담"
place_totalcount = 10
url = 'http://map.search.daum.net/mapsearch/map.daum?callback=jQuery18107186947884846974_1524545004058&q={0}&msFlag=S&page={1}&sort=0'
# url = 'http://map.search.daum.net/mapsearch/map.daum?callback=jQuery18107186947884846974_1524545004058&q={0}&msFlag=A&page={1}&sort=0'


items = []
while len(items)<place_totalcount:
    itUrl = url.format(keyword,page)
    r = requests.get(itUrl,headers=headers)
    print(itUrl)
    print(r.encoding)
    print(r.headers['Content-Type'])

    content = r.content.decode('UTF-8')
    content = content.strip().replace("jQuery18107186947884846974_1524545004058 (","").strip(')')

    magicJsonData=json.loads(content)
    place_totalcount = magicJsonData['place_totalcount']
    # print(magicJsonData['place'])
    place = magicJsonData['place']
    items = items + place
    print(place_totalcount)
    print(len(place))
    print(len(items))
    if(place_totalcount==0):
        print(place)
    #print(items)
    page = page + 1
    time.sleep(0.1)

# json.load()





# GeoTransPoint tmpPt = new GeoTransPoint();
# GeoTransPoint out_pt = new GeoTransPoint();
#
# if (srctype == GEO) {
# tmpPt.x = D2R(in_pt.x);
# tmpPt.y = D2R(in_pt.y);
# } else {
# tm2geo(srctype, in_pt, tmpPt);
# }
#
# if (dsttype == GEO) {
# out_pt.x = R2D(tmpPt.x);
# out_pt.y = R2D(tmpPt.y);
# } else {
# geo2tm(dsttype, tmpPt, out_pt);
# //out_pt.x = Math.round(out_pt.x);
# //out_pt.y = Math.round(out_pt.y);
# }

