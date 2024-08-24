select customer.name
from customers customer
join legal_person on legal_person.id_customers = customer.id;