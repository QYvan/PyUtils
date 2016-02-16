# encoding: utf-8
#!/usr/bin/python
import httplib
import urllib
import json

##POST请求
def postWithJson(host,uri,params):
    try:
        headers = {"Content-Type": "application/json","Content-Encoding": "UTF-8"}
        conn = httplib.HTTPConnection(host)
        conn.request("POST", uri, json.dumps(params), headers)
        response = conn.getresponse()
        data = response.read()
    except Exception as error:
        print('postWithJson error')
        print(error)
    finally:
        if conn is not None:
            conn.close()

##发送post请求并编码URL
def postWithUrlEncode(host,uri,params):
    try:
        headers = {"Content-Encoding": "UTF-8","Content-type": "application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection(host)
        params = urllib.urlencode(params)
        conn.request("POST", uri, params, headers)
        response = conn.getresponse()
        data = response.read()
    except Exception as error:
        print('postWithJson error')
        print(error)
    finally:
        if conn is not None:
            conn.close()

##GET请求
def get(url,headers = None):
    try:
        conn = httplib.HTTPConnection(url)
        conn.request("GET","/")
        response = conn.getresponse()
        data = response.read()
        return data
        print(data)
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    print(get("www.google.com"))

