#! /usr/bin/env python
from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/data/<path:path>')
def get_all_books(path):
    return send_from_directory('data', path)
