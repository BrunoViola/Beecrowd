-- Link do enunciado: https://judge.beecrowd.com/pt/problems/view/3483
SELECT subconsulta.city_name, subconsulta.population
	FROM (SELECT city_name, population
	FROM cities AS p
   ORDER BY population DESC
   LIMIT 2) AS subconsulta
   WHERE subconsulta.population <> (SELECT MAX(population) FROM cities)
UNION ALL
SELECT subconsulta.city_name, subconsulta.population
	FROM (SELECT city_name, population
	FROM cities AS p
   ORDER BY population ASC
   LIMIT 2) AS subconsulta
   WHERE subconsulta.population <> (SELECT MIN(population) FROM cities)
