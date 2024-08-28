(select concat('Podium: ', team) as name
from league
order by position asc
limit 3)
union all
(select concat('Demoted: ', team) as name
from (
		select team, position
		from league
        order by position desc 
        limit 2
) as subquery
order by position asc);