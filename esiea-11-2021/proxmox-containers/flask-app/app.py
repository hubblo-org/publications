from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return "YOU DID IT ! Client is : {}\n".format(request.remote_addr)

if __name__ == '__main__':
    app.run()
