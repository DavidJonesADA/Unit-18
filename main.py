from guizero import *
import sqlite3
from datetime import datetime




with sqlite3.connect("Silver Dawn Data.db") as db:
   cursor = db.cursor()

if (db):
    # Carry out normal procedure
    print ("Connection successful")
else:
    # Terminate
    print ("Connection unsuccessful")

res = cursor.execute("SELECT * FROM sqlite_master")
for name in res:
    print (name[1])





def tickboxes():
    if requirements_checkbox.value == 1:
        requirements_text.enable()
    elif requirements_checkbox.value == 0:
        requirements_text.disable()

def new_customer():
    customer_window = Window(app, title = "Add Customer", bg = (253, 71, 74), height = 725)
    picture = Picture(customer_window, image="Logo.gif")

    text = Text(customer_window, text= "New Customer")
    text.text_color = "white"
    text.text_size = 20

    text = Text(customer_window, text= "First Name")
    text.text_color = "white"
    first_name = TextBox(customer_window)
    first_name.width = 15

    text = Text(customer_window, text= "Last Name")
    text.text_color = "white"
    last_name = TextBox(customer_window)
    last_name.width = 15


    text = Text(customer_window, text= "Address 1")
    text.text_color = "white"
    address1 = TextBox(customer_window)
    address1.width = 40

    text = Text(customer_window, text= "Address 2")
    text.text_color = "white"
    address2 = TextBox(customer_window)
    address2.width = 40

    text = Text(customer_window, text= "City")
    text.text_color = "white"
    city = TextBox(customer_window)
    city.width = 15

    text = Text(customer_window, text= "Post Code")
    text.text_color = "white"
    post_code = TextBox(customer_window)
    post_code.width = 15

    text = Text(customer_window, text= "Phone Number")
    text.text_color = "white"
    phone_number = TextBox(customer_window)
    phone_number.width = 25

    text = Text(customer_window, text= "Email")
    text.text_color = "white"
    email = TextBox(customer_window)
    email.width = 30

    global requirements_checkbox
    global requirements_text

    requirements_checkbox = CheckBox(customer_window, text="Special Requirements?", command=tickboxes)
    requirements_checkbox.text_color = "white"

    requirements_text = TextBox(customer_window, text="No Requirements")
    requirements_text.width = 25
    requirements_text.disable()

    customer_button = PushButton(customer_window, text="Enter", command=add_new_customer, args=[customer_window, first_name, last_name, address1, address2, post_code, city, phone_number, email, requirements_text])
    customer_button.width = 15
    customer_button.text_color = "white"

    home_button = PushButton(customer_window, text="Home", align="bottom", command=customer_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"


def add_new_customer(customer_window, first_name, last_name, address1, address2, post_code, city, phone_number, email, requirements_text):
    FirstName = first_name.value
    Surname = last_name.value
    Email = email.value
    PhoneNumber = phone_number.value
    SpecialNotes = requirements_text.value

    Address1 = address1.value
    Address2 = address2.value
    City = city.value
    Postcode = post_code.value

    if FirstName == '' or Surname == '' or Email == '' or PhoneNumber == '' or Address1 == '' or Address2 == '' or City == '' or Postcode == '':
        print ("error")
    else:
        cursor.execute(("""INSERT INTO Address(Address1, Address2, Postcode, City) VALUES(?, ?, ?, ?)"""),(Address1, Address2, City, Postcode))
        addressID = cursor.lastrowid
        print(addressID)
        cursor.execute(("""INSERT INTO Customer(AddressID, FirstName, Surname, Email, PhoneNumber, SpecialNotes) VALUES(?, ?, ?, ?, ?, ?)"""),(addressID, FirstName, Surname, Email, PhoneNumber, SpecialNotes))
        db.commit()




def new_booking():
    showAllCustomers = []
    showAllDestinations = []

    cursor.execute("SELECT * FROM Customer")
    result = cursor.fetchall()
    for row in result:
       showAllCustomers.append(str(row[0]) + ' ' +  str(row[2]) + ' ' + str(row[3]))
    cursor.execute("SELECT * FROM Destination")
    result2 = cursor.fetchall()
    for row in result2:
       showAllDestinations.append(str(row[0]) + ' ' +  str(row[1]))




    booking_window = Window (app, title = "Add Booking", bg = (253, 71, 74), height = 600)
    picture = Picture(booking_window, image="Logo.gif")

    text = Text(booking_window, text="Add Booking")
    text.text_color = "white"
    text.text_size = 20



    text = Text(booking_window, text="Search Customers")
    text.text_color = "white"
    bookingCustomers_combo = Combo(booking_window, options=showAllCustomers)
    bookingCustomers_combo.text_color = "white"

    text = Text(booking_window, text="Search Destinations")
    text.text_color = "white"
    bookingDestination_combo = Combo(booking_window, options=showAllDestinations)
    bookingDestination_combo.text_color = "white"




    text = Text(booking_window, text="Number of seats required")
    text.text_color = "white"
    booking_seatNumber = TextBox(booking_window)
    booking_seatNumber.width = 2

    text = Text(booking_window, text="Notes")
    text.text_color = "white"
    text_notes = TextBox(booking_window, text="No Notes", multiline=True)
    text_notes.width = 25
    text_notes.height = 3



    booking_button = PushButton(booking_window, text="Enter", command=add_new_booking, args=[bookingCustomers_combo, bookingDestination_combo, booking_seatNumber, text_notes])
    booking_button.width = 15
    booking_button.text_color = "white"

    home_button = PushButton(booking_window, text="Home", align="bottom", command=booking_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"

def add_new_booking(bookingCustomers_combo, bookingDestination_combo, booking_seatNumber, text_notes):

    CustomerID = bookingCustomers_combo.value.split(' ', 1)[0]
    CustomerID = int(CustomerID)

    DestinationID = bookingDestination_combo.value.split(' ', 1)[1]


    SeatAmount = booking_seatNumber.value

    BookingDate = datetime.today().strftime('%d/%m/%y')
    print(BookingDate)

    Notes = text_notes.value

    cursor.execute("SELECT TripID FROM Trip INNER JOIN Destination on Destination.DestinationID = Trip.DestinationID WHERE Town =?", (DestinationID,))
    TripID = cursor.fetchall()
    TripID = [item[0] for item in TripID]
    TripID = int(TripID.pop(0))

    cursor.execute(("""INSERT INTO Booking(CustomerID, TripID, SeatAmount, BookingDate, Notes) VALUES(?, ?, ?, ?, ?)"""),(CustomerID, TripID, SeatAmount, BookingDate, Notes))
    db.commit()



    # cursor.execute("""INSERT INTO Booking(CustomerID, TripID, SeatAmount, BookingDate, Notes) VALUES(?,?,?,?,?)"""),(CustomerID, TripID, SeatAmount, BookingDate, Notes)


def new_trip():
    trip_window = Window (app, title = "New Trip", bg = (253, 71, 74), height= 600)
    picture = Picture(trip_window, image="Logo.gif")

    text = Text(trip_window, text="Book Trip")
    text.text_color = "white"
    text.text_size = 20

    text = Text(trip_window, text="Date of Trip")
    text.text_color = "white"
    trip_dateOfTrip = TextBox(trip_window)
    trip_dateOfTrip.width = 10

    text = Text(trip_window, text="Cost per Person")
    text.text_color = "white"
    trip_cost = TextBox(trip_window)
    trip_cost.width = 7

    text = Text(trip_window, text="Driver")
    text.text_color = "white"
    driver_combo = Combo(trip_window, options=["a", "b", "c", "d"])
    driver_combo.text_color = "white"

    text = Text(trip_window, text="Coach")
    text.text_color = "white"
    coach_combo = Combo(trip_window, options=["a", "b", "c", "d"])
    coach_combo.text_color = "white"

    coach_button = PushButton(trip_window, text="Enter")
    coach_button.width = 15
    coach_button.text_color = "white"

    home_button = PushButton(trip_window, text="Home", align="bottom", command=trip_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"


def new_destination():
    destination_window = Window(app, title = "Add Destination", bg = (253, 71, 74))
    picture = Picture(destination_window, image="Logo.gif")

    text = Text(destination_window, text="New Destination")
    text.text_color = "white"
    text.text_size = 20

    text = Text(destination_window, text="Name of Town")
    text.text_color = "white"
    destination_town = TextBox(destination_window)
    destination_town.width = 25

    text = Text(destination_window, text="Name of Hotel")
    text.text_color = "white"
    destination_hotel = TextBox(destination_window)
    destination_hotel.width = 25

    destination_button = PushButton(destination_window, text="Enter")
    destination_button.width = 15
    destination_button.text_color = "white"

    home_button = PushButton(destination_window, text="Home", align="bottom", command=destination_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"



def passenger_details():
    details_window = Window (app, title = "Passenger Details", bg = (253, 71, 74))
    picture = Picture(details_window, image="Logo.gif")

    text = Text(details_window, text="Passenger Details")
    text.text_color = "white"
    text.text_size = 20

    text = Text(details_window, text="Trips")
    text.text_color = "white"
    trips_combo = Combo(details_window, options=["a", "b", "c", "d"])
    trips_combo.text_color = "white"

    destination_button = PushButton(details_window, text="Enter")
    destination_button.width = 15
    destination_button.text_color = "white"

    back_button = PushButton(details_window, text="Back", align="bottom", command=details_window.destroy)
    back_button.width = 6
    back_button.text_color = "white"

def all_trips():
    trips_window = Window(app, title="All Trips", bg = (253, 71, 74), width = 500, height = 400)
    picture = Picture(trips_window, image="Logo.gif")

    text = Text(trips_window, text="All Trips")
    text.text_color = "white"
    text.text_size = 20

    ok_button = PushButton(trips_window, text="Ok", command=trips_window.destroy)
    ok_button.text_color = "white"

def customer_addresses():
    addresses_window = Window(app, title="Customer Addresses", bg = (253, 71, 74), width = 500, height = 400)
    picture = Picture(addresses_window, image="Logo.gif")

    text = Text(addresses_window, text="Customer Addresses")
    text.text_color = "white"
    text.text_size = 20

    ok_button = PushButton(addresses_window, text="Ok", command=addresses_window.destroy)
    ok_button.text_color = "white"

def trip_income():
    income_window = Window (app, title = "Passenger Details", bg = (253, 71, 74))
    picture = Picture(income_window, image="Logo.gif")

    text = Text(income_window, text="Trip Income")
    text.text_color = "white"
    text.text_size = 20

    text = Text(income_window, text="Trips")
    text.text_color = "white"
    trips_combo = Combo(income_window, options=["a", "b", "c", "d"])
    trips_combo.text_color = "white"

    income_button = PushButton(income_window, text="Enter")
    income_button.width = 15
    income_button.text_color = "white"

    back_button = PushButton(income_window, text="Back", align="bottom", command=income_window.destroy)
    back_button.width = 6
    back_button.text_color = "white"

def query_data():
    query_window = Window (app, title = "Query Data", bg = (253, 71, 74), height = 550)
    picture = Picture(query_window, image="Logo.gif")

    text = Text(query_window, text="Query Data")
    text.text_color = "white"
    text.text_size = 20

    submit = PushButton(query_window, text="Passenger Details", command=passenger_details)
    submit.text_color = "white"
    submit = PushButton(query_window, text="All Trips", command=all_trips)
    submit.text_color = "white"
    submit = PushButton(query_window, text="Customer Addresses", command=customer_addresses)
    submit.text_color = "white"
    submit = PushButton(query_window, text="Trip Income", command=passenger_details)
    submit.text_color = "white"

    home_button = PushButton(query_window, text="Home", align="bottom", command=query_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"


app = App(title='Silver Dawn Coaches', height=550, bg = (253, 71, 74))

text = Text(app, text="Silver Dawn Coaches Customer Software")
text.text_color = "white"



picture = Picture(app, image="Logo.gif")


submit = PushButton(app, text="Add Customer", command=new_customer)
submit.text_color = "white"
submit = PushButton(app, text="Book Coach", command=new_booking)
submit.text_color = "white"
submit = PushButton(app, text="Add Trip", command=new_trip)
submit.text_color = "white"
submit = PushButton(app, text="Add Destination", command=new_destination)
submit.text_color = "white"
submit = PushButton(app, text="Query Database", command=query_data)
submit.text_color = "white"

exit_button = PushButton(app, text="Exit", align="bottom", command=app.destroy)
exit_button.width = 6
exit_button.text_color = "white"
