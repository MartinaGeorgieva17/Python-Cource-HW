CREATE TABLE testTable(
    user_name VARCHAR (50),
    user_age TINYINT UNSIGNED,
    price FLOAT UNSIGNED,
    user_comment TEXT,
    smoker ENUM('yes', 'no'), 
    PRIMARY KEY
);

-- Insert one row
INSERT INTO `testTable` VALUES('Ada', 50, 34.5, '', 'yes');

-- Insert multiple rows with specified columns
INSERT INTO `testTable` (user_name, price, user_age) VALUES 
('Pesho', 34.5, 34);

ALTER TABLE `testTable`
ADD COLUMN `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

