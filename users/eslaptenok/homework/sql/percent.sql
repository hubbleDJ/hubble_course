select 
	ROUND((COUNT(*) - COUNT(goods_id)) * 100.00 / COUNT(*), 2) as res
from shop_users
left join shop_orders
	on shop_users.id = shop_orders.buyer_id 
