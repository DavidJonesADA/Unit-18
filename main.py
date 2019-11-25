from guizero import *
import sqlite3


# with sqlite3.connect("Unit 18") as db:
   #cursor = db.cursor()


app = App(title='Silver Dawn Coaches', width=500, height=500, bg = (253, 71, 74))

def new_customer():
          customer_window = Window(app, title = "Add Customer", bg = (253, 71, 74), width = 500, height = 800)
          picture = Picture(customer_window, image="Logo.gif")

          text = Text(customer_window, text= "New Customer")
          text.text_color = "white"

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

          text = Text(customer_window, text= "Special Requirements?")







def new_booking():
          booking_window = Window (app, title = "Add Booking", bg = (253, 71, 74))
          picture = Picture(booking_window, image="Logo.gif")
          text = Text(booking_window, text="New Booking")
          text.text_color = "white"

def new_trip():
          trip_window = Window (app, title = "Add Trip", bg = (253, 71, 74))
          picture = Picture(app, image="Logo.gif")
          text = Text(trip_window, text="New Trip")
          text.text_color = "white"

def new_destination():
          destination_window = Window(app, title = "Add Destination", bg = (253, 71, 74))
          picture = Picture(destination_window, image="Logo.gif")
          text = Text(destination_window, text="New Destination")
          text.text_color = "white"

def query_data():
          query_window = Window (app, title = "Query Data", bg = (253, 71, 74))
          picture = Picture(query_window, image="Logo.gif")
          text = Text(query_window, text="Query Data")
          text.text_color = "white"



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




