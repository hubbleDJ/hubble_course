--1. Найти тех, кто не сделал ни одного заказа(процент от всех пользователей)
select
	((count(s_u.id) - count(buyer_id))*1.0/count(s_u.id))*100 as not_buyer_id
from public.shop_users as s_u
left join shop_orders as s_o
on s_u.id = s_o.buyer_id;

--2. Найти 10 самых покупаемых товаров
select
	s_g.name as name_of_good,
	goods_id,
 	count(buyer_id) as buyer_id
from public.shop_orders as s_o
join public.shop_goods as s_g 
on s_o.goods_id = s_g.id
group by goods_id, name_of_good
order by buyer_id desc
limit 10;

--3. Посчитать средний чек на одного пользователя
select
	sum(price)/count(s_u.id)*1.0 as mid_cheque_on_usr
from public.shop_users as s_u
left join shop_goods as s_g 
on s_g.id = s_u.id;

--4. Найти самую покупаемую категорию
select
	s_c_g.id as cathegory_id,
	s_c_g.name as cathegory_name,
	s_g.name as name_of_good,
	goods_id,
 	count(buyer_id) as buyer_id
from public.shop_orders as s_o
join public.shop_goods as s_g 
on s_o.goods_id = s_g.id
join public.shop_category_goods as s_c_g
on s_g.category_id= s_c_g.id
group by goods_id, name_of_good, cathegory_id, cathegory_name
order by buyer_id desc
limit 1;

--5. Найти самого популярного селлера

select
	s_g.seller_id as seller_id,
	s_g.name as name_of_good,
 	count(buyer_id) as count_of_buyer_id
from public.shop_orders as s_o
join public.shop_goods as s_g 
on s_o.goods_id = s_g.id
group by goods_id, name_of_good, seller_id
order by count_of_buyer_id desc
limit 1;
