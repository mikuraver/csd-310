/*
    Rebecca Essenburg & Daniel Fryer
    Assignment 9.1
    3/1/2026
*/

-- Delete the database if it exists
DROP DATABASE IF EXISTS Outland;

-- Delete the user if it exists
DROP USER IF EXISTS 'outland_user'@'localhost';

-- Create the database
CREATE DATABASE Outland;

-- Create user and grant them all privileges to the Outland database
CREATE USER 'outland_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'adventure';

-- Grant all privileges to the Outland database to user
GRANT ALL PRIVILEGES ON Outland.* TO 'outland_user'@'localhost';
USE Outland;





-- Create the Positions table and starting data
CREATE TABLE t_Positions(
  positionId     INT           PRIMARY KEY     AUTO_INCREMENT    NOT NULL,
  positionName   VARCHAR(100)                                    NOT NULL,
  active         BIT                                             NOT NULL
);

INSERT INTO t_Positions(positionName, active)
VALUES
('Owner', 1),
('Guide', 1),
('Marketing Manager', 1),
('Supply Clerk', 1),
('Ecommerce Developer', 1),
('Manager', 1);




-- Create the Employee table and starting data
CREATE TABLE t_Employee(
  employeeId         INT           PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  employeeFName      VARCHAR(100)                                   NOT NULL,
  employeeLName      VARCHAR(100)                                   NOT NULL,
  employeePin        VARCHAR(12)                                    NOT NULL,
  positionId         INT                                            NOT NULL,
  active             BIT                                            NOT NULL,
  CONSTRAINT fk_positionId
    FOREIGN KEY(positionId)
    REFERENCES t_Positions(positionId)
);

INSERT INTO t_Employee(employeeFName, employeeLName, employeePin, positionId, active)
VALUES
('Blythe', 'Timmerson', 'AA0001', (SELECT positionId FROM t_Positions WHERE positionName = 'Owner'), 1),
('Jim', 'Ford', 'AA0002', (SELECT positionId FROM t_Positions WHERE positionName = 'Owner'), 1),
('John', 'MacNell', 'AA0003', (SELECT positionId FROM t_Positions WHERE positionName = 'Guide'), 1),
('D.B.', 'Marland', 'AA0004', (SELECT positionId FROM t_Positions WHERE positionName = 'Guide'), 1),
('Anita', 'Gallegos', 'AA0005', (SELECT positionId FROM t_Positions WHERE positionName = 'Marketing Manager'), 1),
('Dimitrios', 'Stravopolous', 'AA0006', (SELECT positionId FROM t_Positions WHERE positionName = 'Supply Clerk'), 1),
('Mei', 'Wong', 'AA0007', (SELECT positionId FROM t_Positions WHERE positionName = 'Ecommerce Developer'), 1);




-- Create Travel Location table and starting data
CREATE TABLE t_TravelLocation(
  locationId       INT           PRIMARY KEY   AUTO_INCREMENT   NOT NULL,
  locationCity     VARCHAR(100)                                 NOT NULL,
  locationCountry  VARCHAR(100)                                 NOT NULL,
  active           BIT                                          NOT NULL
);

INSERT INTO t_TravelLocation(locationCity, locationCountry, active)
VALUES
('Marrakesh', 'Morocco', 1),
('Arusha', 'Tanzania', 1),
('Cape Town', 'South Africa', 1),
('Kathmandu', 'Nepal', 1),
('Pokhara', 'Nepal', 1),
('Granada', 'Spain', 1);




-- Create Trip table and starting data
CREATE TABLE t_Trip(
  tripId                     INT        PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  locationId                 INT                                         NOT NULL,
  tripStartDate              DATETIME                                    NOT NULL,
  tripEndDate                DATETIME                                    NOT NULL,
  tripPrice                  FLOAT                                       NOT NULL,
  tripMaxNumberOfCustomers   INT                                         NOT NULL,
  active 		     BIT                                         NOT NULL,
  CONSTRAINT fk_locationId
    FOREIGN KEY(locationId)
    REFERENCES t_TravelLocation(locationId)
);

INSERT INTO t_Trip(locationId, tripStartDate, tripEndDate, tripPrice, tripMaxNumberOfCustomers, active)
VALUES
(1, '2026-07-01', '2026-07-14', 8675.33, 12, 1),
(2, '2026-06-23', '2026-07-05', 4699.12, 18, 1),
(3, '2026-08-01', '2026-08-08', 3295.00, 10, 1),
(6, '2026-09-12', '2026-09-28', 5235.21, 8, 1),
(1, '2026-10-05', '2026-10-14', 4355.78, 12, 1),
(5, '2026-12-26', '2027-07-01', 10152.25, 20, 1),
(4, '2026-08-15', '2026-08-29', 7346.25, 15, 1);




-- Create the Customers table and starting data
CREATE TABLE t_Customers(
  customerId        INT           PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  customerFName     VARCHAR(100)                                   NOT NULL,
  customerLName     VARCHAR(100)                                   NOT NULL,
  customerPhoneNum  VARCHAR(25)                                    NOT NULL,
  customerEmail     VARCHAR(300)                                   NOT NULL,
  active            BIT                                            NOT NULL
);

INSERT INTO t_Customers(customerFName, customerLName, customerPhoneNum, customerEmail, active)
VALUES
('Mark', 'Hanson', '1237418954', 'mhanson@email.com', 1),
('Jill', 'Hanson', '1237418954', 'jhanson@email.com', 1),
('Billy', 'Bob', '1559521564', 'billybob@haveemail.com', 1),
('Jimmy', 'Smith', '1559524878', 'Jimmy123@yahoo.com', 1),
('Mary', 'Johnson', '4569534561', 'johnsonm4ry@email.com', 1),
('James', 'Jamison', '7851459531', 'jj1211@hotmail.com', 1);




