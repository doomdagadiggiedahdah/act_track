import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from tkinter import font
import sqlite3
from datetime import datetime
import schedule
import time

# Database setup function
def setup_database():
    conn = sqlite3.connect('user_activities.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            activity TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert an activity into the database
def insert_activity(activity):
    conn = sqlite3.connect('user_activities.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO activities (timestamp, activity)
        VALUES (?, ?)
    ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), activity))
    conn.commit()
    conn.close()

# Function to create and show the popup window
def show_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    style = ttk.Style()
    #style.theme_use('clam')
    #style.configure('TButton', font=('Helvetica', 12), background='blue', foreground='white')

    customFont = font.Font(family="Helvetica", size=12, weight="bold")

    label = tk.Label(root, text="Hello, Tkinter!", font=customFont)
    label.pack(pady=20)

    user_input = simpledialog.askstring("Input", "What are you up to right now?")
    if user_input:  # Only save if the user entered something
        insert_activity(user_input)
        print("Activity saved:", user_input)
    root.destroy()

# Schedule the popup window to show every 20 minutes
def run_popup():
    schedule.every(20).minutes.do(show_popup)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Ensure the database table exists
setup_database()

# Start the popup schedule
if __name__ == "__main__":
    show_popup()
    run_popup()
