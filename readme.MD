
# E-Commerce API Documentation

## Introduction

Welcome to the E-Commerce API documentation. This API allows you to interact with our e-commerce platform to perform various actions such as retrieving product information, managing user accounts, and processing orders.

## Base URL

The base URL for all API endpoints is:

```
https://api.example.com/v1
```

## Authentication

All requests to the API must include an API key in the headers:

```http
Authorization: Bearer YOUR_API_KEY
```

You can obtain an API key by registering on our developer portal.

## Endpoints

### 1. Products

#### 1.1 Get All Products

```http
GET /products
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 29.99,
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "category": "Electronics"
  },
  // More products...
]
```

#### 1.2 Get Product by ID

```http
GET /products/{id}
```

**Response:**

```json
{
  "id": 1,
  "name": "Product 1",
  "price": 29.99,
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "category": "Electronics"
}
```

### 2. Users

#### 2.1 Create User

```http
POST /users
```

**Request:**

```json
{
  "username": "john_doe",
  "email": "john.doe@example.com",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "id": 123,
  "username": "john_doe",
  "email": "john.doe@example.com"
}
```

### 3. Orders

#### 3.1 Create Order

```http
POST /orders
```

**Request:**

```json
{
  "user_id": 123,
  "products": [
    {
      "product_id": 1,
      "quantity": 2
    },
    // More products...
  ]
}
```

**Response:**

```json
{
  "id": 456,
  "user_id": 123,
  "products": [
    {
      "product_id": 1,
      "quantity": 2
    },
    // More products...
  ],
  "total_price": 59.98,
  "status": "Pending"
}
```

## Error Handling

In case of an error, the API will return a JSON response with an error message:

```json
{
  "error": "Invalid API key"
}
```

## Rate Limiting

To ensure fair usage, the API has rate limiting in place. Excessive requests may result in temporary suspension.




# Project in CS Elective 1: Web Application in Application Programming Interface
## BSCS 3rd Year, Block 3

**Team Members:**
- Chu, John Cedrick
- Basig, John Clyde
- Ng, Kristian Marc Anthony
- Cayabyab, Charls Brent




