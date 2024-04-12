import sqlite3
import random


conn = sqlite3.connect('casino.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, login TEXT, password TEXT, cash REAL)''')


conn.commit()
conn.close()


def register_user(login, password):
    conn = sqlite3.connect('casino.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (login, password, cash) VALUES (?, ?, ?)", (login, password, 100))
    conn.commit()
    conn.close()


def check_login(login):
    conn = sqlite3.connect('casino.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE login=?", (login,))
    result = c.fetchone()
    conn.close()
    return result


def start_game(login):
    conn = sqlite3.connect('casino.db')
    c = conn.cursor()
    c.execute("SELECT cash FROM users WHERE login=?", (login,))
    cash = c.fetchone()[0]
    if cash < 10:
        conn.close()
        return "Not enough balance to start the game."
    else:
        number = random.randint(1, 10)
        if number % 2 == 0:  
            new_cash = cash + 10
            message = "You won! $10 added to your balance."
        else:  
            new_cash = cash - 5
            message = "You lost! $5 deducted from your balance."
        c.execute("UPDATE users SET cash=? WHERE login=?", (new_cash, login))
        conn.commit()
        conn.close()
        return message


def delete_user(login):
    conn = sqlite3.connect('casino.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE login=?", (login,))
    conn.commit()
    conn.close()


def check_balance(login):
    conn = sqlite3.connect('casino.db')
    c = conn.cursor()
    c.execute("SELECT cash FROM users WHERE login=?", (login,))
    balance = c.fetchone()[0]
    conn.close()
    return balance


while True:
    print("Secim edin:")
    print("(1) Qeydiyyatdan kecin")
    print("(2) Oyuna basla")
    print("(3) İstifadəçini bazadan silin")
    print("(4) Balansi yoxla")
    print("(5) Cixish")

    choice = input()

    if choice == "1":
        login = input("Logini daxil edin: ")
        password = input("Şifrəni daxil edin: ")
        if check_login(login):
            print("Bu login artıq mövcuddur. Zəhmət olmasa, başqa login seçin.")
        else:
            register_user(login, password)
            print("Qeydiyyat uğurla başa çatdı.")
    
    elif choice == "2":
        login = input("Logini daxil edin: ")
        if not check_login(login):
            print("Belə bir istifadəçi mövcud deyil.")
        else:
            print(start_game(login))
    
    elif choice == "3":
        login = input("Silmək istədiyiniz istifadəçinin loginini daxil edin: ")
        if not check_login(login):
            print("Belə bir istifadəçi mövcud deyil.")
        else:
            delete_user(login)
            print("İstifadəçi uğurla silindi.")
    
    elif choice == "4":
        login = input("Logini daxil edin: ")
        if not check_login(login):
            print("Belə bir istifadəçi mövcud deyil.")
        else:
            print("Balansınız:", check_balance(login))
    
    elif choice == "5":
        print("Çıxılır...")
        break
    
    else:
        print("Yanlış seçim. Zəhmət olmasa, düzgün seçim edin.")
