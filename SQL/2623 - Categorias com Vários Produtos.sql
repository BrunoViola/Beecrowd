select product.name, category.name
from products product
join categories category on product.id_categories = category.id
where product.amount > 100 and (category.id = 1 or category.id = 2 or category.id = 3 or category.id = 6 or category.id = 9)
order by category.id;