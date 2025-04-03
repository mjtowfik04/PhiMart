Here’s a well-structured `README.md` file for your Phimart project:

---

# Phimart - eCommerce API

Phimart is a RESTful eCommerce API built using Django Rest Framework (DRF). It provides endpoints for managing products, categories, orders, and carts. The project includes JWT authentication via Djoser and API documentation using drf_yasg (Swagger).

## Features

- **User Authentication**: JWT-based authentication using Djoser.
- **Product Management**: CRUD operations for products.
- **Category Management**: Organize products into categories.
- **Cart System**: Add/remove products from the cart.
- **Order Processing**: Place and manage orders.
- **API Documentation**: Auto-generated Swagger UI using drf_yasg.

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL/MySQL (Optional but recommended)
- Virtual Environment (Recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/phimart.git
   cd phimart
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```sh
   python manage.py createsuperuser
   ```

6. Run the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/products/` | GET | List all products |
| `/api/products/{id}/` | GET | Retrieve a product by ID |
| `/api/categories/` | GET | List all categories |
| `/api/orders/` | GET/POST | Retrieve or create an order |
| `/api/cart/` | GET/POST | View or modify the cart |
| `/auth/users/` | POST | Register a user |
| `/auth/token/login/` | POST | Obtain JWT token |

## Authentication

Phimart uses JWT authentication via Djoser. To authenticate:
1. Obtain a token:
   ```sh
   curl -X POST http://127.0.0.1:8000/auth/token/login/ -d "username=user&password=pass"
   ```
2. Use the token in requests:
   ```sh
   curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:8000/api/products/
   ```

## API Documentation

Swagger UI is available at:
```
http://127.0.0.1:8000/swagger/
```

## Technologies Used

- **Django Rest Framework (DRF)** - RESTful API development
- **Djoser** - JWT authentication
- **drf_yasg** - API documentation
- **PostgreSQL/MySQL** (Optional) - Database
- **Docker** (Optional) - Containerization

## Contributing

Feel free to fork and submit a PR. Follow the contribution guidelines.

## License

This project is licensed under the MIT License.

---

Let me know if you need any modifications! 🚀