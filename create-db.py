import sqlite3

# Connect to the database
conn = sqlite3.connect('census.db')
cursor = conn.cursor()

# Drop old tables if they exist
cursor.execute("DROP TABLE IF EXISTS birthrate")
cursor.execute("DROP TABLE IF EXISTS mortality")
cursor.execute("DROP TABLE IF EXISTS income")
cursor.execute("DROP TABLE IF EXISTS sexratio")

# Create tables
cursor.execute('''
    CREATE TABLE birthrate (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        year INTEGER NOT NULL,
        value REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE mortality (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        year INTEGER NOT NULL,
        value REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        year INTEGER NOT NULL,
        value REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE sexratio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        year INTEGER NOT NULL,
        value REAL NOT NULL
    )
''')

# Sample data (2015–2024)
years = list(range(2015, 2025))

# Realistic dummy values
birthrate_data = {
    "Mumbai": [14.1, 14.0, 13.8, 13.6, 13.4, 13.2, 13.1, 12.9, 12.7, 12.5],
    "Bengaluru": [15.2, 15.0, 14.8, 14.7, 14.5, 14.3, 14.2, 14.0, 13.9, 13.7],
    "Delhi": [17.3, 17.0, 16.7, 16.4, 16.2, 15.9, 15.6, 15.3, 15.1, 14.8]
}

mortality_data = {
    "Mumbai": [6.5, 6.4, 6.3, 6.2, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6],
    "Bengaluru": [6.8, 6.7, 6.6, 6.5, 6.4, 6.3, 6.2, 6.1, 6.0, 5.9],
    "Delhi": [7.0, 6.9, 6.8, 6.7, 6.6, 6.5, 6.4, 6.3, 6.2, 6.1]
}

income_data = {
    "Mumbai": [180000, 185000, 190000, 195000, 200000, 210000, 220000, 230000, 240000, 250000],
    "Bengaluru": [170000, 175000, 180000, 185000, 190000, 200000, 210000, 220000, 230000, 240000],
    "Delhi": [160000, 165000, 170000, 175000, 180000, 190000, 200000, 210000, 220000, 230000]
}

sexratio_data = {
    "Mumbai": [940, 941, 942, 943, 944, 945, 946, 947, 948, 949],
    "Bengaluru": [950, 951, 952, 953, 954, 955, 956, 957, 958, 959],
    "Delhi": [920, 921, 922, 923, 924, 925, 926, 927, 928, 929]
}

# Insert all data
for city in birthrate_data:
    for i, year in enumerate(years):
        cursor.execute("INSERT INTO birthrate (city, year, value) VALUES (?, ?, ?)", (city, year, birthrate_data[city][i]))
        cursor.execute("INSERT INTO mortality (city, year, value) VALUES (?, ?, ?)", (city, year, mortality_data[city][i]))
        cursor.execute("INSERT INTO income (city, year, value) VALUES (?, ?, ?)", (city, year, income_data[city][i]))
        cursor.execute("INSERT INTO sexratio (city, year, value) VALUES (?, ?, ?)", (city, year, sexratio_data[city][i]))

# Commit and close
conn.commit()
conn.close()

print("✅ Database created and populated with real sample data!")
