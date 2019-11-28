from guizero import *
import sqlite3


# with sqlite3.connect("Unit 18") as db:
   #cursor = db.cursor()






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
    phone_number = TextBox(customer_window)
    phone_number.width = 30

    global requirements_checkbox
    global requirements_text

    requirements_checkbox = CheckBox(customer_window, text="Special Requirements?", command=tickboxes)
    requirements_checkbox.text_color = "white"

    requirements_text = TextBox(customer_window)
    requirements_text.width = 25
    requirements_text.disable()

    customer_button = PushButton(customer_window, text="Enter")
    customer_button.width = 15
    customer_button.text_color = "white"

    home_button = PushButton(customer_window, text="Home", align="bottom", command=customer_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"


def add_booking():
    booking_window = Window (app, title = "Add Booking", bg = (253, 71, 74), height = 600)
    picture = Picture(booking_window, image="Logo.gif")

    text = Text(booking_window, text="Add Booking")
    text.text_color = "white"
    text.text_size = 20



    text = Text(booking_window, text="Destination")
    text.text_color = "white"
    bookingDestination_combo = Combo(booking_window, options=["a", "b", "c", "d"])
    bookingDestination_combo.text_color = "white"


    text = Text(booking_window, text="Number of seats required")
    text.text_color = "white"
    booking_seatNumber = TextBox(booking_window)
    booking_seatNumber.width = 2

    text = Text(booking_window, text="Notes")
    text.text_color = "white"
    text_notes = TextBox(booking_window, multiline=True)
    text_notes.width = 25
    text_notes.height = 3



    booking_button = PushButton(booking_window, text="Enter")
    booking_button.width = 15
    booking_button.text_color = "white"

    home_button = PushButton(booking_window, text="Home", align="bottom", command=booking_window.destroy)
    home_button.width = 6
    home_button.text_color = "white"


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
submit = PushButton(app, text="Book Coach", command=add_booking)
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
