CREATE DATABASE data_db default CHARACTER SET UTF8;

use data_db;

CREATE TABLE User
(
    ID VARCHAR(30),
    Coin INT
);

CREATE TABLE DustData
(
    MDate DATETIME,
    ID VARCHAR(30),
    Pullution INT,
    X DOUBLE,
    y DOUBLE
);