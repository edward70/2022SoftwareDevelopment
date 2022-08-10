import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
catALabel = QLabel("Category A")
catBLabel = QLabel("Category B")

group1 = QButtonGroup()
optionOneRadio = QRadioButton("Option 1")
optionTwoRadio = QRadioButton("Option 2")
group2 = QButtonGroup()
optionThreeRadio = QRadioButton("Option 3")
optionFourRadio = QRadioButton("Option 4")

group1.addButton(optionOneRadio)
group1.addButton(optionTwoRadio)
group2.addButton(optionThreeRadio)
group2.addButton(optionFourRadio)

layout.addWidget(catALabel)
layout.addWidget(optionOneRadio)
layout.addWidget(optionTwoRadio)
layout.addWidget(catBLabel)
layout.addWidget(optionThreeRadio)
layout.addWidget(optionFourRadio)

outputLabel = QLabel("")

def submission():
    outputLabel.setText(str(group1.checkedId()))
    
submitButton = QPushButton("Submit")
layout.addWidget(submitButton)
submitButton.clicked.connect(submission)

layout.addWidget(outputLabel)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
