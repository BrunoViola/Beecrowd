select product.name
from products product
join providers provider on product.id_providers = provider.id
where product.amount>10 and product.amount<20 and provider.name like 'P%';