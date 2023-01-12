import sqlite3
from flask import Flask, render_template, g, request


class Validation:

    def __init__(self, database):
        self.database = database

    def login_val(self, email, password):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(f'{self.database}')
            cursor = db.cursor()
        try:
            cursor.execute(
                f"""select user_id from user
                    where user_email like '{email}' and user_password like '{password}'""")
            # all_data = cursor.fetchall()
            if cursor.fetchone() != None:
                cursor.execute(
                f"""UPDATE user
                    SET user_status = 1   
                    WHERE user_email like '{email}'""")
                db.commit()
                return True
            else:
                return False

        except sqlite3.OperationalError as e:
            print(f"Erro! {e}")
            return False

    def cadastro_val(self, name, email, password, passconf):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(f'{self.database}')
            cursor = db.cursor()
            cursor.execute(
                f"""select user_id from user
                    where user_name like '{name}'""")
            if cursor.fetchone() == None:
                if(password == passconf):
                    cursor.execute(
                        f"""insert into user (user_name, user_password, user_email) 
                            values (?, ?, ?)""", [name, password, email])
                    db.commit()
                    print(f"Usuário {name} cadastrado com sucesso!")
                    return True
                else:
                    print(f"As senhas devem ser identicas!")
                    return False
            else:
                return False
