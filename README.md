# Bahandi Write-Offs MVP ☕

A mobile-first, dark-themed write-off automation system for retail stores with iiko API mock integration. Developed for Mentoria Hackathon.

---

## 🛠 Tech Stack
- **Backend**: Django 6.0 + Django REST Framework (DRF)
- **Frontend**: Mobile-first Single Page App (Vanilla HTML5 / CSS3 / JavaScript) with full-screen photo viewer and dynamic forms.

---

## 🚀 Quick Start

1. **Activate environment & install packages**:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Seed demo data** (outlets, users, tokens):
   ```bash
   python manage.py seed_data
   ```
3. **Start development server**:
   ```bash
   python manage.py runserver
   ```
   Open **[http://localhost:8000/](http://localhost:8000/)** in your mobile-simulated browser.

---

## 🔑 Demo Accounts

| Role | Username | Password | Display Name |
| :--- | :--- | :--- | :--- |
| **Sender** (Barista) | `sender1` / `sender2` | `sender123` | Ivan Ivanov / Petr Petrov |
| **Checker** (Manager) | `checker1` | `checker123` | Anna Smirnova |
| **Administrator** | `admin` | `admin123` | System Administrator |

---

## 🧪 Testing

To run unit tests verifying auth, permissions, validation limits (comment >= 10 chars), and mock iiko synchronization:
```bash
python manage.py test
```
