-- Duka Retail Performance: SQL analysis examples
-- 1. Revenue and transaction count by branch
SELECT branch, COUNT(*) AS transactions, ROUND(SUM(net_sales_kes),2) AS revenue_kes
FROM sales_clean GROUP BY branch ORDER BY revenue_kes DESC;

-- 2. Product category performance
SELECT p.category, SUM(s.net_sales_kes) AS revenue_kes
FROM sales_clean s JOIN products p ON s.product_id = p.product_id
GROUP BY p.category ORDER BY revenue_kes DESC;

-- 3. Customers contributing more than KES 20,000
SELECT customer_id, SUM(net_sales_kes) AS customer_revenue
FROM sales_clean GROUP BY customer_id HAVING SUM(net_sales_kes) > 20000
ORDER BY customer_revenue DESC;

-- 4. Monthly revenue with month-over-month comparison (window function)
WITH monthly AS (
  SELECT strftime('%Y-%m', date) AS month, SUM(net_sales_kes) AS revenue_kes
  FROM sales_clean GROUP BY strftime('%Y-%m', date)
)
SELECT month, revenue_kes,
       LAG(revenue_kes) OVER (ORDER BY month) AS previous_month_revenue,
       revenue_kes - LAG(revenue_kes) OVER (ORDER BY month) AS change_kes
FROM monthly ORDER BY month;

-- 5. Top five products by revenue
SELECT p.product_name, SUM(s.net_sales_kes) AS revenue_kes
FROM sales_clean s JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name ORDER BY revenue_kes DESC LIMIT 5;

-- 6. Repeat customers (more than one transaction)
SELECT customer_id, COUNT(*) AS transactions, SUM(net_sales_kes) AS revenue_kes
FROM sales_clean GROUP BY customer_id HAVING COUNT(*) > 1
ORDER BY transactions DESC;
