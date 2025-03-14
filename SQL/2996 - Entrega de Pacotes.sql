-- Link do enunciado: https://judge.beecrowd.com/pt/problems/view/2996
SELECT year, us.name , ur.name
FROM packages AS p
JOIN users AS us
ON us.id = id_user_sender
JOIN users AS ur
ON ur.id = id_user_receiver
WHERE (year=2015 OR color='blue') AND (us.address <> 'Taiwan' AND ur.address <> 'Taiwan')
ORDER BY year DESC;