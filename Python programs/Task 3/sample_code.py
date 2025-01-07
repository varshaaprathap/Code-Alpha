# Code with vulnerabilities 

import sqlite3

def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerability: Hardcoded SQL query
    cursor.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')")
    conn.commit()
    conn.close()

# Example of usage
create_user('admin', 'admin123')

#Code without vulnerabilities

import sqlite3
import os

def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Secure: Parameterized SQL query to avoid SQL injection
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Example of usage
create_user('admin', 'admin123')