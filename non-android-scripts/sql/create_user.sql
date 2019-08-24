CREATE TABLE sail_user.T_EMPLOYEE (
E_id VARCHAR(16) NOT NULL,
Passwd VARCHAR(255) NOT NULL,
Email VARCHAR(255) NOT NULL,
Unit VARCHAR(16) NOT NULL,
Desig VARCHAR(16) NOT NULL,
Mobile VARCHAR(16) NOT NULL,
Created DATETIME DEFAULT CURRENT_TIMESTAMP
PRIMARY KEY (E_Id)
);

CREATE USER 'php_user'@'localhost' IDENTIFIED BY 'random_pass';
GRANT SELECT, INSERT ON sail_user.* TO 'php_user'@'localhost';
