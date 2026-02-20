# Rebecca Essenburg
# Assignment 7.2
# 2/22/26

# This code will update information in the
# movies database using queries.

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

# Create function to join tables iterate over info then output results.
def show_films(cursor,title):
    # Inner join query
    cursor.execute("SELECT film_name AS Name, film_director AS Director, \
                    genre_name AS genre, studio_name AS 'Studio Name' from film INNER JOIN \
                    genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id \
                    ORDER BY film_id")
        
    # Get the results from the cursor object
    films = cursor.fetchall()

    # Display results individually.
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n"
              .format(film[0], film[1], film[2], film[3]))
             
# Define main function with a try/except block for errors.
def main():
    try: 
        with mysql.connector.connect(**config) as db: # Connect to the movies database (with block closes automatically).
            with db.cursor() as cursor:
                # Display films currently in database.
                show_films(cursor,"DISPLAYING FILMS")

                # Add new record into the film table.
                sql = "INSERT INTO film (film_name, film_releaseDate, film_runtime, \
                        film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)"
                val = ('Halloween', '2018', '106', 'David Gordon Green', '2', '1')
                cursor.execute(sql, val)
                show_films(cursor,"DISPLAYING FILMS AFTER INSERT") # Display changes.

                # Update Alien to be a horror film.
                sql = "UPDATE film SET genre_id=%s WHERE film_id=%s"
                val = ('1', '2')
                cursor.execute(sql, val)
                show_films(cursor,"DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror") #Display changes.

                # Delete the movie Gladiator.
                sql = "DELETE from film WHERE film_id=%s"
                val = ('1',)
                cursor.execute(sql, val)
                show_films(cursor,"DISPLAYING FILMS AFTER DELETE") #Display changes.

                # Commit all changes to the database.
                db.commit()

    # Print error codes for database connection.
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist.")
        else:
            print(err)

# Execute the main function.
if __name__ == '__main__':
     main()