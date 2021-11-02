from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return "YOU DID IT ! I'm running on host : {}".format(request.host)

if __name__ == '__main__':
    app.run()
