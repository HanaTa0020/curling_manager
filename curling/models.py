# curling/models.py

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

class League:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self, team):
        self.teams.remove(team)
