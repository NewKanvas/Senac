-- Create a Database
CREATE DATABASE Elefante;
USE Elefante;

-- ############################################################################################
-- ## Criar Adcionar Tabelas
-- ############################################################################################

-- Create a Table for People
CREATE TABLE Person (
    personID INT NOT NULL PRIMARY KEY IDENTITY(1,1), --AUTO_INCREMENT
    cpf VARCHAR NOT NULL,
    name VARCHAR(20) NOT NULL,
    Age INT NOT NULL
);

-- Insert data into the Person table
INSERT INTO Person VALUES ('123456789', 'John Doe', 25);

-- Create a Table for Pizza
CREATE TABLE Pizza (
    pizzaID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50) NOT NULL, 
    description VARCHAR(100) NOT NULL, 
    category VARCHAR(50) NOT NULL, 
    deliveryType VARCHAR(50) NOT NULL, 
    price FLOAT NOT NULL
);

-- Insert data into the Pizza table
INSERT INTO Pizza (name, description, category, deliveryType, price) 
VALUES 
    ('Pepperoni', 'Classic Pepperoni Pizza', 'Classic', 'Store Pickup', 20.99),
    ('FourCheese', 'Four Cheese Pizza', 'Classic', 'Specials', 10.99),
    ('RomeoAndJuliet', 'Romeo and Juliet Pizza', 'Specialty', 'Specials', 54.99);

-- ############################################################################################
-- ## Selecionar
-- ############################################################################################

-- Select all data from the Person table
SELECT * FROM Person;

-- Display all records from Pizza table
SELECT * FROM Pizza;

-- Select specific columns from the Person table with an alias
SELECT name AS Test FROM Person;

-- Select specific columns from the Person table ordered by name
SELECT name, cpf FROM Person ORDER BY name;

-- Select records from the table where the entity is 'John'
SELECT entity FROM Table WHERE entity = 'John';


-- Select records with a specific category using subquery
SELECT * FROM Pizza WHERE category IN (SELECT category FROM Pizza WHERE category = 'Specials');

-- ############################################################################################
-- ############################################################################################

-- Select records where the name contains 'piry'
SELECT * FROM Pizza WHERE name LIKE '%piry';

-- Select records where the name contains 'com'
SELECT * FROM Pizza WHERE name LIKE '%com%';

-- Select records where the name has 'a' as the second letter
SELECT * FROM Pizza WHERE name LIKE '_a%';

-- Select records from Person where the name starts with 'J'
SELECT * FROM Person WHERE Name LIKE 'J%';

-- Select records from Person where the name ends with 'J'
SELECT * FROM Person WHERE Name LIKE '%J';

-- Pizza records from Person by name
SELECT * FROM Person Pizza BY name;


-- ############################################################################################
-- ## Maximo ~ Minimo ... Números
-- ############################################################################################

-- Select records with a specific category and price values
SELECT * FROM Pizza WHERE category = 'Specials' AND price IN (40, 55);

-- Select records with specific conditions
SELECT price, deliveryType FROM Pizza WHERE price <> 35 AND deliveryType = 'Store Pickup';

-- Select records from Person and Pizza tables with an inner join
SELECT * FROM Person INNER JOIN Pizza ON Person.personID = Pizza.personID WHERE price IN (45, 95, 120);

-- Select specific columns from Person and Pizza tables with an inner join
SELECT name, price FROM Person INNER JOIN Pizza ON Person.personID = Pizza.personID WHERE price IN (45, 95, 120);

-- Select records with a price between 50 and 55
SELECT * FROM Pizza WHERE price BETWEEN 50 AND 55;

-- Select records where price is greater than or equal to 10
SELECT price, deliveryType FROM Pizza WHERE price >= 10;

-- Select records where price is not equal to 25.5
SELECT price, deliveryType FROM Pizza WHERE price <> 25.5;


-- Select the maximum price from Pizza table
SELECT MAX(price) FROM Pizza;

-- Select the minimum price from Pizza table
SELECT MIN(price) FROM Pizza;

-- Count the number of records with price greater than 60
SELECT COUNT(price) FROM Pizza WHERE price > 60;

-- Sum of all prices in Pizza table
SELECT SUM(price) FROM Pizza;

-- Sum of prices in Pizza table where price is greater than 100
SELECT SUM(price) FROM Pizza WHERE price > 100;

-- Count records for each category in Pizza table with more than 4 entries
SELECT category, COUNT(*) FROM Pizza GROUP BY category HAVING COUNT(*) > 4;

-- ############################################################################################
-- ## Update / Delete
-- ############################################################################################

-- Update category values in Pizza table
UPDATE Pizza SET category = 'Non-Dairy' WHERE category = 'Dairy-Free';

-- Update category values in Pizza table with a limit
UPDATE Pizza SET category = 'Dairy-Free' WHERE category = 'Non-Dairy' LIMIT 4;

-- Delete the Person table
DROP TABLE Person;

-- Delete all data from the Person table
TRUNCATE TABLE Person;

-- Delete specific data from the Person table
DELETE FROM Person WHERE Name = 'John';

-- Alter the Person table to change the column name
ALTER TABLE Person CHANGE COLUMN Name FirstName VARCHAR(20) NOT NULL;

-- Update category values in Pizza table
UPDATE Pizza SET category = 'Lactose-Free' WHERE category = 'Zero Lactose';

-- Update category values in Pizza table with a limit
UPDATE Pizza SET category = 'Zero Lactose' WHERE category = 'Lactose-Free' LIMIT 4;


