select customer.name, pedido.id
from customers customer
join orders pedido on pedido.id_customers = customer.id
where extract(year from pedido.orders_date)=2016 and extract(month from pedido.orders_date)<=6;