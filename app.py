import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from help import apology, login_required
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()
app = Flask(__name__)
key=os.getenv("ENCRYPTION_KEY").encode()
cipher = Fernet(key)

app.config["DEBUG"] = os.getenv("FLASK_ENV") == "development"

app.secret_key = os.getenv("SECRET_KEY")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db=SQL("sqlite:///vegan.db")


@app.route("/register", methods=["POST", "GET"])
def register():
        if request.method=="POST":
            username=request.form.get("username")
            password=request.form.get("password")
            password2=request.form.get("password2") 
            if not (username and password and password2):    
                 return apology("missing username/password/repeat password")
            if (password!=password2):
                 return apology("not matching passwords")
            hash=generate_password_hash(password)
            fila=db.execute("SELECT * AFROM users WHERE name =?", username)
            if fila:
                 return apology("name in use")
            
            db.execute("INSERT INTO users (name,hash) VALUES (?, ?)", username, hash)
            return redirect("/login")
        else:
             return render_template("/register.html")

            
@app.route("/login", methods=["POST", "GET"])
def login():
    session.clear()
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if not (username and password):
            return apology("usernmae or password missing")
        rows=db.execute("SELECT * FROM users WHERE name=?", username)

        if len(rows)!=1 or not check_password_hash(rows[0]["hash"], password):
             return apology ("incorrect username or password")
        session["user_id"]=rows[0]["id"]
        return redirect ("/")
    else:
         return render_template("login.html")
    
          
         
@app.route("/logout")
@login_required
def logout():
     session.clear()
     return redirect("/login") 

@app.route("/")
@login_required
def index():
    row=db.execute("select name from users where id=?",session["user_id"])
    if not row:
         session.clear()
         return redirect ("/login")
    username=row[0]["name"]
    return render_template("index.html", username=username)


@app.route("/passwords", methods=["GET", "POST"])
@login_required
def passwords():
     if request.method=="POST":
          web_page=request.form.get("web_page")
          username=request.form.get("username")
          password=request.form.get("password").encode("utf-8")
          password_enc=cipher.encrypt(password)
          id=session["user_id"]
          if not (web_page and username and password):
               return apology("missing a input in passwords")  
          db.execute("INSERT INTO passwords(user_id, web_page, username, password) VALUES(?,?,?,?)",id, web_page, username, password_enc)
          return redirect("/passwords")
     
     else:
          id=session["user_id"]
          print(id)
          rows=db.execute("SELECT * FROM passwords WHERE user_id=?",id)
          for row in rows:
               row["password"]=cipher.decrypt(row["password"]).decode("utf-8")
          return render_template("/passwords.html", rows=rows)
     
@app.route("/delete", methods=["POST"])
def delete():
     id_passwords=request.form.get("id", type=int)
     print(id_passwords)
     rows= db.execute("DELETE from passwords WHERE id=?",id_passwords)
     if rows:
          print("correct delete")
     return redirect("/passwords")

if __name__ == "__main__":
    app.run(debug=True)