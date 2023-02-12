from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
import json
import urllib.request
import os


db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwwqretrqwwa'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class Hotel(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   hname = db.Column(db.String(150))
   rating= db.Column(db.String(150))
    
with app.app_context():
        db.create_all()

@app.route('/',methods=['GET', 'POST'])
def HotelCall():
    if request.method=='POST':

       user = request.form.get('name')
       url = "http://127.0.0.1:5000/?user={}".format(user)
       response = urllib.request.urlopen(url)
       data = response.read()
       if data==b'T':
         print("yes")
       #print(data)
         cur_hname=request.form.get('hname')
         cur_rating=request.form.get('rating')
         cur_hotel=Hotel(hname=cur_hname,rating=cur_rating)
         db.session.add(cur_hotel)
         db.session.commit()
         return "success"
       else:
         return "not registered"
       
    else:
       return render_template('user.html')

@app.route('/hotels')
def h():
   hotels=Hotel.query.all()
   tempHotel=[]
   for hotel in hotels:
      tempHotel.append((hotel.hname,hotel.rating))
   
   return json.dumps(tempHotel)

if __name__ == '__main__':
   app.run(debug=True,port=3000)
