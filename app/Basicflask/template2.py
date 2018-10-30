from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
     dict={'name':'riya','Name':'sheena','place':'bora'}
     return render_template('temp2.html',result=dict)

if __name__ == '__main__':
     app.run(debug=True)
