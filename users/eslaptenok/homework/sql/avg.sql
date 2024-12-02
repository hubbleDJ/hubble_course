select 
	shop_users.name,
	shop_users.surname,
	round(avg(price)) as avg
from shop_users
join shop_orders
	on shop_users.id = shop_orders.buyer_id
join shop_goods
	on shop_orders.goods_id = shop_goods.id
group by shop_users.name, shop_users.surname
order by avg desc 