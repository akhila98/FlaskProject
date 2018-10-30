from flask import Flask,render_template
app= Flask(__name__)

@app.route('/index')
def index():
     user={'username':"Dhiraj"}
     posts=[
          {
               'author':{'username':'Daneil'},
               'body':'Beautiful'
               },
          {
               'author':{'username':'Maithili'},
               'body':'hiii'
          }
          ]
     return render_template('index.html',user=user,posts=posts)
if __name__ == '__main__':
     app.run(debug=True)
          
