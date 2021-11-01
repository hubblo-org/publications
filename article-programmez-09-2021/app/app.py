# save this as app.py
from flask import Flask


app = Flask(__name__)

#@app.route("/")
#def fibo():
#    response = "\n la suite fibonacci est : "
#    response += str(fibonacci(30))
#    return response
#
#def fibonacci(n):
#    if(n <= 1):
#        return n
#    else:
#        return (fibonacci(n-1) + fibonacci(n-2))
#    response = ""
#    for i in range(n):
#        response += str(fibonacci(i))
#    return response+", "

@app.route("/")
def fibo():
    nterms = 30
    n1 = 0
    n2 = 1

    response = "\n la suite fibonacci est : {}, {},".format(n1,n2)

    for i in range(2, nterms):
      suivant = n1 + n2
      response += "{},".format(suivant)

      n1 = n2
      n2 = suivant

    return response
