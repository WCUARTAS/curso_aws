create database db_aws

use db_aws

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(10) NOT NULL,
    birthdate DATE NOT NULL,
    gender VARCHAR(50) NOT NULL,
    photo VARCHAR(100) NOT NULL
);

INSERT INTO users
(name,phone,birthdate,gender)
VALUES("willian","3114752066","1993-11-26","male","imagen.png");

select * from users 

-- delete from users where id=12