-- DROP TABLE IF EXISTS guvi.bus_routes;

CREATE TABLE guvi.bus_routes (
id INT AUTO_INCREMENT PRIMARY KEY,
state TEXT,
route_name TEXT,
route_link TEXT,
busname TEXT,
bustype TEXT,
departing_time TIME,
duration TEXT,
reaching_time TIME,
star_rating FLOAT,
price DECIMAL,
seats_available INT);

SELECT * FROM guvi.bus_routes;

SELECT MIN(price), MAX(price) FROM guvi.bus_routes;

SELECT MIN(seats_available), MAX(seats_available) FROM guvi.bus_routes;

SELECT distinct star_rating FROM guvi.bus_routes;
SELECT MIN(star_rating), MAX(star_rating) FROM guvi.bus_routes;

SELECT distinct bustype FROM guvi.bus_routes;

SELECT busname FROM guvi.bus_routes WHERE (route_name="Goa to Pune") and (star_rating > 4) and (price <3000);