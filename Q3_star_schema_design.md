# FlexiMart Data Warehouse – Star Schema Design
## Section 1: Schema Overview
FlexiMart’s data warehouse follows a star schema optimized for analytical reporting and historical trend analysis. The design centers around a single fact table connected to multiple denormalized dimension tables.

### FACT TABLE: fact_sales
Grain: One row per product per order line item
Business Process: Sales transactions
Purpose: Stores measurable sales metrics at the most detailed transactional level, enabling flexible aggregations.
Measures (Numeric Facts):
- quantity_sold: Number of units sold for the product
- unit_price: Price per unit at the time of sale
- discount_amount: Discount applied to the line item
- total_amount: Final revenue (quantity × unit_price − discount)

Foreign Keys:
- date_key - dim_date
- product_key - dim_product
- customer_key - dim_customer

### DIMENSION TABLE: dim_date
Purpose: Enables time-based analysis such as daily, monthly, quarterly, and yearly trends.
Type: Conformed dimension
Attributes:
- date_key (PK): Surrogate key in YYYYMMDD format
- full_date: Actual calendar date
- day_of_week: Day name (Monday–Sunday)
- month: Numeric month (1–12)
- month_name: Month name (January–December)
- quarter: Fiscal quarter (Q1–Q4)
- year: Calendar year
- is_weekend: Boolean indicator

### DIMENSION TABLE: dim_product
Purpose: Provides descriptive context for product-related analysis.
Attributes:
- product_key (PK): Surrogate key
- product_id: Business/natural product identifier
- product_name: Name of the product
- category: Product category (e.g., Electronics, Fashion)
- brand: Manufacturer or brand name
- price_band: Derived attribute (Low, Medium, High)

### DIMENSION TABLE: dim_customer
Purpose: Supports customer segmentation and geographic analysis.
Attributes:
- customer_key (PK): Surrogate key
- customer_id: Business/natural customer identifier
- customer_name: Full customer name
- email: Customer email address
- city: City of residence
- registration_date: Date the customer registered

## Section 2: Design Decisions
The star schema uses line-item level data (one row per product per order) to keep analysis flexible. This makes it easy to calculate revenue by product, category, customer, or time. You can always roll data up later, but starting with aggregated data limits deeper analysis.

Surrogate keys are used instead of natural keys to keep joins fast and data stable over time. Even if product IDs change in the source system, historical data stays intact.

This setup makes drill-down and roll-up straightforward. Analysts can move from yearly to daily sales using the date dimension, or from category-level numbers down to individual products. Denormalized dimensions reduce joins and keep BI queries fast.

## Section 3: Sample Data Flow
### Source Transaction
Order No. 101
- Customer: John Doe
- Product: Laptop
- Quantity: 2
- Unit Price: ₹50,000
- Order Date: 2024-01-15

### Data Warehouse Representation

fact_sales
```
{
  date_key: 20240115,
  product_key: 5,
  customer_key: 12,
  quantity_sold: 2,
  unit_price: 50000,
  discount_amount: 0,
  total_amount: 100000
}
```

dim_date
```
{
  date_key: 20240115,
  full_date: '2024-01-15',
  day_of_week: 'Monday',
  month: 1,
  month_name: 'January',
  quarter: 'Q1',
  year: 2024,
  is_weekend: false
}
```

dim_product
```
{
  product_key: 5,
  product_id: 'P005',
  product_name: 'Laptop',
  category: 'Electronics',
  brand: 'Dell',
  price_band: 'High'
}
```

dim_customer
```
{
  customer_key: 12,
  customer_id: 'C012',
  customer_name: 'John Doe',
  email: 'john.doe@email.com',
  city: 'Mumbai',
  registration_date: '2023-11-20'
}
```