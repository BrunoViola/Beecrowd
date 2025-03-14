-- Link do enunciado: https://judge.beecrowd.com/pt/problems/view/2988
-- Primeira versão
SELECT t.name, COALESCE(SUM(
		CASE
			WHEN t.id = m.team_1 OR t.id = m.team_2 THEN 1
            ELSE 0
        END
	), 0) AS matches,
    COALESCE(SUM(
		CASE
			WHEN (t.id = m.team_1 AND team_1_goals>team_2_goals) THEN 1
            WHEN (t.id = m.team_2 AND team_2_goals>team_1_goals) THEN 1
            ELSE 0
        END), 0) AS victories,
	COALESCE(SUM(
		CASE
			WHEN (t.id = m.team_1 AND team_1_goals<team_2_goals) THEN 1
            WHEN (t.id = m.team_2 AND team_2_goals<team_1_goals) THEN 1
            ELSE 0
        END
    ), 0) AS defeats,
    COALESCE(SUM(
		CASE
			WHEN (t.id = m.team_1 AND team_1_goals=team_2_goals) THEN 1
            WHEN (t.id = m.team_2 AND team_2_goals=team_1_goals) THEN 1
            ELSE 0
        END
    ), 0) AS draws,
    (COALESCE((SUM(
		CASE
			WHEN (t.id = m.team_1 AND team_1_goals>team_2_goals) THEN 1
            WHEN (t.id = m.team_2 AND team_2_goals>team_1_goals) THEN 1
            ELSE 0
        END)*3), 0)+COALESCE(SUM(
		CASE
			WHEN (t.id = m.team_1 AND team_1_goals=team_2_goals) THEN 1
            WHEN (t.id = m.team_2 AND team_2_goals=team_1_goals) THEN 1
            ELSE 0
        END
    ), 0)) AS score
FROM teams AS t, matches AS m
GROUP BY t.name
ORDER BY score DESC;

-- Segunda versão
SELECT sub_matches.name, sub_matches.matches, COALESCE(sub_victories.victories, 0) AS victories, COALESCE(sub_defeats.defeats, 0) AS defeats, COALESCE(sub_draws.draws, 0) AS draws, (COALESCE((victories*3), 0)+COALESCE(draws, 0)) AS score
FROM(SELECT t.id, t.name, count(m.id) AS matches
					FROM teams AS t, matches AS m
					WHERE t.id = m.team_1 OR t.id = m.team_2
                    GROUP BY t.id, t.name) AS sub_matches
LEFT JOIN (SELECT t.id, t.name, count(t.id) AS victories
			FROM teams AS t, matches AS m
			WHERE (t.id = m.team_1 AND team_1_goals>team_2_goals) OR (t.id = m.team_2 AND team_2_goals>team_1_goals)
			GROUP BY t.id, t.name) AS sub_victories
ON sub_matches.id = sub_victories.id
LEFT JOIN (SELECT t.id, t.name, count(m.id) AS defeats
			FROM teams AS t, matches AS m
			WHERE (t.id = m.team_1 AND team_1_goals<team_2_goals) OR (t.id = m.team_2 AND team_2_goals<team_1_goals)
			GROUP BY t.id, t.name) AS sub_defeats
ON sub_matches.id = sub_defeats.id
LEFT JOIN(SELECT t.id, t.name, count(m.id) AS draws
			FROM teams AS t, matches AS m
			WHERE (t.id = m.team_1 AND team_1_goals=team_2_goals) OR (t.id = m.team_2 AND team_2_goals=team_1_goals)
			GROUP BY t.id, t.name) AS sub_draws
ON sub_matches.id = sub_draws.id
ORDER BY score DESC;