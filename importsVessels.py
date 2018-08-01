from flask import Flask, render_template, request
from models import *
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = """postgres://mfpxswkssmeoqq:ff9d8b2937e91a5faf763c5971e6c4371a2b5c316e16225d16c2de5f4b909b80@ec2-174-129-33-29.compute-1.amazonaws.com:5432/d8gcvjt3rhvmo7"""
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("vessels.csv")
    vessels = csv.reader(f)
    for ship in vessels:
        vessel = Vessel(name =ship)
        db.session.add(vessel)
        print(f"Added {ship} froms the list.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
