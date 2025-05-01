# curling/main_window.py

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QListWidget, QVBoxLayout,
    QHBoxLayout, QFileDialog, QMessageBox, QInputDialog
)
from .league_editor import LeagueEditor
from .models import League, Team, Member


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curling League Manager")

        self.leagues = []

        # Main Widget and Layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # League List
        self.league_list = QListWidget()
        self.layout.addWidget(self.league_list)

        # Buttons
        button_layout = QHBoxLayout()
        self.layout.addLayout(button_layout)

        self.add_league_button = QPushButton("Add League")
        self.edit_league_button = QPushButton("Edit League")
        self.delete_league_button = QPushButton("Delete League")

        button_layout.addWidget(self.add_league_button)
        button_layout.addWidget(self.edit_league_button)
        button_layout.addWidget(self.delete_league_button)

        # Connect buttons
        self.add_league_button.clicked.connect(self.add_league)
        self.edit_league_button.clicked.connect(self.edit_league)
        self.delete_league_button.clicked.connect(self.delete_league)

    def add_league(self):
        name, ok = QInputDialog.getText(self, "Add League", "League name:")
        if ok and name:
            league = League(name)
            self.leagues.append(league)
            self.update_league_list()

    def edit_league(self):
        selected_items = self.league_list.selectedItems()
        if selected_items:
            item = selected_items[0]
            index = self.league_list.row(item)
            league = self.leagues[index]

            editor = LeagueEditor(league)
            editor.setWindowModality(True)  # Block main window until done
            editor.show()
            editor.destroyed.connect(self.update_league_list)  # Refresh list after closing

    def delete_league(self):
        selected_items = self.league_list.selectedItems()
        if selected_items:
            item = selected_items[0]
            index = self.league_list.row(item)
            del self.leagues[index]
            self.update_league_list()

    def update_league_list(self):
        self.league_list.clear()
        for league in self.leagues:
            self.league_list.addItem(league.name)
