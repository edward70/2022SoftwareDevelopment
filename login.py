#pyqt

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv) # application

window = QWidget() # window
layout = QGridLayout() # layout of the window
        
#to make button
loginButton = QPushButton("Login")

#labels
loginLabel = QLabel("Username:")
passwordLabel = QLabel("Password:")

#make a text field
loginEntry = QLineEdit()
passwordEntry = QLineEdit()

def authenticate():
    passwd = passwordEntry.text()
    usern = loginEntry.text()
    if usern == "edward" and passwd == "password":
        print("login successful")
    else:
        print("login failed")
        
#add the left button to the layout
layout.addWidget(loginLabel, 0, 0)
layout.addWidget(passwordLabel, 1, 0)
#add the label called msg to the layout
layout.addWidget(loginEntry, 0, 1)
layout.addWidget(passwordEntry, 1, 1)
#add the text field to the layout
layout.addWidget(loginButton, 2, 0)
#add the layout to the window
window.setLayout(layout)

#call to subroutine "greeting" when left button is clicked
loginButton.clicked.connect(authenticate)

#set the title of the window
window.setWindowTitle('Login')
#setting dimensions of the window
window.setGeometry(200, 100, 280, 80)

window.show() # show window
sys.exit(app.exec()) # run app and exit with error code
