import sys
from PyQt6.QtWidgets import *
from datetime import datetime

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello World")
window.setGeometry(100,100,350,200)
layout = QGridLayout()
window.setLayout(layout)

strListAges = ["-- Select Age --"]
with open('ages.txt', 'r') as ageFile:
    for line in ageFile:
        strListAges.append(line.replace("\n", ""))

strListEvents = ["-- Select Events --"]
with open('events.txt', 'r') as eventFile:
    for line in eventFile:
        strListEvents.append(line.replace("\n", ""))

nameLabel = QLabel("Name:")
name = QLineEdit()
ageLabel = QLabel("Age:")
age = QComboBox()
for ageOption in strListAges:
    age.addItem(ageOption)
eventLabel = QLabel("Event:")
event = QComboBox()
for eventOption in strListEvents:
    event.addItem(eventOption)

confirm = QPushButton("Confirm")
save = QPushButton("Save")

def dprint(msg):
    dialog = QDialog()
    dialog.setWindowTitle("Message")
    dlayout = QVBoxLayout()
    dialog.setLayout(dlayout)
    text = QLabel(msg)
    dlayout.addWidget(text)
    dialog.exec()

confirmationText = QLabel("")
def eventConfirm():
    confirmationText.show()
    nameValue = name.text()
    ageValue = age.currentText()
    eventValue = event.currentText()
    if ageValue == "-- Select Age --":
        dprint("no age entered")
        return
    if eventValue == "-- Select Events --":
        dprint("no event entered")
        return
    confirmationText.setText("Name: {}<br>Age: {}<br>Event: {}".format(nameValue,ageValue,eventValue))

def eventSave():
    with open('savefile.txt', 'a+') as f:
        f.write("Date: {}\n".format(datetime.today().strftime("%d/%m/%Y")))
        f.write("Name: {}\n".format(name.text()))
        f.write("Age: {}\n".format(age.currentText()))
        f.write("Event: {}\n".format(event.currentText()))
    dprint("saved successfully")

layout.addWidget(nameLabel, 0, 0)
layout.addWidget(name, 0, 1)
layout.addWidget(ageLabel, 1, 0)
layout.addWidget(age, 1, 1)
layout.addWidget(eventLabel, 2, 0)
layout.addWidget(event, 2, 1)
layout.addWidget(confirm, 3, 0)
layout.addWidget(save, 3, 1)
layout.addWidget(confirmationText, 4, 0)
confirmationText.hide()

confirm.clicked.connect(eventConfirm)
save.clicked.connect(eventSave)

window.show()
sys.exit(app.exec())
