# Rebecca Essenburg
# Assignment 6.2
# 2/15/26

# This code will pull information from the movies
# database using queries.

# Import libraries.
import mysql.connector # To connect
from mysql.connector import errorcode
 
import dotenv # To use .env file
from dotenv import dotenv_values

#Access ENV file.
secrets = dotenv_values(".env")
# Configure database.
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True # Not in ENV file.
}

# Try/Catch block for potential access errors.
try: 
    with mysql.connector.connect(**config) as db: # Connect to the movies database (with block closes automatically).
        with db.cursor() as cursor:
            print('~' * 30) # Separator line.
            print()

            # First Query: All data in Studio table.
            cursor.execute("SELECT * FROM studio")
            studio = cursor.fetchall()
            print('-- DISPLAYING Studio RECORDS --')
            for row in studio:
                print(f'Studio ID: {row[0]}')
                print(f'Studio Name: {row[1]}')
                print()
            print('~' * 30)
            print()
            
            # Second Query: All data in Genre table.
            cursor.execute("SELECT * FROM genre")
            genre = cursor.fetchall()
            print('-- DISPLAYING Genre RECORDS --')
            for row in genre:
                print(f'Genre ID: {row[0]}')
                print(f'Genre Name: {row[1]}')
                print()
            print('~' * 30)
            print()

            # Third Query: Movies less than 2 hours runtime.
            cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
            two_hours = cursor.fetchall()
            print('-- DISPLAYING Short Film RECORDS --')
            for row in two_hours:
                print(f'Film Name: {row[1]}')
                print(f'Runtime: {row[3]} minutes')
                print()
            print('~' * 30)
            print()

            # Fourth Query: Film names (grouped by director).
            cursor.execute("SELECT * FROM film ORDER BY film_director")
            films_directors = cursor.fetchall()
            print('-- DISPLAYING Director RECORDS in Order --')
            for row in films_directors:
                print(f'Film Name: {row[1]}')
                print(f'Director: {row[4]}')
                print()
            print('~' * 30)
            print()
 
# Print any error codes.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)
