import sqlite3

from kivy.clock import Clock

def fill(dt):
    conn = sqlite3.connect("beverages.db")
    cursor = conn.cursor()
    res = cursor.execute('SELECT double FROM data WHERE name = "fillLevel"')
    fillLevel = res.fetchone()[0]
    if(fillLevel < 1):
        fillLevel = fillLevel + 0.02
        fillLeveldata = (fillLevel, )
        cursor.execute('UPDATE data SET double = ? WHERE name = "fillLevel"', fillLeveldata)
        conn.commit()

if __name__ == '__main__':
    Clock.schedule_interval(fill, 0.2)
