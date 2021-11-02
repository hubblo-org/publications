from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return "YOU DID IT ! I'm running on host : {}\n Client is : {}\n".format(request.environ['SERVER_ADDR'], request.remote_addr)

if __name__ == '__main__':
    app.run()
