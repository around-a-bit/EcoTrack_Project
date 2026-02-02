
# 🌱 EcoTrack – Waste Pickup & Segregation Tracker (Django + Docker + PostgreSQL)

EcoTrack is a role-based waste pickup tracking platform built using **Django**, **PostgreSQL**, and **Docker**.  
It supports real operational workflows such as **pickup requests**, **collector assignment**, **status tracking**, and basic **analytics** — with a lightweight AI-based waste type suggestion system.

## 🚀 Key Features

### ✅ Role-Based Access (RBAC)
- **Resident**: Create pickup requests, track status
- **Admin**: View all requests, assign collectors, monitor analytics
- **Collector**: View assigned pickups and update status

### ✅ Pickup Workflow
`PENDING → ASSIGNED → PICKED → COMPLETED`

### ✅ AI + Segregation Scoring (Lightweight)
- Suggests waste type from user description (rule-based AI)
- Calculates segregation score (0–100)
- Displays waste handling tips

### ✅ Admin Analytics Dashboard
- Total requests count
- Breakdown by status
- Breakdown by waste type

### ✅ REST API + Swagger Docs
- REST endpoints via Django REST Framework
- Swagger UI for API testing and documentation

### ✅ Dockerized Stack
- Django App + PostgreSQL run as containers
- Portable and reproducible setup

---

## 🏗️ Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL (Docker container)
- **Containerization:** Docker + Docker Compose
- **API:** Django REST Framework
- **Docs:** drf-yasg (Swagger / ReDoc)
- **Auth (API):** JWT (SimpleJWT)
- **Deployment:** Render (Docker runtime)

---

## 🧠 System Architecture

```

Browser Client
|
v
Django Web App (Docker Container)  <-->  PostgreSQL (Docker Container)
|
v
Render Cloud Deployment

````

---

## 📌 Project Modules

### 1) Accounts
- Register / Login / Logout
- User Profile auto-created via signals
- Roles: Resident / Collector / Admin

### 2) Pickups
- Pickup request creation and tracking
- Collector assignment
- Status updates and dashboards

### 3) Analytics
- Request statistics by waste type and status

### 4) API + Swagger
- API routes exposed under `/api/`
- Swagger UI at `/swagger/`

---

## ✅ Local Setup (Without Docker)
> Recommended for debugging, learning, and development.

### 1) Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
````

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run migrations

```bash
python manage.py migrate
```

### 4) Create superuser

```bash
python manage.py createsuperuser
```

### 5) Run server

```bash
python manage.py runserver
```

App runs at:
✅ `http://127.0.0.1:8000/`

---

## 🐳 Docker Setup (Recommended)

> Best practice setup for consistent environment across machines.

### 1) Start containers

```bash
docker compose up --build -d
```

### 2) Run migrations inside container

```bash
docker exec -it ecotrack_web python manage.py migrate
```

### 3) Create admin user

```bash
docker exec -it ecotrack_web python manage.py createsuperuser
```

### 4) Open app

✅ `http://127.0.0.1:8000/`

---

## 🗄️ Check PostgreSQL Data (Docker)

Enter Postgres container:

```bash
docker exec -it ecotrack_db psql -U ecouser -d ecotrack
```

List tables:

```sql
\dt
```

View pickup request data:

```sql
SELECT * FROM pickups_pickuprequest;
```

Exit:

```sql
\q
```

---

## 🔐 Environment Variables

### Local `.env` example:

```env
DB_NAME=ecotrack
DB_USER=ecouser
DB_PASSWORD=ecopass
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Production (Render) example:

```env
DEBUG=False
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=ecotrack-project.onrender.com

DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=5432
```

⚠️ Note: `ALLOWED_HOSTS` must NOT contain `https://`

✅ Correct:

```
ecotrack-project.onrender.com
```

❌ Wrong:

```
https://ecotrack-project.onrender.com
```

---

## 📌 Useful Routes

### Website

* Home: `/`
* Register: `/accounts/register/`
* Login: `/accounts/login/`
* My Requests: `/my-requests/`
* Admin Dashboard: `/admin-dashboard/`
* Collector Dashboard: `/collector/`

### Admin Panel

* Django Admin: `/admin/`

### API & Docs

* Swagger UI: `/swagger/`
* ReDoc: `/redoc/`
* JWT Token: `/api/token/`
* JWT Refresh: `/api/token/refresh/`
* My Pickups API: `/api/my-pickups/`

---

## 🧪 Notes (Industry Practices Implemented)

* ✅ Dockerized database + app stack
* ✅ Role-based access control (RBAC)
* ✅ Environment-based configuration (safe production setup)
* ✅ Workflow-driven system design (pickup lifecycle)
* ✅ Swagger documentation for APIs
* ✅ Deploy-ready structure for cloud environments

---

## 👨‍💻 Author

**Sankar Rajak**

EcoTrack – Built for industry-ready Django + DevOps practice.


