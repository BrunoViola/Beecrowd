select c.name, sum(p.amount) as total_amount
from categories c
join products p on c.id = p.id_categories
group by c.name;