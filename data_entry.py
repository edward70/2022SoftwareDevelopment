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
        self.output = QLabel("")
        self.layout.addWidget(self.output)

    def submit(self):
        print(self.name.text, self.surname.text, self.age.text, self.dob.text, self.phone.text)
        if self.validate_age(self.age.text) and self.validate_dob(self.dob.text) and self.validate_phone(self.phone.text):
            self.output.setText("Valid")
        else:
            self.output.setText("Invalid")

    def build_layout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def add_forms(self):
        self.name = field(self.layout, "Name:", 0)
        self.surname = field(self.layout, "Surname:", 1)
        self.age = field(self.layout, "Age:", 2)
        self.dob = field(self.layout, "Date of birth (dd/mm/yy):", 3)
        self.phone = field(self.layout, "Phone number:", 4)

    def validate_age(self, age):
        try:
            age = int(age)
            return True if 0 <= age <= 120 else False
        except:
            return False

    def validate_dob(self, dob):
        try:
            nums = dob.split("/")
            a = int(nums[0])
            b = int(nums[1])
            c = int(nums[2])
            if 0 <= a <= 31 and 0 <= b <= 12 and len(nums[0]) == 2 and len(nums[1]) == 2 and len(nums[2]) == 4:
                if (b in [9, 4, 5, 11] and a == 31) or (b == 2 and a > 28):
                    return False
                return True
            else:
                return False
        except:
            return False
    
    def validate_phone(self, phone):
        try:
            if len(phone) == 10 and int(phone):
                return True
            else:
                return False
        except:
            return False

w = window(300,300)
sys.exit(app.exec())