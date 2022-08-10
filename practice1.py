from PyQt6.QtWidgets import *
import sys
app = QApplication(sys.argv)

class field:
    def __init__(self, layout, label, row):
        self.label = QLabel(label)
        self.entry = QLineEdit()
        layout.addWidget(self.label,row,0)
        layout.addWidget(self.entry,row,1)

    @property
    def text(self):
        return self.entry.text()

class window(QWidget):
    def __init__(self, w, h):
        super().__init__()
        self.build_layout()
        self.add_forms()
        self.setGeometry(0,0,w,h)
        self.setWindowTitle("Data Entry")
        self.show()
        button = QPushButton("Submit")
        self.layout.addWidget(button)
        button.clicked.connect(self.submit)
        with open("players.txt") as f:
            txt = [i.split("\n") for i in f.read().split("\n\n")]
            self.names = [i[0].strip() for i in txt]
            self.abilities = sorted([int(i[1]) for i in txt])
            self.positions = [i[2].strip() for i in txt]
            print(self.names, self.abilities, self.positions)
        searchbutton = QPushButton("Search")
        updatebutton = QPushButton("Update")
        searchbutton.clicked.connect(self.search)
        updatebutton.clicked.connect(self.update)
        self.search_form()
        self.layout.addWidget(searchbutton)
        self.update_form()
        self.layout.addWidget(updatebutton)
        self.output = QLabel("")
        self.layout.addWidget(self.output)

    def search(self):
        if self.validate_ability(self.searchability.text):
            ability = int(self.searchability.text)
            lowerbound = 0
            upperbound = len(self.abilities) - 1
            found = False
            while not found:
                if upperbound < lowerbound:
                    self.output.setText("No results")
                midpoint = lowerbound + (upperbound - lowerbound) // 2
                if self.abilities[midpoint] < ability:
                    lowerbound = midpoint + 1
                elif self.abilities[midpoint] > ability:
                    upperbound = midpoint - 1
                elif self.abilities[midpoint] == ability:
                    check = ability
                    i = midpoint
                    results = []
                    while check == self.abilities[i]:
                        i = i - 1
                        results.append(i)
                    check = ability
                    i = midpoint
                    while check == self.abilities[i]:
                        i = i + 1
                        results.append(i)
                    print(results)
                    self.output.setText("Result number: {}".format(midpoint))
        else:
            self.output.setText("Invalid")

    def search_form(self):
        self.layout.addWidget(QLabel("<h3>Search player</h3>"), 5, 0)
        self.searchability = field(self.layout, "Ability:", 6)

    def update(self):
        pass

    def update_form(self):
        self.layout.addWidget(QLabel("<h3>Update player</h3>"), 8, 0)
        self.number = field(self.layout, "Search result number:", 9)
        self.updatename = field(self.layout, "Name:", 10)
        self.updateability = field(self.layout, "Ability:", 11)
        self.updateposition = field(self.layout, "Position:", 12)

    def submit(self):
        print(self.name.text, self.ability.text, self.position.text)
        if self.validate_ability(self.ability.text):
            self.names.append(self.name.text)
            self.abilities.append(int(self.ability.text))
            self.positions.append(self.position.text)
            with open("players.txt", "a") as f:
                f.write("\n\n")
                f.write(self.name.text + "\n")
                f.write(self.ability.text + "\n")
                f.write(self.position.text)
        else:
            self.output.setText("Invalid")

    def build_layout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def add_forms(self):
        self.layout.addWidget(QLabel("<h3>Save player</h3>"), 0, 0)
        self.name = field(self.layout, "Name:", 1)
        self.ability = field(self.layout, "Ability:", 2)
        self.position = field(self.layout, "Position:", 3)

    def validate_ability(self, ability):
        return ability.isdigit()
    
w = window(300,300)
sys.exit(app.exec())
