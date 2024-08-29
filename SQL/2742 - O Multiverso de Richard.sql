select lifereg.name, trunc(lifereg.omega*1.618,3) as "Fator N"
from life_registry lifereg
join dimensions dim on dim.id = lifereg.dimensions_id
where (lifereg.dimensions_id = 1 or lifereg.dimensions_id = 5) and lifereg.name like 'Richard%';