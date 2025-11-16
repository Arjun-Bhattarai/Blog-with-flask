# Blog-with-flask
# 📘 Flask Blog Website

A simple and clean Blog Website built using **Flask**, **SQLAlchemy**, and **Bootstrap**.  
It includes an **Admin Dashboard**, **Login System**, and complete **CRUD for Blog Posts**.

---

## 🚀 Features
- Admin Login / Logout  
- Create, Edit, Delete Posts  
- Category Management  
- Dashboard for Admin  
- Public Blog Homepage  
- Single Post Page  
- Responsive Design  

---

## 📁 Project Structure
```
Blog-with-flask/
│── app.py
│── models.py
│── requirements.txt
│── instance/
│    └── blog.db
│── templates/
│    ├── base.html
│    ├── home.html
│    ├── post.html
│    ├── login.html
│    ├── dashboard.html
│    ├── add_post.html
│    ├── edit_post.html
│    └── categories.html
│── static/
     ├── style.css
     └── images/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/your-username/Blog-with-flask.git
cd Blog-with-flask
```

### 2. Create virtual environment
```
python -m venv venv
```

### 3. Activate virtual environment  
**Windows**
```
venv\Scripts\activate
```
**Mac/Linux**
```
source venv/bin/activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Run the application
```
python app.py
```

Your app will run here:  
👉 http://127.0.0.1:5000/

---

## 🛠 Tech Stack
- Flask  
- SQLAlchemy  
- Bootstrap  
- Jinja2  
- Werkzeug Security  

---

## 📄 License
Free to use and modify for learning or personal projects.
