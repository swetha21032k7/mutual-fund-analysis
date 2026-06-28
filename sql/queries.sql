-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Mutual Fund
SELECT amfi_code,
       AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total SIP Investment
SELECT SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- 4. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Highest 1-Year Return
SELECT scheme_name,
       return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 7. Average Expense Ratio
SELECT AVG(expense_ratio_pct)
AS average_expense_ratio
FROM fact_performance;

-- 8. Count of Funds by Category
SELECT category,
       COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- 9. Total Investment by Transaction Type
SELECT transaction_type,
       SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Top 5 Highest NAV Values
SELECT amfi_code,
       MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY highest_nav DESC
LIMIT 5;