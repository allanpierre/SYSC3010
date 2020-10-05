import httplib
import urllib
import time
key = "54CDA6FJF4RCJ92C"
def task():
    while True:
        params = urllib.urlencode({'field1': "allanpierre@cmail.carleton.ca", 'key':key }) 
        params = urllib.urlencode({'field2': "L2-M-9", 'key':key }) 
        params = urllib.urlencode({'field3': "c", 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
if __name__ == "__main__":
        while True:
                thermometer()
