-- Link do enunciado: https://judge.beecrowd.com/pt/runs/code/43775911
SELECT d.name, ROUND(sum(salary), 1) AS salary 
	FROM (SELECT id_doctor,
		CASE
			WHEN id_work_shift = 1 THEN hours*150 * (1+(SELECT bonus FROM work_shifts WHERE id = 1)/100)
			WHEN id_work_shift = 2 THEN hours*150 * (1+(SELECT bonus FROM work_shifts WHERE id = 2)/100)
			WHEN id_work_shift = 3 THEN hours*150 * (1+(SELECT bonus FROM work_shifts WHERE id = 3)/100)
		END AS salary
		FROM attendances) AS subconsulta_salario
   JOIN doctors AS d
   ON d.id = subconsulta_salario.id_doctor
	GROUP BY d.name
   ORDER BY salary DESC;