import re
import urllib
import urllib.request
import http.cookiejar as cookielib
import base64

url1 = 'http://hub.hust.edu.cn/index.jsp'
url2 = 'http://hub.hust.edu.cn/hublogin.action'
url3 = 'http://s.hub.hust.edu.cn/hublogin.action'
url4 = 'http://s.hub.hust.edu.cn:80/aam/score/CourseInquiry_ido.action'

#用cookielib库保存cookies
cj = cookielib.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

def geturl1():
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    }
    req1 = urllib.request.Request(url1,headers=headers1)
    response1 = urllib.request.urlopen(req1)
    data1 = response1.read().decode('utf-8')
    re1 = re.compile(r'<input type="hidden" name="ln" value="(.*?)"/>')
    ln = re1.findall(data1)
    print(ln[0])
    return ln[0]

def geturl2(ln):
    headers2 = {
        'Host': 'hub.hust.edu.cn',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://hub.hust.edu.cn/index.jsp',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.8'
    }
    pwd = base64.b64encode(b'zsn177288')
    params2 = {'username':'U201417238','password':pwd,'ln':ln}
    bdata2 = urllib.parse.urlencode(params2).encode('ascii')
    req2 = urllib.request.Request(url2, bdata2, headers=headers2)
    response2 = urllib.request.urlopen(req2)
    code = response2.code
    data2 = response2.read().decode('utf-8')
    print(code)
    return data2

def geturl3(data2):
    headers3 = {
        'Host': 's.hub.hust.edu.cn',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://hub.hust.edu.cn/hublogin.action',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.8'
    }
    re2 = re.compile(r'<input type="hidden" name="(.*?)" value="(.*?)"/>')
    re2result = re2.findall(data2)
    re3 = re.compile(r'<input type="hidden" id="password" name="password" value="(.*?)">')
    re3result = re3.findall(data2)
    pwd = re3result[0]
    params3 = {
        'usertype':'xs',
        'username':'U201417238',
        'password':pwd,
        'url':'http://s.hub.hust.edu.cn/',
        'key1':re2result[0][1],
        'key2':re2result[1][1],
        'F_App':re2result[2][1],
    }
    bdata3 = urllib.parse.urlencode(params3).encode('ascii')
    req3 = urllib.request.Request(url3, bdata3, headers=headers3)
    response3 = urllib.request.urlopen(req3)
    code = response3.code
    # data3 = response3.read().decode('utf-8')
    print(code)
    print('登陆成功')

def getcourse():
    print('等待抓取课程')
    headers4 = {
        'Host': 's.hub.hust.edu.cn',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest',
        'Content - Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://s.hub.hust.edu.cn/aam/report/scheduleQuery.jsp',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.8'
    }
    params4 = {
        'start':'2016-09-26',
        'end':'2016-11-07'
    }
    bdata4 = urllib.parse.urlencode(params4).encode('ascii')
    req4 = urllib.request.Request(url4, bdata4, headers=headers4)
    response4 = urllib.request.urlopen(req4)
    data4 = response4.read().decode('utf-8')
    print(data4)

if __name__ == '__main__':
    ln = geturl1()
    data2 = geturl2(ln)
    geturl3(data2)
    getcourse()