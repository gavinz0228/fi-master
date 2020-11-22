from urllib import request
import urllib.parse

def get(url):
    url = urllib.parse.unquote(url).replace(" ", "+")
    res = request.urlopen(url) 
    return res.read()

def post(url, data, headers = {}):
    req = request.Request(url, data=data.encode('ascii'), headers=headers, origin_req_host=None, method="POST")
    res = request.urlopen(req) 
    return res.read()