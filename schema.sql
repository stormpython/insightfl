-- Example table schema
-- To import your schemas into your database, run:
-- `mysql -u username -p database < schema.sql`
-- where username is your MySQL username

-- Load data into table
-- LOAD DATA LOCAL INFILE 'country.csv' INTO TABLE world_index
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY ''
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES
-- (country, median_age, gdp, edu_index);

CREATE TABLE IF NOT EXISTS world_index (
  id INT NOT NULL AUTO_INCREMENT,
  country CHAR(50) NULL,
  median_age DECIMAL(3, 1) NULL,
  gdp INT NULL,
  edu_index DECIMAL(4, 3) NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;
