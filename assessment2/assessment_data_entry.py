from PyQt6.QtWidgets import * # import GUI library
import sys # import library for interfacing with operating system

app = QApplication(sys.argv) # create QT GUI application
window = QWidget() # create a window for the gui
layout = QGridLayout() # create a grid layout for the GUI

def configure_window(window_width, window_height, title): # function to configure GUI window with width and height as well as window title as arguments
    window.setLayout(layout) # make the window use the grid layout
    window.setGeometry(100, 100, window_width, window_height) # set the window size and position
    window.setWindowTitle(title) # set the window title bar title

configure_window(400, 300, "Suzy C's Science Hire Shop Inventory") # call window configuration function with parameters

equipment_name_label = QLabel("Equipment Name:") # label for equipment name
category_label = QLabel("Category:") # label for category
manufacturer_label = QLabel("Manufacturer Name:") # label for manufacturer name
year_label = QLabel("Year Manufactured:") # label for year
condition_label = QLabel("Condition:") # label for condition

equipment_entry = QLineEdit() # create entry field for equipment name
category_selection = QComboBox() # create selection box for category
category_selection.addItem("-- Select Category --") # add a default category
category_selection.addItem("Glassware") # add glassware category
category_selection.addItem("Heating Equipment") # add heating equipment category
category_selection.addItem("Measurement Equipment") # add measurement category
manufacturer_entry = QLineEdit() # add entry field for manufacturer name
year_entry = QLineEdit() # add entry field for year
condition_selection = QComboBox() # add selection box for condition
condition_selection.addItem("-- Select Condition --") # add a default condition
condition_selection.addItem("New") # add a condition for new items
condition_selection.addItem("Used but working") # add a condition for used but working items
condition_selection.addItem("Broken") # add a condition for broken items

save_button = QPushButton("Save") # add a save button

# create an error dialog function
def error_dialog(message):
    dialog = QDialog()
    dialog.setWindowTitle("Error")
    dialog_layout = QVBoxLayout()
    dialog.setLayout(dialog_layout)
    text = QLabel(message)
    dialog_layout.addWidget(text)
    dialog.exec()

# confirmation dialog subroutine
def confirm_dialog():
    # instantiate dialog box, etc.
    dialog = QDialog()
    dialog.setWindowTitle("Confirm Inventory Entry")
    dialog_layout = QGridLayout()
    dialog.setLayout(dialog_layout)
    message = "Equipment Name: {}<br>Category: {}<br>Manufacturer Name: {}<br>Year Manufactured: {}<br>Condition: {}" # use html line breaks
    # put values into string
    message = message.format(equipment_entry.text(), category_selection.currentText(), manufacturer_entry.text(), year_entry.text(), condition_selection.currentText())
    text = QLabel(message) # create label
    dialog_layout.addWidget(text, 0, 0)
    final_save_button = QPushButton("Save")
    reset_button = QPushButton("Reset")
    dialog_layout.addWidget(final_save_button, 1, 0)
    dialog_layout.addWidget(reset_button, 1, 1)

    def reset_gui(): # function to reset gui
        equipment_entry.setText("")
        category_selection.setCurrentText("-- Select Category --")
        manufacturer_entry.setText("")
        year_entry.setText("")
        condition_selection.setCurrentText("-- Select Condition --")
        dialog.close()

    def save_to_file(): # function to save all data to file
        with open("equipment.txt", "w") as file: # open file
            file.write(message.replace("<br>", "\n")) # replace html line break with normal line break
        dialog.close()

    final_save_button.clicked.connect(save_to_file) # connect button presses to function call
    reset_button.clicked.connect(reset_gui)# connect button presses to function call
    
    dialog.exec()

def save_clicked():
    # we don't have to check that the inputs for equipment name, manufacturer name, condition and category are strings since qt will always return strings
    if category_selection.currentText() == "-- Select Category --": # check something was selected
        error_dialog("Error: Invalid category option selected")
        return
    elif condition_selection.currentText() == "-- Select Condition --": # check something was selected
        error_dialog("Error: Invalid condition option selected")
        return
    elif equipment_entry.text() == "" or manufacturer_entry.text() == "" or year_entry.text() == "": # check its not empty
        error_dialog("Error: Entry field(s) left empty")
        return
    elif not year_entry.text().isdigit(): # check its a number
        error_dialog("Error: Year entered is not a number")
        return
    elif not (1800 <= int(year_entry.text()) <= 2022): # nearly all modern scientific equipment is made past the 1800's
        error_dialog("Error: Invalid year entered")
        return

    confirm_dialog() # confirmation dialog function call

save_button.clicked.connect(save_clicked) # connect button click to save_clicked subroutine

def add_widgets(): # function to add widgets to the GUI
    layout.addWidget(equipment_name_label, 0, 0)
    layout.addWidget(equipment_entry, 0, 1)
    layout.addWidget(category_label, 1, 0)
    layout.addWidget(category_selection, 1, 1)
    layout.addWidget(manufacturer_label, 2, 0)
    layout.addWidget(manufacturer_entry, 2, 1)
    layout.addWidget(year_label, 3, 0)
    layout.addWidget(year_entry, 3, 1)
    layout.addWidget(condition_label, 4, 0)
    layout.addWidget(condition_selection, 4, 1)
    layout.addWidget(save_button, 5, 0)

add_widgets() # call function to add widgets

window.show() # show the window
sys.exit(app.exec()) # run the application
