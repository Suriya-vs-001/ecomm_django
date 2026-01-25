# E-Commerce Project 🛒

A modular, scalable E-commerce backend built with **Django**. This project is designed to separate concerns into distinct apps for authentication, product management, orders, and payments.

## 🚀 Development Status & Roadmap

You asked for a step-by-step update on where we are. Here is the current state of the project:

### ✅ Completed & Active (Connected)
These modules are wired up in the main `urls.py` and are accessible via API endpoints.
- **`custom_auth`**: Custom user authentication.
- **`userdetails`**: User profile management.
- **`policy`**: Privacy and usage policies.
- **`base`**: Core project templates and views.

### 🚧 In Development (Backend Ready)
These apps exist and have models/admin files, but **need to be connected** to the main `urls.py` and have their own valid `views.py` and `urls.py`.
- **`products`**: Product catalog (Models exist).
- **`payments`**: Integration with Razorpay (Views implemented, needs URL routing).
- **`cart`**: Shopping cart logic.
- **`orders`**: Order processing.
- **`shipping`**: Shipping address and logistics.
- **`reviews`**: Product ratings and comments.
- **`wishlist`**: Save for later.
- **`offers` / `promotions`**: Discount management.

### 📋 To-Do List (Roadmap)
1.  **Connect Modules**: Create `urls.py` for `products`, `cart`, and `payments` and include them in `Ecommerce_main/urls.py`.
2.  **Finalize Views**: Ensure `products` returns JSON/Template data correctly.
3.  **Frontend Integration**: Connect these APIs to the templates.

---

## 🛠️ How It Was Built

This project follows a **Modular Monolith** architecture. Instead of one giant file, every feature is its own "App".

### Key Technologies
- **Django 5.0**: The core framework.
- **SQLite**: Database (Default).
- **Razorpay**: Payment Gateway (recently integrated).
- **Python Decouple**: For security (`.env` file).

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally.

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Installation
Clone the repo and enter the directory:
```bash
git clone <your-repo-url>
cd Ecommerceproject
```

Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration (.env)
Create a `.env` file in the root directory (`d:\python\Ecommerceproject\.env`) and add your secrets:
```ini
SECRET_KEY=your_django_secret_key
DEBUG=True
RAZORPAY_API_KEY=your_razorpay_key_id
RAZORPAY_API_SECRET=your_razorpay_key_secret
```

### 4. Database Migration
Apply the migrations to set up your database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the app!

---

## 📂 Project Structure
```text
Ecommerceproject/
├── Ecommerce_main/      # Core settings and URL routing
├── custom_auth/         # User Authentication (Active)
├── userdetails/         # User Profiles (Active)
├── products/            # Product Models (Needs URLs)
├── payments/            # Razorpay Integration (Needs URLs)
├── cart/                # Cart Logic
├── orders/              # Order Management
├── templates/           # HTML Files
├── static/              # CSS/JS images
└── manage.py            # Entry point
```
