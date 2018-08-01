

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pasword = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Vessel(db.Model):
    __tablename__ = "vessels"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    vessel_Activities = db.relationship("Activity", backref="vessel", lazy=True)
    vessel_ProductCons = db.relationship("ProductCons", backref="vessel", lazy=True)
    #bulksProducts = db.relationship("BulksProducts", backref="vessel", lazy=True)
    #vessel_id = db.Column(db.Integer, db.ForeignKey("sails.id"), nullable=False)



    def add_vessel(self, name):
        p = Vessel(name=name, vessel_id=self.id)
        db.session.add(p)
        db.session.commit()


class Activity(db.Model):
    __tablename__ = "activities"
    id = db.Column(db.Integer, primary_key=True)

    #activities times
    Cargo_Ops = db.Column(db.Integer, nullable=True)
    Port = db.Column(db.Integer, nullable=True)
    Passage = db.Column(db.Integer, nullable=True)
    Standby = db.Column(db.Integer, nullable=True)

    vessel_id = db.Column(db.Integer, db.ForeignKey("vessels.id"), nullable=False)



class ProductCons(db.Model):
    __tablename__ = "productCons"

    id = db.Column(db.Integer, primary_key=True)
    Fuel_10 = db.Column(db.Integer, nullable=True)
    Water_10 = db.Column(db.Integer, nullable=True)
    Used_Fuel = db.Column(db.Integer, nullable=True)
    Used_Water = db.Column(db.Integer, nullable=True)

    vessel_id = db.Column(db.Integer, db.ForeignKey("vessels.id"), nullable=False)

# class BulksProducts(db.Model):
#     __tablename__ = "bulksProducts"
#
#     Brine = db.Column(db.Integer, nullable=True)
#     Cement = db.Column(db.Integer, nullable=True)
#     Barite = db.Column(db.Integer, nullable=True)
#     Cement_G  = db.Column(db.Integer, nullable=True)
#     Cement_Lt = db.Column(db.Integer, nullable=True)
#     Bentonite = db.Column(db.Integer, nullable=True)
#     Carb_Safe_40 = db.Column(db.Integer, nullable=True)
#     WBM = db.Column(db.Integer, nullable=True)
#     OBM = db.Column(db.Integer, nullable=True)
#     Base_oil = db.Column(db.Integer, nullable=True)
#     Methanol = db.Column(db.Integer, nullable=True)
#
#     vessel_id = db.Column(db.Integer, db.ForeignKey("vessels.id"), nullable=False)
