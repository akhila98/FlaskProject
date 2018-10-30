from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def index():
     name="Dhiraj"
     dict={'daniel':'Heyya coming for movie','Amar':'Yes,i m ready'}
     return render_template('temp4.html',result=dict,name1=name)

if __name__ == '__main__':
     app.run(debug=True)
