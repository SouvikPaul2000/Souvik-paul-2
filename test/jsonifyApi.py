import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


books = [
    
    {'id': 1,
     'title': 'ABC',
     'author': 'XYZ',
     'published': '1973'},
    {'id': 2,
     'title': 'EFG',
     'author': 'IJK',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>BOOK</h1>
<p>A HOME PAGE</p>'''



@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()
