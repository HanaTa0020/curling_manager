from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class TeamEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team Editor")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        label = QLabel("This is the Team Editor window.")
        layout.addWidget(label)

        self.setLayout(layout)
