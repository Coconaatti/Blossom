from re import L
import sqlite3,json
from typing import List,Optional


#setting up: connecting to a file and establishing a cursor to insert commands
con = sqlite3.connect('extras/notes.db')
cur = con.cursor()


# script_dir = os.path.dirname(__file__)

with open(f"extras/commands.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)

keys = list(data.keys())
keys.insert(0,".")

def showup(table,req: Optional[str]) -> List[str]:
    for x in cur.execute(f' SELECT Content,Commands FROM {table} WHERE Commands LIKE "{req}"'):
        return x

def fetch(table):
    x =  cur.execute(f'SELECT Commands FROM {table}')
    return list(x)
def add(table,cmd,content):
    cur.execute(f'INSERT INTO {table} (commands,Content) VALUES("{cmd}","{content}")')
    con.commit()

def delete(table,cmd):
    cur.execute(f"DELETE FROM {table} WHERE Commands LIKE '{cmd}'")
    con.commit()

def update(table,cmd,val):
    cur.execute(f'UPDATE {table} SET (Content) = ("{val}") WHERE Commands LIKE "{cmd}"')
    con.commit()

def tables():
    x = list(cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"))
    return x

def values():
    pass

## previously used to convert YAML / JSON files to databases. OBSOLETE..?
#for key in keys:
#    cur.execute(f'CREATE TABLE IF NOT EXISTS {key} (cid INTEGER PRIMARY KEY,Commands TEXT,Content TEXT)')
#for n in range(0,len(keys)):
#    dat = list(list(data.values())[n]['commands'])
#    val = list(list(data.values())[n]['commands'].values())
#    for x,y in zip(dat,val):
#        cur.execute(f'INSERT INTO {keys[n]} (Commands,Content) VALUES("{x}","{y}")')
