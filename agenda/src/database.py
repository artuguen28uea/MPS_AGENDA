import sqlite3

connection = sqlite3.connect("agenda/users.db")

cursor = connection.cursor()

# Creating tables
cursor.execute(
    """create table user (
        user_id INTEGER,
        user_name TEXT NOT NULL,
        user_password TEXT NOT NULL,
        user_email TEXT NOT NULL,
        user_status INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY (user_id)
        )""")

cursor.execute(
    """create table event (
        event_id INTEGER,
        user_id INTEGER,
        event_title TEXT NOT NULL,
        event_date TEXT NOT NULL,
        event_description TEXT,
        event_status INTEGER NOT NULL,
        PRIMARY KEY (event_id),
        FOREIGN KEY (event_id)
            REFERENCES user (user_id) 
            ON DELETE CASCADE 
            ON UPDATE NO ACTION)""")

users = [("Arthur Uguen", "12345", "audm.snf21@uea.edu.br"),
         ("Katell Uguen", "3675", "katelluguen1@gmail.com",)]

events = [(2, "Party", "10-23-3002", "Dad's house", 2),
          (1, "Meeting", "10-33-3002", "Mom's house", 1),
          (1, "Apointment", "20-23-3002", "Brother's house", 0)]

for i in range(len(users)):
  cursor.execute("insert into user (user_name, user_password, user_email) values (?, ?, ?)",
            [users[i][0], users[i][1], users[i][2]])

for i in range(len(events)):
  cursor.execute("insert into event (user_id, event_title, event_date, event_description, event_status) values (?, ?, ?, ?, ?)", 
            [events[i][0], events[i][1], events[i][2], events[i][3], events[i][4]])


connection.close()