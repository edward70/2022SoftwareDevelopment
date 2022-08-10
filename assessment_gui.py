from PyQt6.QtWidgets import * # import GUI library
import sys # import library for interfacing with operating system

app = QApplication(sys.argv) # create QT GUI application
window = QWidget() # create a window for the gui
layout = QGridLayout() # create a grid layout for the GUI

def configure_window(window_width, window_height, title): # function to configure GUI window with width and height as well as window title as arguments
    window.setLayout(layout) # make the window use the grid layout
    window.setGeometry(100, 100, window_width, window_height) # set the window size and position
    window.setWindowTitle(title) # set the window title bar title

configure_window(100, 500, "Suzy C's Hire Shop GUI") # call window configuration function with parameters

main_header = QLabel("<h1>Suzy C's Hire Shop</h1>") # Create a label as a header with the <h1> html tag
greeting_text = QLabel("Welcome Edward! What would you like to hire?") # Create a label for displaying the greeting
glassware_heading = QLabel("<h2>Glassware</h2>") # Create a second sized header for glassware
heating_heading = QLabel("<h2>Heating</h2>") # Create a second sized header for heating
measuring_heading = QLabel("<h2>Measuring Equipment</h2>") # Create a second sized header for measuirng

# create all labels and fields and button groups and radio buttons
test_tube_text = QLabel("    Test tubes")
test_tube_field = QLineEdit()
beaker_text = QLabel("Beakers")
beaker_field = QLineEdit()
conical_flask_text = QLabel("Conical flasks")
conical_flask_field = QLineEdit()
bunsen_burner_text = QLabel("    Bunsen burners") # space in front to match mockup design
bunsen_burner_field = QLineEdit()
heat_gun_text = QLabel("Heat guns")
heat_gun_field = QLineEdit()
insurance_text = QLabel("Insurance?")
insurance_button_group = QButtonGroup()
insurance_yes_button = QRadioButton("Yes")
insurance_no_button = QRadioButton("No")
insurance_button_group.addButton(insurance_yes_button)
insurance_button_group.addButton(insurance_no_button)
metre_ruler_text = QLabel("    Metre rulers")
metre_ruler_field = QLineEdit()
stopwatch_text = QLabel("Stop watches")
stopwatch_field = QLineEdit()
days_hired_text = QLabel("How many days?")
days_hired_field = QLineEdit()

# create buttons and display field
submit_button = QPushButton("Submit")
selection_display = QPlainTextEdit()
hire_button = QPushButton("Hire")

def calculate_cost(): # cost calculation function
    cost = 0.0
    cost += int(test_tube_field.text())*0.5 # get integer from fields and add to cost
    cost += int(beaker_field.text())
    cost += int(conical_flask_field.text())*2
    cost += int(bunsen_burner_field.text())*5
    cost += int(heat_gun_field.text())*20
    cost += int(metre_ruler_field.text())*3.5
    cost += int(stopwatch_field.text())*4
    if insurance_button_group.checkedId() == -3: # check for yes value of insurance button
        cost += 20
    cost *= 0.9
    # check there are glassware
    if int(beaker_field.text()) > 0 or int(concial_flask_field.text()) > 0 or int(test_tube_field.text()) > 0:
        cost += 30
    return cost
    
def submit_clicked():
    # does existance, range and type checking on field values since isdigit only works on integers greater than or equal to zero that exist, also checks that a checkbox item is selected
    if not insurance_button_group.checkedId() == -1 and test_tube_field.text().isdigit() and beaker_field.text().isdigit() and conical_flask_field.text().isdigit() and bunsen_burner_field.text().isdigit() and heat_gun_field.text().isdigit() and metre_ruler_field.text().isdigit() and stopwatch_field.text().isdigit() and days_hired_field.text().isdigit():
        selection_display.setPlainText("""Name: Edward
Cost: {}""".format(calculate_cost())) # display cost
    else:
        selection_display.setPlainText("Values entered are not valid")

def hire_clicked():
    if not insurance_button_group.checkedId() == -1 and test_tube_field.text().isdigit() and beaker_field.text().isdigit() and conical_flask_field.text().isdigit() and bunsen_burner_field.text().isdigit() and heat_gun_field.text().isdigit() and metre_ruler_field.text().isdigit() and stopwatch_field.text().isdigit() and days_hired_field.text().isdigit():
        with open("save.txt", "w") as file: # write value to file
            file.write("""Name: Edward
Cost: {}""".format(calculate_cost()))
    else:
        selection_display.setPlainText("Values entered are not valid")

submit_button.clicked.connect(submit_clicked)
hire_button.clicked.connect(hire_clicked)

def add_widgets(): # function to add widgets to the GUI
    # add headings
    layout.addWidget(main_header, 0, 0) # add the label object to the GUI at row 0 column 0
    layout.addWidget(greeting_text, 1, 0) # add the label object to the GUI at row 1 column 0
    layout.addWidget(glassware_heading, 2, 0) # add the label object to the GUI at row 2 column 0
    layout.addWidget(heating_heading, 4, 0) # add the label object to the GUI at row 4 column 0
    layout.addWidget(measuring_heading, 6, 0) # add the label object to the GUI at row 7 column 0

    layout.addWidget(test_tube_text, 3, 0) # add the label object to the GUI at row 3 column 0
    layout.addWidget(test_tube_field, 3, 1)
    
    layout.addWidget(beaker_text, 3, 2) # add the label object to the GUI at row 3 column 2
    layout.addWidget(beaker_field, 3, 3)
    
    layout.addWidget(conical_flask_text, 3, 4) # add the label object to the GUI at row 3 column 4
    layout.addWidget(conical_flask_field, 3, 5)

    layout.addWidget(insurance_text, 4, 4) # add the label object to the GUI at row 4 column 4
    layout.addWidget(insurance_yes_button, 5, 4)
    layout.addWidget(insurance_no_button, 5, 5)
    
    layout.addWidget(bunsen_burner_text, 5, 0) # add the label object to the GUI at row 5 column 0
    layout.addWidget(bunsen_burner_field, 5, 1)
    
    layout.addWidget(heat_gun_text, 5, 2) # add the label object to the GUI at row 5 column 2
    layout.addWidget(heat_gun_field, 5, 3)
    
    layout.addWidget(metre_ruler_text, 7, 0) # add the label object to the GUI at row 7 column 0
    layout.addWidget(metre_ruler_field, 7, 1)
    
    layout.addWidget(stopwatch_text, 7, 2) # add the label object to the GUI at row 7 column 2
    layout.addWidget(stopwatch_field, 7, 3)
    
    layout.addWidget(days_hired_text, 8, 0) # add the label object to the GUI at row 8 column 0
    layout.addWidget(days_hired_field, 8, 1)

    layout.addWidget(submit_button, 9, 0)
    layout.addWidget(selection_display, 9, 1)
    layout.addWidget(hire_button, 9, 2)

add_widgets() # call function to add widgets

window.show() # show the window
sys.exit(app.exec()) # run the application
