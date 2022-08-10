from PyQt6.QtWidgets import *
import sys

app = QApplication(sys.argv)

class category:
    def __init__(self, layout, cname, **kwargs):
        self.label = QLabel(cname)
        layout.addWidget(self.label)
        self.vars = list(kwargs.keys())
        self.choices = list(kwargs.values())
        self.group = QButtonGroup()
        for var in self.vars:
            setattr(self, var, QRadioButton(kwargs[var]))
            self.group.addButton(getattr(self, var))
            layout.addWidget(getattr(self, var))

    @property
    def response(self):
        return self.choices[abs(self.group.checkedId())-2]

class window(QWidget):
    def __init__(self, title, w, h):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setGeometry(100,100,w,h)
        self.setWindowTitle(title)
        self.add_form()
        button = QPushButton("Submit")
        button.clicked.connect(self.submit)
        self.layout.addWidget(button)
        self.show()

    def submit(self):
        print(self.color.response)

    def add_form(self):
        self.color = category(self.layout, "Favourite color", red="Red", green="Green", blue="Blue")

w = window("Radio button", 300, 200)
sys.exit(app.exec())