-- Create the Booking table and starting data
CREATE TABLE t_Booking(
  bookingId    INT    PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  tripId       INT                                     NOT NULL,
  customerId   INT                                     NOT NULL,
  employeeId   INT                                     NOT NULL,
  active       BIT                                     NOT NULL,
  CONSTRAINT fk_tripId
    FOREIGN KEY(tripId)
    REFERENCES t_Trip(tripId),
  CONSTRAINT fk_customerId
    FOREIGN KEY(customerId)
    REFERENCES t_Customers(customerId),
  CONSTRAINT fk_employeeId
    FOREIGN KEY(employeeId)
    REFERENCES t_Employee(employeeId)
);

INSERT INTO t_Booking(tripId, customerId, employeeId, active)
VALUES
(1, 1, 3, 1),
(1, 2, 3, 1),
(2, 3, 4, 1),
(3, 1, 3, 1),
(2, 5, 4, 1),
(5, 5, 3, 1);




-- Create the New Equipment table and starting data
CREATE TABLE t_EquipmentNew(
  equipmentId             INT           PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  equipName               VARCHAR(100)                                   NOT NULL,
  equipPurchasePrice      FLOAT                                          NOT NULL,
  equipPrice              FLOAT                                          NOT NULL,
  equipLastDatePurchase   DATETIME                                       NOT NULL,
  equipQtyLeft            INT                                            NOT NULL,
  active                  BIT                                            NOT NULL
);

INSERT INTO t_EquipmentNew(equipName, equipPurchasePrice, equipPrice, equipLastDatePurchase, equipQtyLeft, active)
VALUES
('2 Person Tent', 149.99, 249.99, '2026-02-01', 25, 1),
('First Aid Kit', 42.75, 125.99, '2025-12-15', 121, 1),
('North face water proof jacket', 82.75, 299.99, '2025-10-16', 31, 1),
('Camp Stove', 49.00, 175.99, '2020-11-03', 30, 1),
('Hydration Bladder', 52.00, 119.99, '2025-07-15', 25, 1),
('4 Person Tent', 190.00, 499.99, '2023-06-07', 1, 1);




-- Create the Trip Purchased Equipment table and starting data
CREATE TABLE t_TripEquipmentPurchase(
  tripEqId      INT     PRIMARY KEY    AUTO_INCREMENT   NOT NULL,
  equipmentId   INT                                     NOT NULL,
  bookingId     INT                                     NOT NULL,
  CONSTRAINT fk_equipmentId
    FOREIGN KEY(equipmentId)
    REFERENCES t_EquipmentNew(equipmentId),
  CONSTRAINT fk_bookingId
    FOREIGN KEY(bookingId)
    REFERENCES t_Booking(bookingId)
);

INSERT INTO t_TripEquipmentPurchase(equipmentId, bookingId)
VALUES
(1,1),
(2,1),
(2,3),
(4,1),
(2,2),
(2,4);




-- Create Rental Status table and starting data
CREATE TABLE t_RentalStatus(
  rentalStatusId  INT           PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  rentalStatus    VARCHAR(100)                                   NOT NULL,
  active          BIT                                            NOT NULL
);

INSERT INTO t_RentalStatus(rentalStatus, active)
VALUES
('Available', 1),
('Booked', 1),
('Checkout', 1),
('Last Use', 1),
('Lost', 1),
('Sold', 1);




-- Create the Rental Equipment table and starting data
CREATE TABLE t_RentalEquipment(
  rentalId             INT            PRIMARY KEY    AUTO_INCREMENT    NOT NULL,
  rentalEqName         VARCHAR(100)                                    NOT NULL,
  rentalDatePurchase   DATETIME                                        NOT NULL,
  rentalPrice          FLOAT                                           NOT NULL,
  rentalStatusId       INT                                             NOT NULL,
  active               BIT                                             NOT NULL,
  CONSTRAINT fk_rentalStatusId
    FOREIGN KEY(rentalStatusId)
    REFERENCES t_RentalStatus(rentalStatusId)
);

INSERT INTO t_RentalEquipment(rentalEqName, rentalDatePurchase, rentalPrice, rentalStatusId, active)
VALUES
('2 Person Tent', '2025-12-16', 35, 2, 1),
('Hydration Bladder', '2020-01-01', 10, 2, 1),
('2 Person Tent', '2025-07-15', 35, 3, 1),
('Hiking Backpack', '2025-08-17', 29, 2, 1),
('Hiking Backpack', '2025-10-07', 29, 5, 1),
('Sleeping Bag', '2020-07-07', 12.50, 4, 1);




-- Create the Trip Rental Equipment table and starting data
CREATE TABLE t_TripRental(
  tripRentalId   INT    PRIMARY KEY     AUTO_INCREMENT    NOT NULL,
  rentalId       INT                                      NOT NULL,
  bookingId      INT                                      NOT NULL,
  active         BIT                                      NOT NULL,
  CONSTRAINT fk_rentalId
    FOREIGN KEY(rentalId)
    REFERENCES t_RentalEquipment(rentalId),
  CONSTRAINT fk_RentalbookingId
    FOREIGN KEY(bookingId)
    REFERENCES t_Booking(bookingId)
);

INSERT INTO t_TripRental(rentalId, bookingId, active)
VALUES
(1,1,1),
(1,2,1),
(2,1,1),
(2,1,1),
(4,5,1),
(5,4,1);