from painter import paint
import sqlite3 as sqlite
import sys
from utils.data import query_db

class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.currently_raised = 0

    def update(self, new_currently_raised):
        qs = ('UPDATE Projects SET currently_raised=? WHERE name=?')
        args = (new_currently_raised, self.name)

        query_db(qs, args=args, commit=True)

    def save(self):
        qs = ('INSERT INTO Projects (name, target, currently_raised) VALUES (?, ?, ?)')
        args = (self.name, self.target, self.currently_raised)
        query_db(qs, args=args, commit=True)

    def __str__(self):
        return self.name
