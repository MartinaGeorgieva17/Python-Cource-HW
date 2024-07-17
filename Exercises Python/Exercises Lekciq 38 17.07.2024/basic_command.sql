-- Create table `testTable`
CREATE TABLE testTable (
    user_name VARCHAR(50),
    user_age TINYINT UNSIGNED,
    price FLOAT UNSIGNED,
    user_comment TEXT,
    smoker ENUM('yes', 'no'),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_name)  -- Assuming user_name is intended as primary key
);

-- Insert one row
INSERT INTO testTable (user_name, user_age, price, user_comment, smoker)
VALUES ('Ada', 50, 34.5, '', 'yes');

-- Insert multiple rows with specified columns
INSERT INTO testTable (user_name, price, user_age)
VALUES ('Pesho', 34.5, 34);

-- Alter table `testTable` to add `created_at` column
ALTER TABLE testTable
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

