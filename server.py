from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.get_json()
    first=data['first']
    second=data['second']
    sum=first+second
    return jsonify({'result':sum})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
        data=request.get_json()
    first=data['first']
    second=data['second']
    difference=first+second
    return jsonify({'result':difference})
  

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
