from flask import Flask
app= Flask(__name__)

@app.route('/hi/<name>')
def hello_name(name):
     return ' Hello %s!' %name

@app.route('/hi/<int:id>')
def hello_name1(id):
     return ' %d!' %id


if __name__ == '__main__':
     app.run(debug=True)
