-- Link do enunciado: https://judge.beecrowd.com/pt/problems/view/2995
SELECT temperature, COUNT(mark) AS "number_of_records"
FROM records
GROUP BY temperature, mark
ORDER BY mark;