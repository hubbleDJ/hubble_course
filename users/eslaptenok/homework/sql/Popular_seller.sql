with seller_count as (
	select 
		shop_users.name,
		shop_users.surname,
		count(1) as ct
	from shop_users
	join shop_goods
		on shop_users.id = shop_goods.seller_id
	group by shop_users.name, shop_users.surname
)

select 
	name,
	surname
from seller_count
where ct = (
	select 
		max(ct)
	from seller_count
)