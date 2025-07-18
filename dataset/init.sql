
create table car_specs (
    id serial primary key,
    city_mpg int,
    class varchar(30),
    combination_mpg int,
    cylinders real,
    displacement real,
    drive varchar(3),
    fuel_type varchar(15),
    highway_mpg int,
    make varchar(50),
    model varchar(50),
    transmission char(1),
    year int
);

COPY car_specs (city_mpg, class, combination_mpg, cylinders, displacement, 
                drive, fuel_type, highway_mpg, make, model, transmission, year)
FROM '/docker-entrypoint-initdb.d/car_data.csv'
DELIMITER ',' 
CSV HEADER;
