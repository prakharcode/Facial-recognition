from bs4 import BeautifulSoup
import urllib2

site_list = ['https://www.google.co.in/search?biw=1920&bih=549&tbm=isch&sa=1&ei=jXAsWv25O8zfvgTi676QBw&q=narendra+modi+close+up&oq=narendra+modi+close&gs_l=psy-ab.3.0.0.416302.804922.0.806151.35.29.0.1.1.0.254.2941.0j3j10.17.0....0...1c.1.64.psy-ab..18.12.2506.0..0i67k1.228.kvOn60q1L8Y',
            'https://www.google.co.in/search?ei=tXMsWp6UHsTUvgSZsLyoBw&yv=2&tbm=isch&q=narendra+modi+close+up&vet=10ahUKEwjewtDEjP7XAhVEqo8KHRkYD3UQuT0IPCgB.tXMsWp6UHsTUvgSZsLyoBw.i&ved=0ahUKEwjewtDEjP7XAhVEqo8KHRkYD3UQuT0IPCgB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s',
            'https://www.google.co.in/search?ei=tXMsWp6UHsTUvgSZsLyoBw&yv=2&tbm=isch&q=narendra+modi+close+up&vet=10ahUKEwjewtDEjP7XAhVEqo8KHRkYD3UQuT0IPCgB.tXMsWp6UHsTUvgSZsLyoBw.i&ved=0ahUKEwjewtDEjP7XAhVEqo8KHRkYD3UQuT0IPCgB&ijn=2&start=200&asearch=ichunk&async=_id:rg_s,_pms:s',]
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
folder ="./images/narendra/"
for site in site_list:
    print "Opening Url: "+site+"..."
    cfc = 0
    log = open(folder+"log.txt",'r')
    pfc = int(log.read())
    log.close()
    req_obj = urllib2.Request(site,headers=hdr)
    content = urllib2.urlopen(req_obj).read()
    data = BeautifulSoup(content,'html.parser')
    img_list = data.find_all('img')
    if img_list!=[]:
        img_link_list = list()
        for img in img_list:
            img_str = str(img)
            img_str = img_str[img_str.find('data-src'):(img_str.find('data-sz'))].strip()
            img_link_list.append(img_str[img_str.find('https'):-1])
    else:
        img_link_list = str(data).split('src=\\')
        for k,i in enumerate(img_link_list):
            img_link_list[k] = i[1:(i.find('jsaction')-3)].strip()
            img_link_list[k] = img_link_list[k].replace('\\','')
    for count,img in enumerate(img_link_list):
        try:
            if img!="":
                lc = folder+str(count+1+pfc)+".jpg"
                print "image: "+str(count+1+pfc)
                fp = open(lc,'wb')
                fp.write(urllib2.urlopen(img).read())
                fp.close()
                cfc = count+1+pfc
        except:
            pass
    log = open(folder+"log.txt",'w')
    log.write(str(cfc))
    log.close()
