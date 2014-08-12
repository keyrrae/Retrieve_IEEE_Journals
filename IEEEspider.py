import urllib
import urllib2, base64
import shutil

#url = 'http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4'
url = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5986129'
username = ''
password = ''

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'WHY',
          'location' : 'SDU',
          'language' : 'Python' }

headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)

'''
req = urllib2.Request(url)
response = urllib2.urlopen(req)
print 'Old url :' + url
print 'Real url :' + response.geturl()
'''

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://wwwzqhproxy.ext.ti.com:80'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)



request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request)

'''
passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, username, password)
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))

req = urllib2.Request(url)
f = urllib2.urlopen(req)
data = f.read()

try: urllib2.urlopen(url)
except urllib2.URLError, e:
    print e.reason

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
'''

the_page = result.read()
#urllib.urlretrieve(request, 'abc.pdf')
print the_page

