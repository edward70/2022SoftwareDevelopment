import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
app.setStyleSheet("QLabel,QRadioButton{color: #FAFAFA; font: 16px 'Segoe UI'; font-weight: 600;}QRadioButton{color: #8a882b;}QWidget{background-color: #973629;}")
window = QWidget()
window.setStyleSheet("background-color: #973629;")
layout = QVBoxLayout()
window.setWindowTitle("Suzy C's streaming service")

nameLabel = QLabel("<h2>Name</h2>")
nameEntry = QLineEdit()
nameEntry.setStyleSheet("background-color: #FFFFFF;")

layout.addWidget(nameLabel)
layout.addWidget(nameEntry)

catALabel = QLabel("<h2>Content</h2>")
catBLabel = QLabel("<h2>Genre</h2>")
catCLabel = QLabel("<h2>Quality</h2>")
catDLabel = QLabel("<h2>Update Regularity</h2>")

layout.addWidget(catALabel)

contentGroup = QButtonGroup()
contentRadios = ["Movies", "TV", "Interviews"]
for b in contentRadios:
    b = QRadioButton(b)
    layout.addWidget(b)
    contentGroup.addButton(b)

layout.addWidget(catBLabel)

genreGroup = QButtonGroup()
genreRadios = ["Action", "Comedy", "Drama"]
for b in genreRadios:
    b = QRadioButton(b)
    layout.addWidget(b)
    genreGroup.addButton(b)

layout.addWidget(catCLabel)

qualityGroup = QButtonGroup()
qualityRadios = ["Standard Definition", "High Definition", "4K"]
for b in qualityRadios:
    b = QRadioButton(b)
    layout.addWidget(b)
    qualityGroup.addButton(b)

layout.addWidget(catDLabel)

regularityGroup = QButtonGroup()
regularityRadios = ["Daily", "Monthly", "Weekly"]
for b in regularityRadios:
    b = QRadioButton(b)
    layout.addWidget(b)
    regularityGroup.addButton(b)

window2 = QWidget()
layout2 = QVBoxLayout()
window2.setLayout(layout2)
window2.hide()
window2.setGeometry(100,100,400,200)
nameLabel2 = QLabel("")
choiceLabel = QLabel("")
priceLabel = QLabel("")

def submission():
    flatPrices = {"Movies": 10, "TV": 8, "Interviews": 6, "Action": 2, "Comedy": 1, "Drama": 1.5}
    multipliers = {"Daily": 3, "Weekly": 1.5, "Monthly": 1, "Standard Definition": 1.5, "High Definition": 2, "4K": 3}
    name = nameEntry.text()
    content = contentRadios[abs(contentGroup.checkedId())-2]
    genre = genreRadios[abs(genreGroup.checkedId())-2]
    quality = qualityRadios[abs(qualityGroup.checkedId())-2]
    regularity = regularityRadios[abs(regularityGroup.checkedId())-2]
    finalPrice = (flatPrices[content] + flatPrices[genre]) * multipliers[quality] * multipliers[regularity]
    window.hide()
    window2.show()
    nameLabel2.setText("Name: " + name)
    choiceLabel.setText(f"Content: {content}<br>Genre: {genre}<br>Quality: {quality}<br>Regularity: {regularity}")
    priceLabel.setText(f"Monthly Cost: ${finalPrice}")
    with open("suzycdata.txt", "a") as f:
        f.write(f"{name}\n")
        f.write(f"{content},{genre},{quality},{regularity}\n")
        f.write(f"${finalPrice}\n")
    
submitButton = QPushButton("Submit")
layout.addWidget(submitButton)
submitButton.clicked.connect(submission)

layout2.addWidget(nameLabel2)
layout2.addWidget(choiceLabel)
layout2.addWidget(priceLabel)
window.setLayout(layout)
window.setGeometry(100,100,400,500)

window.show()
sys.exit(app.exec())
