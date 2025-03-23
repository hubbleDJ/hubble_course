-- 1. Найти тех, кто не сделал ни одного заказа(процент от всех пользователей)
SELECT 
    COUNT(DISTINCT su.id) AS total_users,
    COUNT(DISTINCT su.id) - COUNT(DISTINCT so.buyer_id) AS users_without_orders,
    (COUNT(DISTINCT su.id) - COUNT(DISTINCT so.buyer_id)) * 1.0 / COUNT(DISTINCT su.id) AS doly
FROM public.shop_users su
LEFT JOIN public.shop_orders so 
    ON su.id = so.buyer_id

 -- 2. Найти 10 самых покупаемых товаров
 select 
count(so.goods_id) as count_goods,
--goods_id 
sg."name" 
from public.shop_orders so 
left join public.shop_goods sg on sg.id =so.goods_id 
group by 2
order by 1 desc
limit 10 
  3. Посчитать средний чек на одного пользователя
  WITH order_checks AS (
    SELECT 
        so.id AS order_id,
        so.buyer_id,
        SUM(sg.price) AS total_check
    FROM 
        public.shop_orders so
    LEFT JOIN 
        public.shop_goods sg ON sg.id = so.goods_id
    GROUP BY 
        so.id, so.buyer_id
    HAVING 
        COUNT(sg.id) > 0
)
SELECT 
    --buyer_id,
    AVG(total_check) AS avg_check
FROM 
    order_checks
--GROUP BY 
   -- buyer_id;
 -- 4. Найти самую покупаемую категорию
  select 
count(so.goods_id) as count_goods,
scg."name" 
from public.shop_orders so 
left join public.shop_goods sg on sg.id =so.goods_id 
left join public.shop_category_goods scg on scg.id=sg.category_id 
group by 2
order by 1 desc
limit 1 
 -- 5. Найти самого популярного селлера
  with top_seller as (
SELECT 
    COUNT(so.goods_id) AS count_goods,
    sg.seller_id as id
FROM 
    public.shop_orders so
LEFT JOIN 
    public.shop_goods sg ON sg.id = so.goods_id
GROUP BY 
    sg.seller_id
ORDER BY 
    count_goods DESC
LIMIT 1)
select 
s.id, su."name" ,su.surname 
from top_seller s
LEFT JOIN 
    public.shop_users su ON su.id = s.id