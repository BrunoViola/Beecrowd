-- Link do enunciado: https://judge.beecrowd.com/pt/problems/view/2990
SELECT e.cpf, e.enome, d.dnome
	FROM empregados e
   JOIN departamentos d
   ON e.dnumero = d.dnumero
   WHERE e.cpf NOT IN (SELECT cpf_emp FROM trabalha)
   ORDER BY e.cpf ASC;