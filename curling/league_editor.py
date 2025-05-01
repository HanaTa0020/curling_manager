# curling/league_editor.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class LeagueEditor(QWidget):
    def __init__(self, league):
        super().__init__()
        self.league = league

        self.setWindowTitle("Edit League")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Edit League Name:")
        layout.addWidget(self.label)

        self.name_input = QLineEdit()
        self.name_input.setText(self.league.name)  # Pre-fill with current name
        layout.addWidget(self.name_input)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_league)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_league(self):
        new_name = self.name_input.text()
        if new_name:
            self.league.name = new_name
            self.close()  # Close the editor window after saving
