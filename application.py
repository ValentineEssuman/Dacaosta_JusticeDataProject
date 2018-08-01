from flask import Flask, render_template, jsonify, request
from models import *
from models import db
#import sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = """postgres://mfpxswkssmeoqq:ff9d8b2937e91a5faf763c5971e6c4371a2b5c316e16225d16c2de5f4b909b80@ec2-174-129-33-29.compute-1.amazonaws.com:5432/d8gcvjt3rhvmo7"""
app.config['DEBUG'] = True
db.init_app(app)

@app.route("/")
def index():
    vessels = Vessel.query.all()
    return render_template("index.html", vessels= vessels)

@app.route("/viewvessel", methods=["POST"])
def viewvessel():
    """Check a Vessel."""

    # Get form information.
    name = request.form.get("name")
    try:
        vessel_id = int(request.form.get("vessel_id"))
    except ValueError:
        return render_template("error.html", message="Invalid Vessel number.")

    # Make sure the vessel exists.
    vessel = Vessel.query.get(vessel_id)
    if not vessel:
        return render_template("error.html", message="No such vessel with that id.")

    # Add passenger.
    Vessel.add_vessel(name)
    return render_template("success.html")
