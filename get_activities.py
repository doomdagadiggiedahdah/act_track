import sqlite3
from datetime import datetime

# Function to fetch activities for a given date
def fetch_activities_for_date(date):
    conn = sqlite3.connect('user_activities.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, activity FROM activities
        WHERE DATE(timestamp) = ?
        ORDER BY timestamp
    ''', (date,))
    activities = cursor.fetchall()
    conn.close()
    
    if activities:
        print(f"Activities for {date}:")
        for activity in activities:
            print(f"{activity[0]}: {activity[1]}")
    else:
        print(f"No activities found for {date}.")

# Function to ask the user for a date and display activities for that date
def main():
    print("Activity Fetcher")
    date_input = input("Enter the date (YYYY-MM-DD) to fetch activities for, or press Enter for today's activities: ")
    
    # If the user presses Enter without typing a date, use today's date
    if date_input == "":
        date_input = datetime.now().strftime('%Y-%m-%d')
    
    # Validate the input format
    try:
        # This also serves as a check for today's date format
        datetime.strptime(date_input, '%Y-%m-%d')
        fetch_activities_for_date(date_input)
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format or press Enter for today's date.")

if __name__ == "__main__":
    main()
