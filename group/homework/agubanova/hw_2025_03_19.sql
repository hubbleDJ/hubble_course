-- 1. Найти тех, кто не сделал ни одного заказа (процент от всех пользователей)
SELECT 
    COUNT(DISTINCT su.id) AS total_users,
    COUNT(DISTINCT su.id) - COUNT(DISTINCT so.buyer_id) AS users_without_orders,
    (COUNT(DISTINCT su.id) - COUNT(DISTINCT so.buyer_id)) * 1.0 / COUNT(DISTINCT su.id) AS share
FROM 
    public.shop_users su
LEFT JOIN 
    public.shop_orders so ON su.id = so.buyer_id;

-- 2. Найти 10 самых покупаемых товаров
SELECT 
    COUNT(so.goods_id) AS count_goods,
    sg."name" 
FROM 
    public.shop_orders so 
LEFT JOIN 
    public.shop_goods sg ON sg.id = so.goods_id 
GROUP BY 
    sg."name"
ORDER BY 
    count_goods DESC
LIMIT 10;

-- 3. Посчитать средний чек на одного пользователя
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
    AVG(total_check) AS avg_check
FROM 
    order_checks;

-- 4. Найти самую покупаемую категорию
SELECT 
    COUNT(so.goods_id) AS count_goods,
    scg."name"
FROM 
    public.shop_orders so 
LEFT JOIN 
    public.shop_goods sg ON sg.id = so.goods_id 
LEFT JOIN 
    public.shop_category_goods scg ON scg.id = sg.category_id 
GROUP BY 
    scg."name"
ORDER BY 
    count_goods DESC
LIMIT 1;

-- 5. Найти самого популярного селлера
WITH top_seller AS (
    SELECT 
        COUNT(so.goods_id) AS count_goods,
        sg.seller_id AS id
    FROM 
        public.shop_orders so
    LEFT JOIN 
        public.shop_goods sg ON sg.id = so.goods_id
    GROUP BY 
        sg.seller_id
    ORDER BY 
        count_goods DESC
    LIMIT 1
)
SELECT 
    s.id, su."name", su.surname 
FROM 
    top_seller s
LEFT JOIN 
    public.shop_users su ON su.id = s.id;
