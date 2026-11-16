# Executive Summary — Duka Retail Performance

## Business question
How do sales vary by branch, product category, month, and customer segment, and where should management focus to improve retail performance?

## Dataset and method
This is a **synthetic training dataset**, not actual company or customer records. It contains 5,000 transactions dated 1 January–31 December 2025, 993 customer IDs, 20 products, and five branches. Python (pandas, NumPy, Matplotlib), SQLite/SQL, and a Welch two-sample t-test were used.

## KPI snapshot
- Net sales revenue: **KES 3,302,319.80**
- Transactions: **5,000**
- Average transaction value: **KES 660.46**
- Unique customers: **993**
- Highest-revenue branch: **Nairobi**
- Highest-revenue category: **Household**
- Strongest month: **2025-02**

## Findings
1. **Branch performance:** Nairobi generated the highest total net sales in this simulated sample. Branch totals are shown in `figures/revenue_by_branch.png`.
2. **Category mix:** Household was the leading category by net sales. Category-level results are shown in `figures/revenue_by_category.png`.
3. **Seasonality:** 2025-02 was the strongest month in the simulated year. The monthly trend is shown in `figures/monthly_sales_trend.png`.
4. **Product focus:** The five highest-revenue products are listed in `stakeholder_summary.xlsx`.
5. Statistical test: A Welch independent-samples t-test comparing Nairobi and Mombasa transaction values found no statistically significant difference at the 5% significance level (t = -0.4135, p = 0.6793). Nairobi recorded a mean transaction value of KES 684.44, compared with KES 703.80 in Mombasa. This suggests that the observed difference in average transaction values is not statistically significant.

## Recommendations
- Review stock availability and replenishment performance for the top revenue categories and products.
- Compare branch-level stock-outs, pricing, and promotions before reallocating inventory.
- Plan promotions using monthly demand patterns, then evaluate results against a baseline.
- Track average transaction value, repeat-customer activity, and discount rate monthly.

## Limitations
The data is synthetically generated for learning. Results illustrate an analysis workflow and must not be represented as verified performance of a real retailer. The simulated sample does not establish causation.
