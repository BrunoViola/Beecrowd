select product.name, provider.name
from products product
join providers provider on provider.id = product.id_providers
where provider.name = 'Ajax SA';