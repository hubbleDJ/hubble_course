-- Найти тех, кто не сделал ни одного заказа (процент от всех пользователей)
SELECT 
    COUNT(DISTINCT su.id) AS buyers_counted, 
    COUNT(DISTINCT CASE 
        WHEN so.buyer_id IS NULL THEN su.id 
        ELSE NULL 
    END) AS buyers_without_orders,
    (COUNT(DISTINCT CASE 
        WHEN so.buyer_id IS NULL THEN su.id 
        ELSE NULL 
    END) * 1.0 / COUNT(DISTINCT su.id)) AS share
FROM public.shop_users su 
LEFT JOIN public.shop_orders so ON so.buyer_id = su.id;

-- Найти 10 самых покупаемых товаров
SELECT 
    COUNT(so.goods_id) AS count_goods,
    sg."name"
FROM public.shop_orders so 
LEFT JOIN public.shop_goods sg ON sg.id = so.goods_id 
GROUP BY sg."name"
ORDER BY count_goods DESC
LIMIT 10;

-- Посчитать средний чек на одного пользователя
WITH orders_with_items AS (
    SELECT 
        o.id AS order_id,
        o.buyer_id,
        SUM(g.price) AS total_check
    FROM public.shop_orders o
    LEFT JOIN public.shop_goods g ON g.id = o.goods_id
    GROUP BY o.id, o.buyer_id
    HAVING COUNT(g.id) > 0
)
SELECT 
    AVG(total_check) AS avg_check
FROM orders_with_items;

-- Найти самую покупаемую категорию
SELECT 
    COUNT(so.goods_id) AS count_goods,
    scg."name"
FROM public.shop_orders so 
LEFT JOIN public.shop_goods sg ON sg.id = so.goods_id 
LEFT JOIN public.shop_category_goods scg ON scg.id = sg.category_id 
GROUP BY scg."name"
ORDER BY count_goods DESC
LIMIT 1;

-- Найти самого популярного селлера
WITH popular AS (
    SELECT 
        COUNT(so.goods_id) AS count_goods,
        sg.seller_id AS id
    FROM public.shop_orders so
    LEFT JOIN public.shop_goods sg ON sg.id = so.goods_id
    GROUP BY sg.seller_id
    ORDER BY count_goods DESC
    LIMIT 1
)
SELECT 
    p.id, 
    su."name", 
    su.surname 
FROM popular p
LEFT JOIN public.shop_users su ON su.id = p.id;
