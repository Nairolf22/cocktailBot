import sqlite3

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Image, InstructionGroup
from kivy.graphics.vertex_instructions import Rectangle



class Settings:
    def __init__(self):
        self.width = 1024
        self.height = 600
        self.windowFactor = 4

def calcNumCols(numRecipes):
    return int(numRecipes / 3)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class BevDatabase:
    def __init__(self, dbFile):
        self.conn = sqlite3.connect(dbFile)
        self.conn.row_factory = dict_factory

    def getAvailableBeverages(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id as id , name as name , duration as duration FROM beverages WHERE available = 1')
        return cursor.fetchall()

    def getFillLevel(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT double FROM data WHERE name = "fillLevel"')
        res = cursor.fetchone()
        return res['double']



if __name__ == '__main__':
    db = BevDatabase('beverages.db')
    print(db.getAvailableBeverages())