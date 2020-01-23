from flask import Blueprint, render_template, request
import database

si_su = Blueprint('si_su', __name__)
main = Blueprint('main', __name__)

selectedID = 0
cardID = 0
addressID = 0

@si_su.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
    return render_template("index.html")

@si_su.route("/signup", methods=["GET", "POST"])
def signup ():
    if request.method == "POST":
        firstName = request.form.get('fname')
        lastName = request.form.get('lname')
        email = request.form.get('email')
        userName = request.form.get('username')
        password = request.form.get('pass')

        database.register(firstName, lastName, email, userName, password)
        return render_template("index.html")

    return render_template("signup.html")

@si_su.route("/", methods=["POST"])
def signedUp ():

    return render_template("mainpage.html")
    # return f'{firstName} <br> {lastName} <br> {email} <br> {userName}<br>  {password}'

@main.route("/credit", methods=["GET", "POST"])
def credit():
    tup = database.viewCredit(request.form['credit-card'], request.form['cc_number'], request.form['street'], request.form['city'], request.form['state'], request.form['country'], request.form['postal'])
    return render_template("mainpage.html", cc_id = tup[0], cc_number=tup[1], street=tup[2], city=tup[3], state=tup[4], country=tup[5], postal=tup[6])

@main.route("/addr", methods=["GET", "POST"])
def addr():
    tup = database.viewAddr(request.form['curr_addr'], request.form['addr_street'], request.form['addr_city'], request.form['addr_state'], request.form['addr_country'], request.form['addr_postal'])
    return render_template("mainpage.html", curr_addr = tup[0], addr_street=tup[1], addr_city=tup[2], addr_state=tup[3], addr_country=tup[4], addr_postal=tup[5])

@main.route("/main")
def mainpage():
    return render_template("mainpage.html")

@main.route("/main", methods=['POST'])
def signInForm():
    name = request.form.get('username')
    password = request.form.get('pass')
    
    if "signIn" in request.form:
        if database.login(name, password):
            return render_template("mainpage.html")
    elif "signUp" in request.form:
        return render_template("signup.html")

    return render_template("index.html")

@main.route("/results", methods=['POST', 'GET'])
def displayResults():
    origin = request.form['origin']
    destination = request.form['destination']
    checkIn = request.form['check-in']
    checkOut = request.form['check-out']
    connections = request.form['maxConnections']
    economy = request.form['economy']

    table = database.updateTable(checkIn, checkOut)
    data = database.searchRoutes(int(connections), 0, [], origin, destination, economy)
    li = []
    for v in data:
        li.append([])
        for x in v:
            li[-1].append(table[x])

    if checkOut != '':
        data = database.searchRoutes(int(connections), 0, [], destination, origin, economy)
        for v in data:
            li.append([])
            for x in v:
                li[-1].append(table[x])

    # At this point in the code, "li" is a list of flights, where each flight is a dictionary
    return render_template("displayResults.html", results=li)

@main.route("/results")
def sendResults(data):
    print(data)    

@main.route("/bookings", methods=['POST'])
def showBookings ():
    seatClass='economy'
    cc_id=1
    airCode = request.form.get('a-code', 'YH')
    flightNum = request.form.get('flightNum', 'HS1781')
    cc = database.getCreditByID(cc_id)
    database.insertBooking(flightNum, airCode, seatClass, cc)

    bookings = database.getBookings()

    return render_template("bookings.html", bookings=bookings)

@main.route("/bookings", methods=['GET'])
def displayBookings():
    booking = database.getBookings()

    return render_template("bookings.html", bookings=booking)

@main.route("/delete", methods=['GET', 'POST'])
def deleteBooking():
    flightNumber = request.form.get('flightNum', 'HS1781')
    ID = request.form.get('userID', '347786204795292')

    database.deleteBooking(ID, flightNumber)

    #return render_template("bookings.html")
