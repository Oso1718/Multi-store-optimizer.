# Multi-store-optimizer.

This project aims to identify the supermarket or combination of supermarkets that provides the lowest total cost for a grocery basket, helping users plan their shopping in the most cost-efficient way.

The system implements a scalable data pipeline architecture capable of scraping product data, normalizing product information across stores, computing standardized unit prices, and ranking products by cost efficiency.

This project was designed with **future machine learning integration** in mind, including embedding-based product similarity and multi-store basket optimization.

# Real Data Collection

The system collects real product data from Mexican supermarket websites using Scrapy spiders.Currently supported stores include:

- Chedraui
- Soriana 
- La Gran Bodega

This supermarkets were chosen based on their open policies for scraping. Without hurting neither the system nor the supermarket website. (Based on robots.txt)

Each scraping run collects product information including:

- product name
- price
- store
- timestamp

The collected data is stored in a PostgreSQL database for further normalization and price analysis.

# Project Highlights

- Multi-store **web scraping pipeline** using Scrapy  
- **Product normalization system** using regex-based NLP  
- **Unit price standardization** for fair product comparison  
- **SQL ranking engine** for cost-efficient product analysis  
- Architecture designed for **scalability and ML integration**


# Problem/Motivation

This project originated from a simple real-life question:

When buying groceries, how can we know which store — or combination of stores — offers the lowest total cost for an entire shopping basket?

My brother and I have been thinking on it.

Consumers usually compare prices product by product, but determining the optimal store combination is a more complex optimization problem often studied in Operations Research.
This system explores how such optimization could be applied to everyday consumer shopping. Even when individual product prices are visible, it is difficult to determine:

- which store offers the **lowest unit price**
- which **combination of stores** minimizes the total basket cost

This project addresses that problem by building a system capable of:

- collecting grocery prices across multiple stores
- normalizing product information
- computing standardized unit prices
- ranking products by cost efficiency

# System Architecture

The system follows a modular **data pipeline architecture**:

```
Web Scrapers (Scrapy)
↓
Data Normalization Layer
↓
PostgreSQL Database
↓
SQL Ranking Engine
↓
Basket Optimization (future step)
```

Design principle: **Separate data extraction from product intelligence**. This allows the system to scale as more stores and product categories are added.


# Technology Stack

- **Python**
- **Scrapy** — Web scraping
- **PostgreSQL** — Data storage
- **SQL Views** — Ranking queries
- **Regex-based NLP** — Product normalization


# Product Normalization Pipeline

Raw product names scraped from websites are transformed into structured product attributes.
Example:

**Raw product name: Leche Alpura Deslactosada 1L**

Structured output:
```
product_base: milk
brand: alpura
quantity: 1000
unit: ml
```

This allows the system to compare products **across brands and packaging sizes**.

# Unit Price Calculation

To fairly compare products with different package sizes, prices are normalized using: unit_price = price / quantity

Example [add a picture]

# Price Ranking

Products are ranked by lowest **unit price** within the same product category.

Example SQL query:

```sql
SELECT *
FROM ranking_productos
WHERE producto_base = 'leche'
ORDER BY precio_unitario ASC;
```
This allows users to identify the most cost-efficient product option.


# Repository Status & Future Improvements

This repository is currently under active development.

Current capabilities:

- Multi-store product scraping
- Product normalization
- Unit price computation
- SQL-based product ranking
  
The system was intentionally designed to support machine learning extensions.Planned features include:

- Location system for scrap the closest supermarkets and be region based improving results.
- Embedding-based product similarity: Use vector embeddings to improve product matching across stores where product names differ.
- Shopping basket optimization: Compute the minimum cost combination of stores for an entire grocery basket.
- API layer: Expose the ranking and comparison engine through a REST API.
- User Interface for deployment in real world.

This system is intended to work as a first layer of a more complex project which is based on create personalized diets. This layer would be used to be connnected to the diet app which gives the list of products for the recipes and then is searched by the optimizer giving a full user experience.

## Potential Applications

Although this project focuses on grocery price intelligence, the same architecture can be applied to other domains such as:

- supplier cost optimization in supply chains
- procurement analysis for organizations
- price monitoring systems
- consumer price comparison platforms
