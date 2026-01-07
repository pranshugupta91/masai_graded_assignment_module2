o# FlexiMart Data Architecture Project
Student Name: Pranshu Gupta  
Student ID: bitsom_ba_25071507
Email: [pranshu.gupta91@gmail.com]
Date: January 2026

## Project Overview
This project demonstrates the design and implementation of an end-to-end data architecture for FlexiMart. It covers the complete lifecycle from ingesting raw CSV data using an ETL pipeline, designing normalized relational schemas, performing business analytics with SQL, evaluating and implementing NoSQL solutions, and finally building a star-schema-based data warehouse for OLAP analysis.

## Repository Structure
```
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md
```

## Technologies Used
- Python 3.x (pandas, mysql-connector-python)
- MySQL 8.0 / PostgreSQL 14
- MongoDB 6.0
- SQL (OLTP & OLAP)


## Setup Instructions
### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql
```

### MongoDB Setup
```bash
mongosh < part2-nosql/mongodb_operations.js
```

## Key Learnings
This project strengthened my understanding of designing reliable ETL pipelines and handling real-world data quality issues. I gained hands-on experience with relational modeling, normalization, and writing complex SQL queries for business analytics. Additionally, I learned how NoSQL databases like MongoDB complement relational systems for flexible data models, and how star schemas enable efficient analytical querying in data warehouses.

## Challenges Faced
1. Handling data quality issues in raw CSV files – Solved by applying systematic cleaning steps such as de-duplication, standardization, and validation during the transformation stage.
2. Designing analytics-ready schemas – Addressed by separating OLTP and OLAP workloads and implementing a star schema to support efficient drill-down and roll-up analysis.
