with res_count as (
	select 
		shop_category_goods.name,
		count(1) as ct 
	from shop_category_goods
	join shop_goods
		on shop_category_goods.id = shop_goods.category_id
	join shop_orders
		on shop_goods.id = shop_orders.goods_id
	group by shop_category_goods.name
)

select
	name
from res_count
where ct = (
	select 
		max(ct)
	from res_count
)