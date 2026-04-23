# 🏃 MySCRUM

**Free and open-source project management tool built on the Scrum framework.**

MySCRUM helps teams plan, track and deliver software projects with sprints, task boards and gamified performance — all without paying for expensive SaaS tools.

---

## Documentação
- [Diagrama ER](docs\er-diagram.md)

## ✨ Features

- 📋 **Sprint management** — create and manage sprints with backlog, in progress and done columns
- 👤 **User authentication** — secure login, registration and permission control
- 📊 **Dashboard & reports** — visual overview of sprint progress and team performance
- 🔌 **REST API** — programmatic access to projects and tasks
- 🏆 **Gamification** — teams earn points and badges based on sprint results, keeping motivation high

---

## 🛠 Tech Stack

- **Backend:** Python 3.13+, Django
- **Database:** PostgreSQL
- **Dependency management:** Poetry
- **Auth:** Django built-in authentication

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gcileno/myscrun.git
cd myscrun
```

### 2. Set up environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Required variables: PostgreSQL connection, Django secret key, and any others listed in `.env.example`.

### 3. Install dependencies

```bash
poetry install
```

### 4. Run database migrations

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

### 5. Create a superuser

```bash
poetry run python manage.py createsuperuser
```

### 6. Start the development server

```bash
poetry run python manage.py runserver
```

Access the app at `http://localhost:8000`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built by [Gabriel Cileno](https://github.com/gcileno)*
