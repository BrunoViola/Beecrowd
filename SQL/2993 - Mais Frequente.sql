-- Link do enunciado: https://judge.beecrowd.com/pt/problems/view/2993
SELECT amount AS "most_frequent_value"
	FROM value_table
   GROUP BY amount
   ORDER BY count(*) DESC
   LIMIT 1;