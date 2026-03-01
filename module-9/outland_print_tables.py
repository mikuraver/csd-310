#Rebecca Essenburg & Daniel Fryer
#Assignment 9.1
#3/1/2026

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values

import os

from tabulate import tabulate


# Create a printing function for tables.
def PrintTables(title, cursor, rows):
  print(f"-- {title} --")
  headers = [i[0] for i in cursor.description]    
  print(tabulate(rows, headers=headers, tablefmt="grid"))
  print()

def main():
  #using our .env file
  script_dir = os.path.dirname(__file__)
  env_path = os.path.join(script_dir, ".env")
  secrets = dotenv_values(env_path)

  """ database config object """
  config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
  }

  #MySQL: mysql_test.py. Connection test codetry:
  """ try/catch block for handling potential MySQL database errors """

  try:
    db = mysql.connector.connect(**config) # connect to the Outland database 

    #Print the Booking table 
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_booking")
    rows = cursor.fetchall()
    PrintTables("Booking",cursor, rows)

    #Print the Customers table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_customers")
    rows = cursor.fetchall()
    PrintTables("Customers",cursor, rows)

    #Print the Employee table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_employee")
    rows = cursor.fetchall()
    PrintTables("Employee",cursor, rows)

    #Print the EquipmentNew table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_equipmentnew")
    rows = cursor.fetchall()
    PrintTables("EquipmentNew",cursor, rows)

    #Print the Positions table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_positions")
    rows = cursor.fetchall()
    PrintTables("Positions",cursor, rows)

    #Print the RentalEquipment table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_rentalequipment")
    rows = cursor.fetchall()
    PrintTables("RentalEquipment",cursor, rows)

    #Print the RentalStatus table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_rentalstatus")
    rows = cursor.fetchall()
    PrintTables("RentalStatus",cursor, rows)

    #Print the TravelLocation table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_travellocation")
    rows = cursor.fetchall()
    PrintTables("TravelLocation",cursor, rows)

    #Print the Trip table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_trip")
    rows = cursor.fetchall()
    PrintTables("Trip",cursor, rows)

    #Print the TripEquipmentPurchase table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_tripequipmentpurchase")
    rows = cursor.fetchall()
    PrintTables("Trip Equipment Purchase",cursor, rows)

    #Print the TripRental table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM t_triprental")
    rows = cursor.fetchall()
    PrintTables("Trip Rental",cursor, rows)

  except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("The specified database does not exist.")

    else:
      print(err)

  finally:
    """ close the connection to MySQL """
    db.close()

if __name__ == "__main__":
  main()