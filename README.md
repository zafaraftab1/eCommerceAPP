# 👗 Fashion Website

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.1.5-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Bootstrap-Frontend-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
</p>

<p align="center">
  A stylish Django-powered fashion storefront with category-based product display, modern UI pages, and static/media asset support.
</p>

---

## ✨ Highlights

- Dynamic product/category listing from database (`fashionCategory` model)
- Dedicated pages for shop, cart, contact, signup, and order thank-you
- Media uploads support for category images
- Static asset pipeline with CSS, JS, and image resources
- Admin panel enabled for content management

---

## 🚧 Upcoming Features

- User authentication with personalized profiles
- Product search, filters, and category sorting
- Wishlist and save-for-later functionality
- Secure checkout integration with payment gateway
- Order history and tracking dashboard
- Responsive admin analytics for sales insights

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.1.5 |
| Language | Python |
| Database | PostgreSQL |
| ORM Model | `fashionCategory` |
| Frontend | HTML templates + Bootstrap + JS plugins |
| Media Handling | Pillow |

---

## 📂 Project Structure

```text
fashionWebsite/
├── fashion/                    # App: models, views, urls
├── fashionWebsite/             # Project: settings, root urls, wsgi/asgi
├── templates/fashionHTML/      # HTML templates
├── static/                     # Source static files (css/js/image/scss)
├── staticfiles/                # Collected static files
├── media/                      # Uploaded media files
├── manage.py
└── requirment.txt
```

---

## 🚀 Quick Start

### 1. Clone and enter project

```bash
git clone <your-repo-url>
cd fashionWebsite
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirment.txt
```

### 4. Configure PostgreSQL

Current settings expect:

- Database: `fashionDatabase`
- User: `postgres`
- Password: `aftab@14581`
- Host: `localhost`
- Port: `5432`

Update these in `fashionWebsite/settings.py` if your local setup is different.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create admin user (optional)

```bash
python manage.py createsuperuser
```

### 7. Start development server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/home/`

---

## 🛍️ Available Routes

| URL | View | Purpose |
|---|---|---|
| `/home/` | `home` | Landing page with categories |
| `/shop/` | `shop` | Product/category listing |
| `/cart/` | `cart` | Cart page |
| `/contact/` | `contact` | Contact page |
| `/thankyou/` | `thankyou` | Post-checkout thank you |
| `/signup/` | `signup` | Sign in / sign up page |
| `/shop-single/` | `shopSingle` | Single product page |
| `/admin/` | Django Admin | Content management |

---

## 🧩 Core Model

`fashion/models.py`

```python
class fashionCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fashionCategory/')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    offer = models.BooleanField(default=False)
```

---

## 📸 Media & Static Notes

- Static URL: `/static/`
- Media URL: `/media/`
- Media files are served in development via `urlpatterns + static(...)`

For production, configure a proper static/media hosting strategy (e.g., Nginx + collected static files).

---

## ✅ Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py collectstatic
```

---

## 🔐 Security Reminder

- `DEBUG` is currently `True`
- Secret key and DB credentials are hardcoded in settings

Before deploying, move sensitive values to environment variables.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

---

## 📄 License

This project is open source and available under the MIT License (add a `LICENSE` file if you want MIT officially applied).
