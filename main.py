from guizero import *
import sqlite3

x= 0

# with sqlite3.connect("Unit 18") as db:
   #cursor = db.cursor()


app = App(title='Silver Dawn Coaches', width=500, height=500)

def open_splash_screen():
       splash_window = Window(app, title = "Welcome to SD Coaches")
       Text(splash_window, text="This is where you can Access the Database")


def open_modify_screen():
   modify_window = Window (app, title = "Modify the database")
   Text(modify_window, text="This is where you can Modify the Database")

text = Text(app, text="Silver Dawn Coaches Customer Software")

image = Text(app, image="Logo.png")


submit = PushButton(app, text="Add Customer", command=open_splash_screen)
submit = PushButton(app, text="Book Coach", command=open_modify_screen)
submit = PushButton(app, text="Add Trip", command=open_modify_screen)
submit = PushButton(app, text="Add Destination", command=open_modify_screen)
submit = PushButton(app, text="Query Database", command=open_modify_screen)




