# FlexiMart Database Schema Documentation

## 1. Entity–Relationship Description

### ENTITY: customers
Purpose: Stores master data related to FlexiMart customers.

Attributes:
- customer_id (PK): Unique surrogate identifier for each customer
- first_name: Customer's first name
- last_name: Customer's last name
- email: Unique email address used for communication and identification
- phone: Standardized contact number of the customer
- city: City of residence
- registration_date: Date the customer registered on FlexiMart

Relationships:
- One customer can place many orders (1:M relationship with `orders`)

### ENTITY: products
Purpose: Stores information about products sold on FlexiMart.

Attributes:
- product_id (PK): Unique surrogate identifier for each product
- product_name: Name of the product
- category: Standardized product category (e.g., Electronics, Clothing)
- price: Unit selling price of the product
- stock_quantity: Available inventory units

Relationships:
- One product can appear in many order items (1:M with `order_items`)

### ENTITY: orders
Purpose: Captures high-level transactional information for customer purchases.

Attributes:
- order_id (PK): Unique identifier for each order
- customer_id (FK): References the customer who placed the order
- order_date: Date on which the order was placed
- total_amount: Total monetary value of the order
- status: Current status of the order (e.g., Pending, Completed)

Relationships:
- Each order belongs to one customer (M:1 with `customers`)
- Each order contains many order items (1:M with `order_items`)

### ENTITY: order_items
Purpose: Stores line-level details of products included in an order.

Attributes:
- order_item_id (PK): Unique identifier for each order line
- order_id (FK): References the associated order
- product_id (FK): References the purchased product
- quantity: Number of units purchased
- unit_price: Price per unit at time of purchase
- subtotal: Calculated as quantity × unit_price

Relationships:
- Each order item belongs to one order (M:1 with `orders`)
- Each order item refers to one product (M:1 with `products`)

## 2. Normalization Explanation (3NF)
The FlexiMart database follows Third Normal Form (3NF) to keep data clean, consistent, and free from duplication.

All tables meet 1NF since fields store single, atomic values with no repeating groups. 2NF is covered because every non-key column depends fully on the primary key—no partial dependencies, thanks to surrogate keys.

For 3NF, non-key columns depend only on the primary key and nothing else. For example, in the customers table, details like name, email and city depend only on customer_id. In the products table, price and stock depend only on product_id, not on category or product name.

This setup avoids common data issues: updates happen in one place, new customers or products can be added without orders, and deleting an order doesn’t wipe out master data. Overall, the design stays reliable, scalable and easy to analyze.

## 3. Sample Data Representation
### customers
| customer_id | first_name | last_name | email               | phone           | city   | registration_date |
|------------|------------|-----------|---------------------|-----------------|--------|-------------------|
| 1          | Rahul      | Mehta     | rahul@gmail.com     | +91-9999999999  | Pune  | 2024-01-15        |
| 2          | Ananya     | Sharma    | ananya@yahoo.com    | +91-8888888888  | Delhi| 2024-02-01        |

### products
| product_id | product_name     | category     | price  | stock_quantity |
|------------|------------------|--------------|--------|----------------|
| 1          | iPhone 14        | Electronics  | 69999  | 25             |
| 2          | Running Shoes    | Footwear     | 2999   | 100            |

### orders
| order_id | customer_id | order_date | total_amount | status     |
|---------|-------------|------------|--------------|------------|
| 101     | 1           | 2024-03-10 | 72998        | Completed  |
| 102     | 2           | 2024-03-12 | 2999         | Completed  |

### order_items
| order_item_id | order_id | product_id | quantity | unit_price | subtotal |
|--------------|----------|------------|----------|------------|----------|
| 1001         | 101      | 1          | 1        | 69999      | 69999    |
| 1002         | 101      | 2          | 1        | 2999       | 2999     |
