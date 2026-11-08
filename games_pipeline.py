

import sqlite3
import requests


def init_db():
  conn = sqlite3.connect("games_database.db")
  cursor = conn.cursor()


  cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            title TEXT,
            genre TEXT,
            platform TEXT,
            publisher TEXT,
            release_date TEXT
        )
    """)

  conn.commit()
  conn.close()
  print("تم تجهيز قاعدة البيانات والجدول بنجاح! 🗄️")



def fetch_games():
  url = "https://www.freetogame.com/api/games"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  return []



def save_games_to_db(games):
  conn = sqlite3.connect("games_database.db")
  cursor = conn.cursor()


  insert_query = """
        INSERT OR REPLACE INTO games (id, title, genre, platform, publisher, release_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """


  games_to_insert = [
      (
          g.get("id"),
          g.get("title"),
          g.get("genre"),
          g.get("platform"),
          g.get("publisher"),
          g.get("release_date"),
      )
      for g in games
  ]


  cursor.executemany(insert_query, games_to_insert)

  conn.commit()
  count = cursor.rowcount
  conn.close()

  print(f"تم حفظ {count} لعبة في قاعدة البيانات بنجاح! 💾")



if __name__ == "__main__":
  init_db()  
  data = fetch_games() 
  if data:
    save_games_to_db(data) 
