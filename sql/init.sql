/**
  * Initialization file for users, permissions and databases.
  *
  */

/* To create 2 users for MySQL*/

/* Access to MySQL from anywhere */
CREATE USER 'airbnb_user_dev'@'%'
IDENTIFIED BY '?Z4~~TwugPJN!?ND';

/* Access t MySQL from localhost */
CREATE USER 'airbnb_user_prod'@'localhost'
IDENTIFIED BY 'e3xXKwgcZ=rpP($';

/* To create databases */
CREATE DATABASE airbnb_dev
CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE DATABASE airbnb_prod
CHARACTER SET utf8 COLLATE utf8_general_ci;

/* To grant privileges */
GRANT ALL PRIVILEGES ON airbnb_dev.*
TO 'airbnb_user_dev'@'%'
IDENTIFIED BY '?Z4~~TwugPJN!?ND'
WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON airbnb_prod.*
TO 'airbnb_user_prod'@'localhost'
IDENTIFIED BY 'e3xXKwgcZ=rpP($'
WITH GRANT OPTION;


FLUSH PRIVILEGES;
