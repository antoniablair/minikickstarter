import sqlite3 as sqlite
from utils.data import query_db

from backings.actions import *

class Backing():
    def __init__(self, name, project, card, amount):
        self.name = name
        self.project = project
        self.card = card
        self.amount = amount

    def save(self):
        qs = ('INSERT INTO Backings (name, project, card, amount) values(?,?,?,?);')
        args = (self.name, self.project, self.card, self.amount)

        query_db(qs, args, commit=True)

    def __str__(self):
        return u'{} - {}'.format(self.name, self.project)
