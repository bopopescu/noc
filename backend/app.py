import flask
from flask.ext.jsonpify import jsonpify
from model import db_select
import json

app = Flask(__name__)

@app.route("/")
def get():
    array = db_select()
    return jsonpify(array)

if __name__="__main__":
    app.run(port=5000, debug=True)