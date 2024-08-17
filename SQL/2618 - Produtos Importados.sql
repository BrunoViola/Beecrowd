select product.name, provider.name, category.name
from products product
join providers provider on product.id_providers = provider.id
join categories category on product.id_categories = category.id
where provider.name = 'Sansul SA' and category.name = 'Imported';