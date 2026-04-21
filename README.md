# 🚀 Company & Employee Management API (DRF)

## 📌 Description
This is a RESTful API built using Django REST Framework (DRF) to manage companies and employees. It provides full CRUD functionality and handles relationships between models using ForeignKey.

---

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework (DRF)
- SQLite

---

## 🚀 Features
- Create, Read, Update, Delete (CRUD) for Company
- Create, Read, Update, Delete (CRUD) for Employee
- ForeignKey relationship (Employee → Company)
- Custom API endpoint to fetch employees of a company  
- Admin panel for data management
- Clean and scalable API structure

---

## 🔗 API Endpoints

### Company APIs
- GET /companies/
- POST /companies/
- GET /companies/{id}/
- PUT /companies/{id}/
- DELETE /companies/{id}/

### Employee APIs
- GET /employees/
- POST /employees/
- GET /employees/{id}/
- PUT /employees/{id}/
- DELETE /employees/{id}/

### Custom Endpoint
- GET /companies/{id}/employees/ → Get all employees of a company

---

## ⚙️ Installation

```bash
# Clone repository
git clone <your-repo-link>

# Move into project
cd companyapi

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver