1. Найти тех, кто не сделал ни одного заказа(процент от всех пользователей)
select
	((count(s_u.id) - count(buyer_id))*1.0/count(s_u.id))*100 as not_buyer_id
from public.shop_users as s_u
left join shop_orders as s_o
on s_u.id = s_o.buyer_id;

2. Найти 10 самых покупаемых товаров
3. Посчитать средний чек на одного пользователя
select
	sum(price)/count(s_u.id)*1.0 as mid_cheque_on_usr
from public.shop_users as s_u
left join shop_goods as s_g 
on s_g.price = s_u.id;

4. Найти самую покупаемую категорию
5. Найти самого популярного селлера