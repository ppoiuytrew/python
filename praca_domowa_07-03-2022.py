# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:14:38 2022

@author: poppa
"""

import sqlite3
 
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username, password)")
connection.commit()
users={}

def get_users():
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    queryset = cursor.execute("SELECT * FROM users")
    users = queryset.fetchall()
    connection.close()
    print(users, "\n") 

def register():
    username = input("Podaj swój login: ")
    password=input("Podaj hasło: ")
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?)",(username,password))
    connection.commit()
    connection.close()
    
    
def login():
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    username=input("podaj nazwę użytkownika: ")
    password=input("podaj hasło: ")
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username, password))
    result=cursor.fetchone()
    if result:
        print("\n zalogowano!!! \n")
    else:
        print("\n podałes błędne hasło lub login \n")
    connection.close()
       
def delete():
    username=input("Podaj nazwe uzytkownika do usuniecia: ")
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE username LIKE ?",[username])
    connection.commit()
    connection.close()

def update():
    username=input("Podaj nazwę użytkownika do aktualizacji: ")
    new_username=input("Podaj nową nazwę użytkownika: ")
    new_password=input("podaj nowe hasło: ")
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET username=?, password=? WHERE username LIKE ?",[new_username, new_password, username])
    connection.commit()
    connection.close()
    
while True:
    print('1. Zarejestruj się')
    print('2. Zobacz uzytkownikow')
    print('3. Zaloguj się')
    print('4. Usuń uzytkownika')
    print('5. Zmodyfikuj uzytkownika')
    print('0. Wyjdź z programu')
    option = input('Wybierz opcję: ')
    if option == "1": 
        register()
    elif option == "2":
        get_users()      
    elif option == "3":
        login()
    elif option == "4":
        delete()
    elif option == "5":
        update()
    elif option == "0":
        break