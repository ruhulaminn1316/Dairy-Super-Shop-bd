# Daily Dairy Shop - E-Commerce Django Project 🥛

[![Python](https://img.shields.io/badge/Python-3.12.3-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.5-green)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Storage-blue)](https://cloudinary.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Online-success)](https://dailydairyshop-3.onrender.com/)
[![Deploy](https://img.shields.io/badge/Deploy-Render-46E3B7)](https://render.com)

## Project Overview

**Daily Dairy Shop** is a fully functional **e-commerce web application** built with **Django** for selling fresh dairy products online (milk, curd, ghee, paneer, cheese, ice cream, etc.).

It features a beautiful, responsive frontend for customers and a powerful custom admin dashboard for managing products, orders, inventory, and customers — all without relying only on Django's default admin.

Perfect for small dairy businesses, startups, or learning full-stack Django development.

**Live Demo:** [https://dailydairyshop-3.onrender.com](https://dailydairyshop-3.onrender.com)

---

## Screenshots

| Homepage (Welcome Slider) | Product Catalog |
|---------------------------|-----------------|
| ![Homepage](https://drive.google.com/uc?id=16_dRqTb6lV_XxB8a0o-pO4Pzoi9IPgD7) | ![Products](https://drive.google.com/uc?id=1RjvFzhSXO2ouvDsT0qZEksyXlT5put4V) |

| Product Details | Admin Dashboard |
|------------------|------------------|
| ![Product Detail](https://drive.google.com/uc?id=1llCnC_9ki7UzG9HQdpX7iOJ-7cVxiO_t) | ![Admin](https://drive.google.com/uc?id=15fXBZQVgPwkHdmwQmGjDs6mIrU-bIkcl) |

---

## Key Features

### Customer Features
- Full-screen animated welcome slider (text + snow effect)
- Browse products by category
- View detailed product page with images
- Add to Cart & Buy Now
- Responsive design (mobile-first)
- Beautiful cards with hover effects
- Small & elegant "View Details" buttons

### Admin Features
- Custom Admin Dashboard (`/adminpanel/`)
- View total products, orders, revenue
- Manage Categories & Products (Add/Edit/Delete)
- Upload product images via Cloudinary
- Track stock & pricing
- View & update order status
- Quick action buttons

### Technical Features
- Django Template Engine
- Cloudinary for image storage
- Session-based cart
- CSRF protection
- Clean, modular code
- Fully commented & documented

---

## Tech Stack

| Technology       | Version     | Purpose                     |
|------------------|-------------|-----------------------------|
| Python           | 3.13+       | Backend Language            |
| Django           | 4.2.7       | Web Framework               |
| Bootstrap        | 5.3         | Responsive UI               |
| Cloudinary       | Latest      | Image Hosting & Management  |
| SQLite           | Default     | Development Database        |
| HTML5 / CSS3 / JS| Modern      | Frontend                    |


## 📌 Project Structure

```
DailyDairyShop/
│
├── adminpanel/
│   ├── templates/adminpanel/
│   │   ├── dashboard_home.html
│   │   ├── products.html
│   │   ├── categories.html
│   │   └── ...
│   ├── urls.py
│   ├── views.py
│   └── models.py
│
├── customer/
│   ├── templates/customer/
│   ├── urls.py
│   ├── views.py
│   └── models.py
│
├── DailyDairyShop/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
├── media/
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/Sharatpsd/DailyDairyShop.git
cd DailyDairyShop
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Run Migrations & Create Superuser**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### **4. Start the Server**

```bash
python manage.py runserver
```

---

## 🚀 Deployment

### Deploy to Render.com

This project is ready to deploy to Render.com! Follow these guides:

- **Quick Start**: See [QUICK_START.md](QUICK_START.md) for fast deployment
- **Detailed Guide (Bengali)**: See [RENDER_DEPLOYMENT_GUIDE_BN.md](RENDER_DEPLOYMENT_GUIDE_BN.md)

**Key Files for Deployment:**
- `build.sh` - Build script for Render
- `Procfile` - Web server configuration
- `render.yaml` - Service configuration
- `.env.example` - Environment variables template

**Quick Deploy Steps:**
1. Push code to GitHub
2. Connect repository to Render.com
3. Add environment variables (SECRET_KEY, DEBUG=False)
4. Deploy! 🎉

**Live Demo:** [https://dailydairyshop-3.onrender.com](https://dailydairyshop-3.onrender.com)

---

## 🌐 Access URLs

| Page                   | Local URL                                                              | Production URL                                                          |
| ---------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Homepage               | [http://127.0.0.1:8000](http://127.0.0.1:8000)                         | [https://dailydairyshop-3.onrender.com](https://dailydairyshop-3.onrender.com) |
| Django Admin           | [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)             | [https://dailydairyshop-3.onrender.com/admin](https://dailydairyshop-3.onrender.com/admin) |
| Custom Admin Dashboard | [http://127.0.0.1:8000/adminpanel/](http://127.0.0.1:8000/adminpanel/) | [https://dailydairyshop-3.onrender.com/adminpanel/](https://dailydairyshop-3.onrender.com/adminpanel/) |

---

## 🚀 Features

* ✅ Admin Dashboard
* ✅ Product & Category Management
* ✅ Customer & Order Handling
* ✅ Frontend for Users to Browse Products
* ✅ Secure Authentication with Google OAuth
* ✅ Cloudinary Image Storage
* ✅ Fully Template-Based UI
* ✅ WhiteNoise for Static Files
* ✅ Production-Ready Configuration
* ✅ SQLite Database (default, PostgreSQL ready)

---

## 🎯 Future Enhancements

* 🔹 User Registration & Login (✅ Partially done with django-allauth)
* 🔹 Wishlist System
* 🔹 Payment Gateway (bKash, Nagad, SSLCommerz)
* 🔹 Order Tracking Page
* 🔹 Email/SMS Notifications
* 🔹 PDF Invoice Generation
* 🔹 Multi-language (Bangla + English)
* 🔹 PostgreSQL Database Integration

---

## 👨‍💻 Author

**Sharat Acharja Mugdho**
Computer Science & Engineering
Green University of Bangladesh

* GitHub: [https://github.com/Sharatpsd](https://github.com/Sharatpsd)
* Email: [sharatacharjee6@gmail.com](mailto:sharatacharjee6@gmail.com)
* Portfolio: [https://mugdho-portfolio.netlify.app/](https://mugdho-portfolio.netlify.app/)

---
