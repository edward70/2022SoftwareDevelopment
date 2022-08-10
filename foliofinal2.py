from PyQt6.QtWidgets import * # import pyqt for gui
import sys # import sys for system api calls
app = QApplication(sys.argv) # pass cli arguments to qt

class field: # field class for a generic label + lineedit template
    def __init__(self, layout, label, row): # initialization function
        self.label = QLabel(label) # create label
        self.entry = QLineEdit() # create entry field
        layout.addWidget(self.label,row,0) # add label to layout
        layout.addWidget(self.entry,row,1) # add entry to layout next to label

    @property # property decorator for easy use
    def text(self): # text property
        return self.entry.text() # get text entered

class window(QWidget): # window class extending qwidget to create a new gui window
    def __init__(self, w, h): # initialize with width and height of window
        super().__init__() # call QWidget initialization
        self.build_layout() # build the layout
        self.setGeometry(0,0,w,h) # set window size
        self.setWindowTitle("Suzy C's Science Equipment") # window title set
        self.show() # show the window
        with open("inventory.txt") as f: # open the inventory file
            txt = list(filter(lambda x: x != "", f.read().split("\n"))) # read file, split by newlines, filter out empty lines
            #print(txt) 
            self.names = txt[0::3] # every third element offset by 0 is a name, make this a list
            self.conditions = list(map(int, txt[1::3])) # offset by 1 is a condition, convert all to int
            self.manufacturers = txt[2::3] # offset by two is a manufacturer
            #print(self.names, self.conditions, self.manufacturers)
        searchbutton = QPushButton("Search") # create search button
        updatebutton = QPushButton("Update") # create update button
        searchbutton.clicked.connect(self.search) # connect button to search function
        updatebutton.clicked.connect(self.update) # connect to update function
        self.search_form() # add search form
        self.layout.addWidget(searchbutton) # add button to layout
        self.update_form() # add update form
        self.layout.addWidget(updatebutton) # add update button to layout
        self.output = QLabel("") # empty label for output data
        self.layout.addWidget(self.output,10,0) # add to the bottom of screen

    def search(self): # function to search for equipment
        query = self.searchname.text.lower() # make query case insensitive
        texts = ["<h3>Search Results</h3><br>"] # have the first line be some title text with <h3>
        for i,element in enumerate(self.names): # loop through all names counting positions
            if element.lower() == query: # check if the element matches search, case insensitive
                # store position, name, condition, manufacturer in local variable
                pos = i
                name = element
                condition = self.conditions[i]
                manufacturer = self.manufacturers[i]
                # add formatted text to text list using <br> for line breaks
                texts.append("Position: {}<br>Name: {}<br>Conditon: {}<br>Manufacturer: {}<br><br>".format(pos,name,condition,manufacturer))
        if len(texts) > 1: # check that there were search results
            self.output.setText("".join(texts)) # display search results
        else:
            self.output.setText("<h3>Search Results</h3><br>Nothing found") # show that nothing was found

    def search_form(self): # add search form to gui
        self.layout.addWidget(QLabel("<h3>Search Equipment</h3>"), 1, 0) # add title
        self.searchname = field(self.layout, "Equipment name:", 2) # add equipment name field

    def update(self): # update function
        if self.number.text.isdigit() and int(self.number.text) <= len(self.names): # input validate position is integer, within bounds of data
            number = int(self.number.text) # convert to int for array indexing
            if self.updatecondition.text.isdigit(): # check the condition is an integer
                self.names[number] = self.updatename.text # change name at pos
                self.conditions[number] = int(self.updatecondition.text) # change condition to new integer
                self.manufacturers[number] = self.updatemanufacturer.text # change manufacturer
                with open("inventory.txt", "w") as f: # open inventory to write
                    # format data as a single newline delimited text string using zip to join data
                    txt = "\n\n".join(["{}\n{}\n{}".format(e[0], e[1], e[2]) for e in zip(self.names, self.conditions, self.manufacturers)])
                    f.write(txt) # save to file
                self.output.setText("Equipment info updated successfully") # success message
            else:
                self.output.setText("Error: Condition must be a number") # input validation failure case
        else:
            self.output.setText("Invalid position to update!") # invalid position case

    def update_form(self): # function to add the update form to the gui
        self.layout.addWidget(QLabel("<h3>Update Equipment</h3>"), 4, 0) # add the title
        self.number = field(self.layout, "Position number:", 5) # add a field to enter the position number in the data structure
        self.updatename = field(self.layout, "Name:", 6) # add a field to enter the new name
        self.updatecondition = field(self.layout, "Condition:", 7) # new condition field
        self.updatemanufacturer = field(self.layout, "Manufacturer:", 8) # new manufacturer field

    def build_layout(self): # build layout of window
        self.layout = QGridLayout() # create grid layout
        self.setLayout(self.layout) # set the layout to the current window
    
w = window(300,300) # 300x300 window
sys.exit(app.exec()) # properly execute and terminate gui
