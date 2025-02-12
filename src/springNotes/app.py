from flask import Flask, jsonify, request
# from mysql_setting import Session
from mysql_setting import Session
from models import User, Note
import json

app = Flask(__name__)

# ノート取得
@app.route('/api/notes/<int:note_id>', methods=['GET'])
def getNote(note_id):
    noteinfojson = dataaccess(note_id)

    return noteinfojson

def dataaccess(note_id):
    a = Session.query(Note).filter(Note.note_id == note_id)

    return a[0].note_name


if __name__ == '__main__':
    app.run(debug=True)