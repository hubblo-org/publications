from flask import Flask, request
from os import environ, path
import random

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    service_host = ""
    for k,v in environ.items():
        if "SERVICE_SERVICE_HOST" in k:
            service_host = v
    return "<html><body><h1>2Wheels</h1><p><a href='twowheels/buy'>Buy one !</a></p><p><img src='https://d2p6e6u75xmxt8.cloudfront.net/2/2016/02/PNemeyEaQcurH6p6Uko3_Bike-Tiny-Bike-2.gif'/></p></p>Client is : {}</p><p>Container hostname: {}</p><p>Host url: {}</p><p>Service host: {}</p></body></html>".format(request.remote_addr, environ.get('HOSTNAME'), request.host_url, service_host)

@app.route('/buy', methods = ['GET'])
def buy():
    bikes_left = random.randrange(50,200)
    remaining_colors = "<b>COULDN'T GET THE DATA</b></p><p><img src='https://d2p6e6u75xmxt8.cloudfront.net/2/2016/02/v6E6NPPlSpeDwi5VRcCY_Bike-Flip-Fail.gif'/>"
    if path.exists("/var/colors/colors"):
        with open("/var/colors/colors") as fd:
            remaining_colors = "<ul>"
            for line in fd.readlines():
                remaining_colors += "<li>{}</li>".format(line)
            remaining_colors += "</ul>"
            remaining_colors += "</p><p><img src='https://d2p6e6u75xmxt8.cloudfront.net/2/2016/02/giphy1.gif'/>"
    service_host = ""
    for k,v in environ.items():
        if "SERVICE_SERVICE_HOST" in k:
            service_host = v
    return "<html><body><h1>2Wheels shop</h1><p>There are {} bikes left ! Send us and email to get one !</p><p>Remaining colors : {}</p>Client is : {}</p><p>Container hostname: {}</p><p>Host url: {}</p><p>Service host: {}</p></body></html>".format(bikes_left, remaining_colors, request.remote_addr, environ.get('HOSTNAME'), request.host_url, service_host)

if __name__ == '__main__':
    app.run()
