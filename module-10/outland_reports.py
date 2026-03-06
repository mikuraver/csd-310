#Rebecca Essenburg & Daniel Fryer
#Assignment 10.1 - Milestone 3
#3/7/2026

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
 
import dotenv # to use .env file
from dotenv import dotenv_values
import os

from tabulate import tabulate

def PrintTables(title, cursor, rows):
    print(f"--{title}--")
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
        db = mysql.connector.connect(**config) # connect to the movies database
        cursor = db.cursor()

        #Report for Equipment Sales
        cursor.execute("""
                        SELECT
                            CONCAT(c.customerFName,' ', c.customerLName) AS Customer,
                            COUNT(te.tripEqId) AS "Total Purchases",
                            SUM(en.equipPrice) AS "Total Sales"
                        FROM t_tripequipmentpurchase te
                        JOIN t_booking b ON b.bookingId = te.bookingId
                        JOIN t_customers c ON c.customerId = b.customerId
                        JOIN t_equipmentnew en ON en.equipmentId = te.equipmentId
                        GROUP BY Customer
                        ORDER BY "Total Sales" DESC""")
        rows = cursor.fetchall()
        PrintTables("Customers Buying Equipment", cursor, rows)
        
        # Report for Total Equipment Purchased
        cursor.execute("""
                        SELECT 
                            e.equipName AS Item,
                            COUNT(te.equipmentId) AS "Total Items Purchased",
                            SUM(e.equipPrice) AS "Total Sales Amount"
                        FROM t_tripequipmentpurchase te
                        JOIN t_equipmentnew e 
                            ON e.equipmentId = te.equipmentId
                        GROUP BY Item
                        ORDER BY "Total Items Purchased" DESC""")
        rows = cursor.fetchall()
        PrintTables("Equipment Inventory Purchased", cursor, rows)
        
        #Report for Rentable Equipment > 5 Years Old
        cursor.execute("""
                        SELECT re.rentalId AS "Item ID",
                        re.rentalEqName AS Equipment,
                        re.rentalDatePurchase AS "Date Added to Inventory",
                        rs.rentalStatus AS "Rental Status"
                        FROM t_rentalequipment re
                        JOIN t_rentalstatus rs ON rs.rentalStatusId = re.rentalStatusId
                        WHERE rentalDatePurchase <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR)""")
        rows = cursor.fetchall()
        PrintTables("Rental Equipment > 5 Years Old",cursor, rows)

                #Report for New Equipment > 5 Years Old 
        cursor.execute("""
                        SELECT en.equipmentID AS "Item ID",
                        en.equipName AS Equipment,
                        en.equipLastDatePurchase AS "Date Added to Inventory"
                        FROM t_equipmentnew en
                        WHERE en.equipLastDatePurchase <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR)""")
        rows = cursor.fetchall()
        PrintTables("New Equipment > 5 Years Old",cursor, rows)
        
        cursor.execute("""
                        SELECT 
                            CASE
                                WHEN l.locationCountry IN ('Morocco', 'Tanzania', 'South Africa')
                                    THEN 'Africa'
                                WHEN l.locationCountry IN ('Nepal')
                                    THEN 'Asia'
                                WHEN l.locationCountry IN ('Spain')
                                    THEN 'Southern Europe'
                            END AS Region,
                            COUNT(b.bookingId) AS TotalBookings
                        FROM t_Booking b
                        JOIN t_Trip t 
                            ON t.tripId = b.tripId
                        JOIN t_TravelLocation l 
                            ON l.locationId = t.locationId
                        GROUP BY Region
                        ORDER BY TotalBookings ASC""")
        rows = cursor.fetchall()
        PrintTables("Bookings by Region", cursor, rows)
    
    
    except mysql.connector.Error as err:
        """ on error code """
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist.")
        else:
            print(err)

    finally:
        #""" close the connection to MySQL """
        db.close()
        
        
if __name__ == "__main__":
    main()
