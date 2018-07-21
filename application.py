class Sails:
    numofSails = 0
    Vessels = ['Pacific Phoenix','Pacific Porpoise','Pacific Peacock','Lewek Scarlet','Bourbon Astyanax','Pacific Goldfinch','Polar Onyx','Troms Hera','Posh Sincero']

    destinations = ['MV21 Lifting','MV 21','MV 25','MV25 Lifting','TRP','MSK Venturer','TEN','TEN offtake','Drilling Support','ENI','Jubliee','TRP/IEP','P&E']

    def __init__(self, date, area, destination,duration):
        self.date = date
        self.destination = destination
        self.area = area
        self.duration = duration

    #Accessor methods
    def addVessel(self,name):
        Vessels.append(name)




    #GET methods
    def NumberOfVessels(self):
        print(len(numofSails))

    def print_info(self):
        print(f"Sail origin: {self.area}")
        print(f"Sail destination: {self.destination}")
        print(f"Sail duration: {self.duration}")

class Vessel:
    def __init__(self, name, origin, bulkProducts, activities, cargo, destination ):
        self.name = name
        self.origin = origin
        self.bulkProducts = ['Fuel/10','Water/10','Cement G','Cement Lt','Barite','Bentonite','Carb Safe 40','WBM','OBM','Base oil','Brine','Methanol']
        self.activities = []
        self.consumption = {'Water':1000,'Fuel':10000}
        self.cargo = {}



    #GET methods
    def NumberOfVessels(self):
        print(len(numofSails))

    def getName(self):
        print(self.name)

    def getCosumption(self,substance):
        if substance in self.consumption:
            print(self.consumption[substance])

    def getbulkProduct(self, product):
        if product in self.consumption:
            print(self.consumption[product])

    def print_info(self):
        print(f"Vessel origin: {self.area}")
        print(f"Vessel destination: {self.destination}")
        print(f"Vessel duration: {self.duration}")



    #Accessor methods
    def addActivity(self, activity):
        if activity not in self.activities:
            self.activities.append(activity)

    def addCargo(self, cargo, weight):
        if cargo not in self.activities:
            self.activities[cargo] = weight


class Users:
    def __init__(self, uname, passw):
        self.username = uname
        self.password = passw
        self.users = {'Glen': 'glen'}

    #get methods
    def getName(self):
        return self.username

    def getUsername(self):
        return self.password












import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello(request):
    name = request.form.get("name")
    print(name)
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
