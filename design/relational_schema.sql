/*Relational schema (sql script version) for cs425 project*/
CREATE TABLE airport
(
	airport_id CHAR(3),/*IATA location id*/
	country VARCHAR(10),
	state_name VARCHAR(10),/*only for US and Canada*/
	PRIMARY KEY(airport_id)
);

CREATE TABLE customer
(
	id NUMERIC(15),
	email VARCHAR(50),
	password VARCHAR(50),
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	credit_card_number NUMERIC(20),
	airport_id CHAR(3),/*home_airport*/
	PRIMARY KEY(id)
);

CREATE TABLE addr
(
	user_id NUMERIC(15),
	addr_id NUMERIC(5),
	street VARCHAR(30),
	city VARCHAR(20),
	state_name VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(10),
	PRIMARY KEY(user_id, addr_id),
	FOREIGN KEY(user_id) REFERENCES customer(id)
);

CREATE TABLE credit
(
	user_id NUMERIC(15),
	card_id NUMERIC(3),/* numbering credit cards*/
	credit_card_number NUMERIC(20),
	street VARCHAR(30),
	city VARCHAR(20),
	state_name VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(10),
	PRIMARY KEY(user_id, card_id),
	FOREIGN KEY(user_id) REFERENCES customer(id)
);

CREATE TABLE airline
(
	airline_code CHAR(2),
	airline_name VARCHAR(20),
	origin_country VARCHAR(20),
	PRIMARY KEY(airline_code)
);

CREATE TABLE flight
(
	airline_code CHAR(2),
	flight_number VARCHAR(10),/*primary key,*/
	flight_date VARCHAR(15),/*primary key, format dd/mm/yyyy */
	home_airport_id CHAR(3),/*IATA id*/
	arv_airport_id CHAR(3),
	dep_time VARCHAR(20),
	arv_time VARCHAR(20),
	first_class_capacity NUMERIC(3, 0),
	economy_class_capacity NUMERIC(3, 0),
	PRIMARY KEY(flight_number),/*airline_code*/
	FOREIGN KEY(airline_code) REFERENCES airline(airline_code),
	FOREIGN KEY(home_airport_id) REFERENCES airport(airport_id),
	FOREIGN KEY(arv_airport_id) REFERENCES airport(airport_id)
);

CREATE TABLE booking /*flight booking is for a particular customer, possibly for multiple flights*/
(
	user_id NUMERIC(15),
	flight_number VARCHAR(10),
	airline_code VARCHARef(10),
	class VARCHAR(10),/*first or economy*/
	credit_card_type NUMERIC(2, 0),
	PRIMARY KEY(user_id, flight_number),/*credit_card_type*/
	FOREIGN KEY(user_id) REFERENCES customer(id),
	FOREIGN KEY(flight_number) REFERENCES flight(flight_number)
);

CREATE TABLE price
(
	flight_number VARCHAR(10),
	class VARCHAR(10),/*first or economy*/
	price NUMERIC(6),
	PRIMARY KEY(flight_number, class),/*flight_number*/
	FOREIGN KEY(flight_number) REFERENCES flight(flight_number)
); 

