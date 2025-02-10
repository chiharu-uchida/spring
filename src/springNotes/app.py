from flask import Flask, jsonify, request

app = Flask(__name__)

# メモ取得
@app.route('/api/notes/<int:note_id>', methods=['GET'])
def getNote(note_id):
    return "This is your note"

if __name__ == '__main__':
    app.run(debug=True)