CREATE DATABASE GALLERY;
USE GALLERY;
CREATE TABLE ARTIST
	(ArtistName		CHAR(30)	NOT NULL,
    Phone			CHAR(12),
    Address			VARCHAR(30),
    Birthplace		VARCHAR(25) NOT NULL,
    ArtistAge		INT			NOT NULL,
    ArtStyle		VARCHAR(30) NOT NULL,
    PRIMARY KEY (ArtistName, ArtStyle),
    UNIQUE(ArtistName, Phone));
CREATE TABLE ART_WORK
	(ArtistName		CHAR(30) 	NOT NULL,
    ArtTitle		VARCHAR(25)	NOT NULL,
    ArtType			CHAR(30)	NOT NULL,
    DateCreated		DATE,
    DateAcquired	DATE		NOT NULL,
    Price			INT,
    ArtLocation		VARCHAR(20)	NOT NULL,
    PRIMARY KEY (ArtistName, ArtTitle),
    FOREIGN KEY (ArtistName) REFERENCES ARTIST(ArtistName));
CREATE TABLE CUSTOMER
	(CustNumber		INT			NOT NULL,
    CustPhone		CHAR(12),
    ArtPref			VARCHAR(30),
    UNIQUE (CustNumber, CustPhone));
CREATE TABLE ART_SHOW
	(ArtistName		CHAR(30)	NOT NULL,
    Date_and_Time	VARCHAR(30) NOT NULL,
    Location		CHAR(25) 	NOT NULL,
    ContactName		CHAR(30) 	NOT NULL,
    ContactPhone	CHAR(12),
    PRIMARY KEY (ArtistName),
    UNIQUE(ContactName, ContactPhone),
    FOREIGN KEY (ArtistName) REFERENCES ARTIST(ArtistName));
SELECT * FROM ARTIST;
SELECT * FROM ART_WORK;
SELECT * FROM CUSTOMER;
SELECT * FROM ART_SHOW;