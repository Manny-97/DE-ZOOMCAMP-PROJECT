SELECT name, season, country, circuit, constructor, ride_class
FROM motogp
WHERE season = (SELECT MAX(season) FROM motogp)