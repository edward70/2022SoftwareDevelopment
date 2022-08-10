from PyQt6.QtWidgets import *
import sys, pickle

app = QApplication(sys.argv)
window = QWidget()
layout = QGridLayout()
window.setLayout(layout)
window.setGeometry(100,100,350,150)
window.setWindowTitle("Car")

make_label = QLabel("Make")
make_entry = QLineEdit()
layout.addWidget(make_label, 0, 0)
layout.addWidget(make_entry, 0, 1)

model_label = QLabel("Model")
model_entry = QLineEdit()
layout.addWidget(model_label, 0, 2)
layout.addWidget(model_entry, 0, 3)

year_label = QLabel("Year")
year_entry = QLineEdit()
layout.addWidget(year_label, 1, 0)
layout.addWidget(year_entry, 1, 1)

seats_label = QLabel("No. of seats")
seats = QComboBox()
seats.addItem("-- Select --")
seats.addItem("2")
seats.addItem("5")
seats.addItem("7")
layout.addWidget(seats_label, 2, 0)
layout.addWidget(seats, 2, 1)

towbar_label = QLabel("Towbar?")
towbar = QCheckBox()
layout.addWidget(towbar_label, 2, 2)
layout.addWidget(towbar, 2, 3)

def dprint(text):
   msgBox = QMessageBox()
   #msgBox.setIcon(QMessageBox.Information)
   msgBox.setText(text)
   msgBox.setWindowTitle("Message")
   #msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   #msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   #if returnValue == QMessageBox.Ok:
   #   print('OK clicked')

class car:
    def __init__(self, make, model, year, seats, towbar):
        if (not make == "") and (not make.isdigit()):
            print("valid make")
        else:
            dprint("invalid make")
            return
        if (not model == "") and (not model.isdigit()):
            print("valid model")
        else:
            dprint("invalid model")
            return
        if year.isdigit() and 1900 < int(year) < 2022:
            print("valid year")
        else:
            dprint("invalid year")
            return
        if seats.isdigit():
            print("valid seat number")
        else:
            dprint("invalid seat number")
            return
        if towbar:
            print("you have a towbar")
        else:
            dprint("are you sure you don't have a towbar?")
        
        self.strMake = make
        self.strModel = model
        self.intYear = int(year)
        self.intSeats = int(seats)
        self.boolTowbar = towbar
        
    def __repr__(self):
        return "{} {} {} with {} seats and {}".format(self.intYear, self.strMake, self.strModel, self.intSeats, "a towbar" if self.boolTowbar else "no towbar")

carList = []
def submit():
    new_car = car(make_entry.text(), model_entry.text(), year_entry.text(), seats.currentText(), towbar.isChecked())
    try:
       print(new_car.strMake)
    except Exception as e:
       print("invalid")
       return
    carList.append(new_car)
    for iterCar in carList:
        print(iterCar)
    pickle.dump(carList, open("car.p", "wb"))

window2 = QWidget()
layout2 = QVBoxLayout()
window2.setLayout(layout2)

def perform_search():
    results = []
    for iterCar in carList:
        if entry.text().casefold() == iterCar.strMake.casefold():
            results.append(repr(iterCar))
    if len(results) == 0:
        resultLabel.setText("No matching cars found")
        return
    resultLabel.setText("<br>".join(results))

entry = QLineEdit()
layout2.addWidget(entry)
searchButton = QPushButton("Search")
layout2.addWidget(searchButton)
searchButton.clicked.connect(perform_search)
resultLabel = QLabel("")
layout2.addWidget(resultLabel)
window2.setGeometry(100,100,300,300)
window2.setWindowTitle("Car Search")

def launch_search():
    window.hide()
    window2.show()

def close_search():
    window2.hide()
    window.show()

add = QPushButton("Add vehicle")
layout.addWidget(add, 3, 0)
add.clicked.connect(submit)

search = QPushButton("Search")
layout.addWidget(search, 3, 1)
search.clicked.connect(launch_search)

close = QPushButton("Close")
layout2.addWidget(close)
close.clicked.connect(close_search)

def quicksort(array, high=[], mid=[], low=[]):
    if len(array) == 1:
        return array
    middle_elem = array[0]
    for elem in array:
        if elem == middle_elem:
            mid.append(elem)
        elif elem < middle_elem:
            low.append(elem)
        elif elem > middle_elem:
            high.append(elem)
    return quicksort(high) + mid + quicksort(low)

try:
    carList = pickle.load(open("car.p", "rb"))
    carMap = {}
    sortList = []
    for iterCar in carList:
        print(iterCar)
        intcode = int("".join(map(lambda x: str(ord(x)), iterCar.strMake)))
        carMap[intcode] = iterCar
        sortList.append(intcode)
    carList = [carMap[x] for x in quicksort(sortList)]
    for iterCar in carList:
        print(iterCar)
except Exception as e:
    print(e)

window.show()
sys.exit(app.exec())
