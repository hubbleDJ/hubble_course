select 
	name,
	count(1) as quantity
from shop_goods
join shop_orders
	on shop_goods.id = shop_orders.goods_id 
group by name
order by quantity desc
limit 10