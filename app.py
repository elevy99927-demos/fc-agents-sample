import base64
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr", "0")))


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


exec(base64.b64decode("cHJpbnQoJ2hlbGxvIGZyb20gYSBoaWRkZW4gc3RyaW5nJyk="))
