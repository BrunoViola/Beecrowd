select product.name, provider.name, product.price
from products product
join providers provider on product.id_providers = provider.id
join categories category on product.id_categories = category.id
where product.price > 1000.00 and category.name='Super Luxury';