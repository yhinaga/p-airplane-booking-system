DELETE FROM airport;
DELETE FROM addr;
DELETE FROM customer;
DELETE FROM credit_card;
DELETE FROM airline;
DELETE FROM flight;
DELETE FROM booking;
DELETE FROM price;

insert into airport (airport_id, country, state_name) values ('UKP', 'Canada', 'QC');
insert into airport (airport_id, country, state_name) values ('VCC', 'Canada', 'BC');
insert into airport (airport_id, country, state_name) values ('JVV', 'Mexico', 'CHP');
insert into airport (airport_id, country, state_name) values ('JLU', 'France', 'A1');
insert into airport (airport_id, country, state_name) values ('RRL', 'Indonesia', null);

insert into customer (id, email, first_name, last_name, credit_card_number, airport_id) values ('347786204795292', 'bkeam0@quantcast.com', 'Becka', 'Keam', '4508655595023029', 'RRL');
insert into customer (id, email, first_name, last_name, credit_card_number, airport_id) values ('253099774590486', 'gjoppich1@nba.com', 'Glyn', 'Joppich', '633110126786059459', 'JLU');
insert into customer (id, email, first_name, last_name, credit_card_number, airport_id) values ('846337783837720', 'mpyne2@accuweather.com', 'Marieann', 'Pyne', '5100175923757965', 'JVV');
insert into customer (id, email, first_name, last_name, credit_card_number, airport_id) values ('015918622208307', 'agarbett3@wordpress.com', 'Aloysia', 'Garbett', '3552083082779598', 'VCC');
insert into customer (id, email, first_name, last_name, credit_card_number, airport_id) values ('704591841369337', 'csyms4@ebay.com', 'Carlie', 'Syms', '4905651261779878', 'UKP');

insert into addr (user_id, addr_id, street, city, state_name, country, postal_code) values ('347786204795292', '1', '0886 Gina Street', 'PentÃ©li', null, 'Greece', null);
insert into addr (user_id, addr_id, street, city, state_name, country, postal_code) values ('253099774590486', '3', '804 Annamark Court', 'Kertapura', null, 'Indonesia', null);
insert into addr (user_id, addr_id, street, city, state_name, country, postal_code) values ('846337783837720', '2', '2401 Sachtjen Trail', 'Naguilian', null, 'Philippines', '1116');
insert into addr (user_id, addr_id, street, city, state_name, country, postal_code) values ('015918622208307', '1', '35031 Reindahl Lane', 'Chenglin', null, 'China', null);
insert into addr (user_id, addr_id, street, city, state_name, country, postal_code) values ('704591841369337', '4', '60 Victoria Plaza', 'Agbor', null, 'Nigeria', null);

insert into credit_card (user_id, card_id, credit_card_number, street, city, state_name, country, postal_code) values ('347786204795292', '1', '4508655595023029', '0886 Gina Street', 'PentÃ©li', null, 'Greece', null);
insert into credit_card (user_id, card_id, credit_card_number, street, city, state_name, country, postal_code) values ('253099774590486', '3', '633110126786059459', '804 Annamark Court', 'Kertapura', null, 'Indonesia', null);
insert into credit_card (user_id, card_id, credit_card_number, street, city, state_name, country, postal_code) values ('846337783837720', '2', '5100175923757965', '2401 Sachtjen Trail', 'Naguilian', null, 'Philippines', '1116');
insert into credit_card (user_id, card_id, credit_card_number, street, city, state_name, country, postal_code) values ('015918622208307', '3', '4936428924158957593', '1789 Algoma Alley', 'YaguarÃ³n', null, 'Paraguay', null);
insert into credit_card (user_id, card_id, credit_card_number, street, city, state_name, country, postal_code) values ('704591841369337', '1', '5602236921584380', '1514 Susan Trail', 'Sovetskaya', null, 'Russia', '357329');

insert into airline (airline_code, airline_name, origin_country) values ('GI', 'Mosciski LLC', 'Brazil');
insert into airline (airline_code, airline_name, origin_country) values ('JJ', 'Bode', 'China');
insert into airline (airline_code, airline_name, origin_country) values ('VG', 'Macejkovic Inc', 'Russia');
insert into airline (airline_code, airline_name, origin_country) values ('JI', 'Mitchell Group', 'Philippines');
insert into airline (airline_code, airline_name, origin_country) values ('HZ', 'Raynor', 'China');

insert into flight (airlinecode, flight_number, flight_date, home_airport_id, arv_airport_id, dep_time, arv_time, first_class_capacity, economy_class_capacity) values ('GI', 'HS1781', '5/31/2019', 'UKP', 'JVV', '5:06', '4:00', '08', '832');
insert into flight (airline_code, flight_number, flight_date, home_airport_id, arv_airport_id, dep_time, arv_time, first_class_capacity, economy_class_capacity) values ('JJ', 'ZP1204', '5/6/2019', 'VCC', 'UKP', '23:52', '23:45', '15', '520');
insert into flight (airline_code, flight_number, flight_date, home_airport_id, arv_airport_id, dep_time, arv_time, first_class_capacity, economy_class_capacity) values ('VG', 'UT5309', '10/5/2019', 'JVV', 'RRL', '18:42', '5:22', '26', '231');
insert into flight (airline_code, flight_number, flight_date, home_airport_id, arv_airport_id, dep_time, arv_time, first_class_capacity, economy_class_capacity) values ('JI', 'DD5514', '2/2/2019', 'JLU', 'VCC', '11:03', '4:43', '82', '172');
insert into flight (airline_code, flight_number, flight_date, home_airport_id, arv_airport_id, dep_time, arv_time, first_class_capacity, economy_class_capacity) values ('HZ', 'TF0261', '5/22/2019', 'RRL', 'JLU', '17:26', '20:21', '92', '405');

insert into booking (user_id, flight_number, airline_code, class, credit_card_type) values ('347786204795292', 'HS1781', 'YH', 'economy', '1');
insert into booking (user_id, flight_number, airline_code, class, credit_card_type) values ('253099774590486', 'ZP1204', 'CR', 'economy', '3');
insert into booking (user_id, flight_number, airline_code, class, credit_card_type) values ('846337783837720', 'UT5309', 'LG', 'first', '2');
insert into booking (user_id, flight_number, airline_code, class, credit_card_type) values ('015918622208307', 'DD5514', 'WT', 'economy', '3');
insert into booking (user_id, flight_number, airline_code, class, credit_card_type) values ('704591841369337', 'TF0261', 'GI', 'first', '4');

insert into price (flight_number, class, price) values ('HS1781', 'first', '4684');
insert into price (flight_number, class, price) values ('ZP1204', 'first', '4704');
insert into price (flight_number, class, price) values ('UT5309', 'economy', '2552');
insert into price (flight_number, class, price) values ('DD5514', 'economy', '2479');
insert into price (flight_number, class, price) values ('TF0261', 'economy', '3696');
_
