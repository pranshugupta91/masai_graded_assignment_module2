# NoSQL Database Analysis – FlexiMart (Question 2)

## Section A: Limitations of RDBMS (Relational Databases)
Relational databases such as MySQL or PostgreSQL are effective for structured data but struggle with highly diverse product catalogs. A fixed schema forces all products to share the same columns, which is inefficient when different categories have distinct attributes (e.g., laptops need RAM and processor, shoes need size and color). This results in many nullable columns or complex subtype tables.

Frequent schema changes are another limitation. Adding new product types often requires ALTER TABLE operations, which are risky and disruptive in production. Additionally, storing customer reviews as nested data is unnatural in RDBMS; it typically requires separate tables and joins, increasing query complexity and reducing read performance. These issues limit agility and scalability for evolving product data.

## Section B: Benefits of Using MongoDB (NoSQL)
MongoDB solves these problems through a flexible, document-based schema. Each product can store only the attributes relevant to its category, allowing laptops and shoes to coexist without wasted fields. This removes the need for frequent schema migrations.

MongoDB supports embedded documents, enabling customer reviews to be stored directly inside product documents. This aligns with access patterns and improves read performance by avoiding joins. Furthermore, MongoDB offers horizontal scalability via sharding, allowing FlexiMart to scale product data and traffic across multiple nodes efficiently.

## Section C: Trade-offs of Using MongoDB
MongoDB has trade-offs compared to relational databases. It provides weaker support for complex multi-document transactions and joins, which can complicate consistency-heavy workflows. Additionally, schema flexibility can lead to inconsistent data if validation rules are not enforced at the application or database level, increasing governance responsibility.