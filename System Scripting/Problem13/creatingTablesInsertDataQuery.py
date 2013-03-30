import sqlite3
#
conn = sqlite3.connect("albums.db")
#
conn.execute("PRAGMA foreign_keys = 1")
conn.execute("CREATE TABLE albums (id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist TEXT NOT NULL)")
conn.execute("CREATE TABLE tracks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, album_id INTEGER NOT NULL REFERENCES albums)")
#
conn.execute("INSERT INTO albums (name, artist) VALUES ('The Wall', 'Pink Floyd')")
conn.execute("INSERT INTO albums (name, artist) VALUES ('The Game', 'Queen')")
#
conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Is There Anybody Out There', 1)")
conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Comfortably Numb', 1)")
conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Hey You', 1)")
#
conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Play The Game', 2)")
conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Save Me', 2)")
conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Another One Bites The Dust', 2)")
#
cursor = conn.execute("INSERT INTO tracks (name, album_id) VALUES ('Another One Bites The Dust', 2)")
print "The primary key of the inserted row above is", cursor.lastrowid
#
cursor = conn.execute("SELECT tracks.name FROM albums, tracks WHERE albums.id = tracks.album_id AND albums.artist = 'Queen'")
#
data = cursor.fetchall()
#
for item in data:
   print item[0]
#
conn.commit()