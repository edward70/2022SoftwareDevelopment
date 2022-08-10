import sys # library to interface with operating system
from PyQt6.QtWidgets import * # gui library

app = QApplication(sys.argv) # create application

window = QWidget() # create window
layout = QGridLayout() # create layout of the window
        
# make login button
login_button = QPushButton("Login")

# make labels for username and password
login_label = QLabel("Username:")
password_label = QLabel("Password:")

#make a text field for username and password
login_entry = QLineEdit()
password_entry = QLineEdit()

# keep track of failed attempts
login_fail_count = 0

# open usernames file
with open("usernames.txt", "r") as usernames_file:
    usernames = usernames_file.readlines() # read all usernames
    logins = {} # keep logins in a dictionary for constant time lookup
    with open("passwords.txt", "r") as passwords_file: # open passwords file
        passwords = passwords_file.readlines() # read all passwords
        for i, username in enumerate(usernames): # loop through usernames
            logins[username.replace("\n", "")] = passwords[i].replace("\n", "") # set username and password values in dictionary while removing newlines

# create a login dialog
def authentication_dialog(message):
    dialog = QDialog()
    dialog.setWindowTitle("Authentication") # set window title
    dialog_layout = QVBoxLayout()
    dialog.setLayout(dialog_layout)
    text = QLabel(message)
    dialog_layout.addWidget(text)
    dialog.exec()

# function to authenticate username and password
def authenticate():
    global login_fail_count # use global variable for fail attempts
    passwd = password_entry.text() # get password text
    usern = login_entry.text() # get username text
    # we don't have to check if the username and password are strings because qt will always return strings
    if usern == "" or passwd == "": # check there was text entered
        login_fail_count += 1 # increment failure
        authentication_dialog("Username or password not entered") # error message
    elif logins.get(usern) == passwd: # test if username password combo works
        authentication_dialog("Login successful") # display success
    else: # otherwise it failed
        login_fail_count += 1 # increment failure
        if login_fail_count == 3: 
            sys.exit() # close when there are 3 fails
        else:
            authentication_dialog("Login failed") # otherwise display a failure message
        
# add labels
layout.addWidget(login_label, 0, 0)
layout.addWidget(password_label, 1, 0)
# add login fields
layout.addWidget(login_entry, 0, 1)
layout.addWidget(password_entry, 1, 1)
# add login button
layout.addWidget(login_button, 2, 0)
#add the layout to the window
window.setLayout(layout)

#call to subroutine "authenticate" when left button is clicked
login_button.clicked.connect(authenticate)

#set the title of the window
window.setWindowTitle("Login to Suzy C's Science Hire Shop Inventory")
#setting dimensions of the window
window.setGeometry(200, 100, 280, 80)

window.show() # show window
sys.exit(app.exec()) # run app and exit with error code
