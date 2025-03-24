"""hw_2025_03_19"""

-- Найти тех, кто не сделал ни одного заказа(процент от всех пользователей)
select
COUNT(distinct su.id) as buyers_counted, COUNT(DISTINCT CASE 
        WHEN so.buyer_id IS NULL THEN su.id 
        ELSE NULL 
    END) AS buyers_without_orders,
(COUNT(DISTINCT CASE 
        WHEN so.buyer_id IS NULL THEN su.id 
        ELSE NULL 
    END) * 1.0 / COUNT(DISTINCT su.id)) AS share
from public.shop_users su 
left join public.shop_orders so on so.buyer_id =su.id

-- Найти 10 самых покупаемых товаров
select 
count(so.goods_id) as count_goods,
sg."name" 
from public.shop_orders so 
left join public.shop_goods sg on sg.id =so.goods_id 
group by 2
order by 1 desc
limit 10

-- Посчитать средний чек на одного пользователя
WITH orders_with_items AS (
    SELECT 
        o.id AS order_id,
        o.buyer_id,
        SUM(g.price) AS total_check
    FROM 
        public.shop_orders o
    LEFT JOIN 
        public.shop_goods g ON g.id = o.goods_id
    GROUP BY 
        o.id, o.buyer_id
    HAVING 
        COUNT(g.id) > 0
)
SELECT 
    AVG(total_check) AS avg_check
FROM 
    orders_with_items

-- Найти самую покупаемую категорию
select 
count(so.goods_id) as count_goods,
scg."name" 
from public.shop_orders so 
left join public.shop_goods sg on sg.id =so.goods_id 
left join public.shop_category_goods scg on scg.id=sg.category_id 
group by 2
order by 1 desc
limit 1

-- Найти самого популярного селлера
with popular as (
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
p.id, su."name" ,su.surname 
from popular p
LEFT JOIN 
    public.shop_users su ON su.id = p.id