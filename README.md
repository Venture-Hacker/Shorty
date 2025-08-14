# 🔗 Django URL Shortener

A simple yet functional **URL shortener** built with Django.  
It allows users to enter a long URL and get a **short code** that redirects to the original link.  
The app also tracks click counts and supports link expiration.

---

## 📜 Description

This project implements a basic URL shortening service, similar to Bitly, but self-hosted.  
Users can submit any valid URL, and the application will generate a short URL (e.g., `http://127.0.0.1:8000/abc123`) that redirects to the original destination.

The mappings between short codes and original URLs are stored in a **database**, ensuring persistence across restarts.

---

## ✨ Features

- **Short URL generation** — Generate unique short codes for any URL.
- **Redirects** — Visiting a short code redirects to the original URL.
- **Database storage** — URL mappings are saved in SQLite by default.
- **Click tracking** — Each visit to a short link increments a counter.
- **Expiry date** — Optional expiration date for each link.
- **Recent links list** — Shows the 20 most recently created links.
- **Responsive UI** — Simple, clean Bootstrap interface.
- **QR Code Support** *(optional)* — Easily generate a QR code for each short URL.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3)
- **Database:** SQLite (default, but can use PostgreSQL/MySQL)
- **Frontend:** HTML, Bootstrap 5

---

## 📦 Local Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/django-url-shortener.git
cd django-url-shortener
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```

Visit the app at **http://127.0.0.1:8000/**.

---

### 6️⃣ Create a Superuser (Optional, for Django Admin)
```bash
python manage.py createsuperuser
```
Then login at **http://127.0.0.1:8000/admin/**.

---

## ⚙️ Environment Variables (Optional)
If deploying, configure:
- `DEBUG=False`
- `SECRET_KEY=your-secret-key`
- `ALLOWED_HOSTS=yourdomain.com,127.0.0.1`

---

## 📂 Project Structure
```
urlshortener/
├── shorty/               # Main app
│   ├── migrations/
│   ├── templates/shorty/ # HTML templates
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── urlshortener/          # Project settings
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
└── README.md
```


## 📝 License
This project is licensed under the MIT License — feel free to use and modify it.

---

