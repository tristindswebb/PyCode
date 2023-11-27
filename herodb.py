import sqlite3
from heroes import Heroes

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE heroesdb (
          hero text,
          item text,
          skill text
)""")

hero_1 = Heroes('testhero','testitem','testskill')

c.execute("INSERT INTO heroesdb VALUES (?, ?, ?)", (hero_1.hero,hero_1.item,hero_1.skill))

conn.commit()


c.execute("SELECT * FROM heroesdb WHERE skill='testskill'")

print(c.fetchall())

conn.commit()

conn.close()