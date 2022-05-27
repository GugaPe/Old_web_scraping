import requests

page = requests.get("https://kwejk.pl")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("h2")

lista_linkow = []
lista_nazw = []

for i in results:
  lista_linkow.append(i.a['href'])
  lista_nazw.append(i.text)

listka = []

for b in range(len(lista_linkow)):
  listka.append([lista_nazw[b], lista_linkow[b]])

import sqlite3

db = sqlite3.connect("kwejk.db")

create_table = """
CREATE TABLE IF NOT EXISTS titles(
  id integer PRIMARY KEY AUTOINCREMENT,
  title text NOT NULL,
  link text NOT NULL
);
"""
cur = db.cursor()

cur.execute(create_table)

insert_sql = """
  INSERT INTO titles(title, link) VALUES(?, ?)
"""

cur.executemany(insert_sql, listka)

db.commit()

select_sql = """
  SELECT * from titles;
"""
cur.execute(select_sql)
rows = cur.fetchall()
