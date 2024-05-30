CREATE DATABASE voting_system
    CHARACTER SET utf8
    COLLATE utf8_general_ci;

CREATE TABLE candidate (
    name VARCHAR(50),
    surname VARCHAR(50),
    patronymic VARCHAR(50),
    occupation VARCHAR(50)
);

CREATE TABLE validator ( 
  email VARCHAR(255), 
  public_key VARCHAR(255), 
  ip_address VARCHAR(15) 
  );

CREATE TABLE vote ( 
  title VARCHAR(255), 
  start_date DATE, 
  finish_date DATE 
  );

CREATE TABLE voter (
    email VARCHAR(100),
    vote BOOL
);
