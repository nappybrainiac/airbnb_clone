/**
  * Project:    AirBnB Clone
  * File:       user.py
  * By:         Mackenzie Adams, Gloria Bwandungi
  *
  * Initialization file for testers, setting their username,
  * password and privileges.
  *
  */

/* To create 2 users for MySQL*/

/* Access to MySQL from anywhere */
CREATE USER 'airbnb_user_test'@'%'
IDENTIFIED BY '?Z4~~TwugPJN!?ND';

/* To create database */
CREATE DATABASE airbnb_test
CHARACTER SET utf8 COLLATE utf8_general_ci;

/* To grant privileges */
GRANT ALL PRIVILEGES ON airbnb_test.*
TO 'airbnb_user_test'@'%'
IDENTIFIED BY '?Z4~~TwugPJN!?ND'
WITH GRANT OPTION;


FLUSH PRIVILEGES;
