from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
     lists=['riya','sheena','bora']
     return render_template('temp1.html',list1=lists)

if __name__ == '__main__':
     app.run(debug=True)
