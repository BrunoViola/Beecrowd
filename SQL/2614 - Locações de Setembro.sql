select c.name, r.rentals_date
from customers c
join rentals r on c.id = r.id_customers
where extract(month from rentals_date) = 9 and extract(year from rentals_date)=2016