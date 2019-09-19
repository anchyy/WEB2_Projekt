from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_bootstrap import Bootstrap
import os 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
bootstrap = Bootstrap(app) 
app.config['SECRET_KEY']='gvpTrsDaf5vgzIzdzC2XKA'


#DATABASE location
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///charterdb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Category(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   boats = db.relationship('Boat', backref='category') 
   image = db.Column(db.String(100), nullable=False) 
   


# boatHasEquipments = db.Table('boatHasEquipments',
#     db.Column('boat_id', db.Integer, db.ForeignKey('boat.id'), primary_key=True),
#     db.Column('equipment_id', db.Integer, db.ForeignKey('boatEquipment.id'), primary_key=True)
# )
  

class BoatEquipment(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False) 



class Boat(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False, unique=True)
   length = db.Column(db.Integer, nullable=False)
   people_number = db.Column(db.Integer, nullable=False)
   cabine = db.Column(db.Integer)
   toilets= db.Column(db.Integer)
   engine = db.Column(db.String, nullable=False)
   fuel = db.Column(db.Integer, nullable=False)
   category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
   price_season = db.Column(db.Numeric, nullable=False)
   price_outOfSeason = db.Column(db.Numeric, nullable=False)
   #equipments = db.relationship('Boat_Equipment', secondary=boatHasEquipments, backref=db.backref('boat', lazy='dynamic'))
   images = db.relationship('BoatImage', backref='boat') 
   reservations = db.relationship('Reservation', backref='boat') 
   image = db.Column(db.String(200), nullable=False)

boatHasEquipments = db.Table('boatHasEquipments',
   db.Column('boat_id', db.Integer,db.ForeignKey(Boat.id), nullable=False),
   db.Column('equipment_id',db.Integer,db.ForeignKey(BoatEquipment.id),nullable=False),
   db.PrimaryKeyConstraint('boat_id', 'equipment_id') )

class BoatImage(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   boat_id = db.Column(db.Integer, db.ForeignKey('boat.id'))
   image = db.Column(db.String(100), nullable=False) 

    

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   surname = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String, nullable=False)
   password = db.Column(db.Integer, nullable=False)
   telephone = db.Column(db.String, nullable=False)
   birth_date = db.Column(db.Date, nullable=False)
   address = db.Column(db.String(200))
   reservations = db.relationship('Reservation', backref='user') 

class Reservation(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   update_date = db.Column(db.Date)
   create_date = db.Column(db.Date)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   boat_id = db.Column(db.Integer, db.ForeignKey('boat.id'), nullable=False)
   date_from = db.Column(db.Date, nullable=False)
   date_to = db.Column(db.Date, nullable=False)
   description = db.Column(db.String(300))
   reservation_cancellation = db.Column(db.Boolean)
   boat_name = db.Column(db.String(300))
   
 
 
 
@app.route('/')
def index():   
   categories = Category.query.all() 
   return render_template('index.html', categories=categories)

@app.route('/details/<id>')
def details(id):  
   result = Boat.query.filter(Boat.category_id==id)
   return render_template('details.html', boatList = result )

@app.route('/register', methods=['GET','POST'])
def register():
   if request.method == 'POST': 
      name = request.form.get('name')
      surname =request.form.get('surname')
      email =request.form.get('email')
      password =request.form.get('password') 
      contact =request.form.get('contact')
      address =request.form.get('address') 
      user =  User(name=name, surname=surname, email=email, password=generate_password_hash(password), telephone=contact,birth_date=datetime.now(), address=address)
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('index'))

   return render_template('register.html')

 #  https://www.youtube.com/watch?v=d04xxdrc7Yw
     


@app.route('/reservation/<id>', methods=['GET','POST'])
def reservation(id):  
   if request.method == 'POST':
      email =request.form.get('email')
      datumOd =request.form.get('datefrom') 
      datumDo =request.form.get('dateto')
      boatId= request.form.get('boatId')
      description= request.form.get('description')
      boatName = request.form.get('boat_name')
      user = User.query.filter(User.email == email).first()  
      reservation =  Reservation( date_from=datetime.strptime(datumOd, '%Y-%m-%d'), date_to=datetime.strptime(datumDo, '%Y-%m-%d'),create_date=datetime.now(), update_date=datetime.now(),user_id= user.id, boat_id=boatId,description=description, boat_name=boatName)
      db.session.add(reservation)
      db.session.commit()
      return redirect(url_for('index'))

   result = Boat.query.filter(Boat.id==id).first()
   images= BoatImage.query.filter(BoatImage.boat_id==id)
   return render_template('reservation.html', boat = result, images=images )

     

@app.route('/addreservation', methods=['POST'])
def addReservation():   
   email =request.form.get('email')
   datumOd =request.form.get('datefrom') 
   datumDo =request.form.get('dateto')
   boatId= request.form.get('boatId')
   description= request.form.get('description')
   
   user = User.query.filter(User.email == email).first()
   reservation =  Reservation( date_from=datetime.datetime.strptime(datumOd, '%Y-%m-%d'), date_to=datetime.datetime.strptime(datumDo, '%Y-%m-%d'),update_date=datetime.now(),user_id= user.id, boat_id=boatId,description=description)
   db.session.add(reservation)
   db.session.commit()
   return redirect(url_for('index'))



@app.route('/login', methods=['GET','POST'])
def login():  
   if request.method == 'POST':
      email =request.form.get('email')
      password =request.form.get('password')    

      user = User.query.filter(User.email == email).first()
      if user != None and check_password_hash(user.password, password):
         session["username"]= user.email
         session["ime"]= user.name
         session["prezime"]= user.surname
         return redirect(url_for('index')) 
      else:
         message="Krivi e-mail ili lozinka"
         return render_template('login.html', message=message)
   return render_template('login.html')

@app.route('/profile')
def profile():  
   user = User.query.filter(User.email == session['username']).first()
   reservation = Reservation.query.filter(Reservation.user_id == user.id)
   return render_template('profile.html', user= user, reservations = reservation)    

@app.route('/logout')
def logout():  
   session["username"]= None
   return redirect(url_for('index')) 

@app.route('/cancel/<id>')
def cancel(id):   
   reservation = Reservation.query.filter(Reservation.id == id).first()
   reservation.reservation_cancellation = True
   db.session.add(reservation)
   db.session.commit()
   return redirect(url_for('profile')) 

@app.route('/active/<id>')
def active(id):   
   reservation = Reservation.query.filter(Reservation.id == id).first()
   reservation.reservation_cancellation = False
   db.session.add(reservation)
   db.session.commit()
   return redirect(url_for('profile')) 



if __name__ == "__main__":
    app.run()

 