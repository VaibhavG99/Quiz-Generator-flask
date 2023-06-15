from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL



app = Flask(__name__)

#DEFINING database
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='quiz' 
mysql = MySQL(app)




#oop for creating tables inside databse





@app.route("/quiz/play" , methods = ['POST','GET'] )
def quizpage():
    if (request.method == 'POST'):
        Q_no = request.form.get('q_no') 
        ques = request.form.get('ques')
    return render_template('quizpage.html')

@app.route("/")
def hello():
    return render_template('homepage.html')
@app.route("/home")
def hell():
    return render_template('homepage.html')

@app.route("/joinquiz")
def joinquiz():
    return render_template("joinquiz.html")

@app.route("/abt")
def aboutpage():
    return render_template("about.html")

@app.route("/create")
def createpage():
    return render_template("createquiz.html")

@app.route("/create/2", methods = ['POST'])
def getvalue():                                                     #fetching values from the html form
    title = request.form['title']
    desc= request.form['desc']
    k = int(request.form['n'])
    time = request.form['time']
    level = request.form['difficulty']
    dict={"title":title , "no. of questions": k, "time alloted" : time , "level" : level , "desc" : desc }
    
    #INSERTING FORM DATA IN DATABSE DEFINED ABOVE
    cur= mysql.connection.cursor()
    cur.execute("INSERT INTO quiz_desc(Title,description,difficulty,numQ) VALUES(%s,%s,%s,%s)",(title,desc,level,k))
    mysql.connection.commit()
    cur.close()


    return render_template("quizcreation.html", n=k)
@app.route("/create/submit", methods = ['POST'])
def submitquiz():
    option_list =[]
    q = request.form['ques']
    for i in range (0,4):
        opt = request.form['opt']
        option_list.append(opt)
    print(option_list)
    dict1={q: option_list}
    return render_template('submit.html')


app.run(debug = True)