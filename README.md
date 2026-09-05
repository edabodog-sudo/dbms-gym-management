# Gym Management System

## Description

The Gym Management System is a database-backed application developed for the
Introduction to Database Management Systems (DBMS_10) course.

The application allows the management of:

- Members
- Courses
- Registrations
- Payments

The frontend communicates with a FastAPI backend using HTTP. Write operations
are protected by an X-API-Key. The backend stores the application data in a
PostgreSQL database.

## Architecture

Frontend (.deb)
      |
      | HTTP + X-API-Key
      v
FastAPI Backend
      |
      v
PostgreSQL Database

The FastAPI backend and PostgreSQL database are orchestrated using Docker
Compose.

## Technologies

- PostgreSQL 16
- FastAPI
- SQLAlchemy
- Python
- Docker
- Docker Compose
- HTML
- CSS
- JavaScript
- Debian package (.deb)
- LaTeX
- GitHub Actions

## Project Structure

dbms10-gym-management/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── packaging/
├── tests/
├── docs/
├── docker-compose.yml
└── README.md

## Environment Configuration

Create a .env file in the project root.

Example:

POSTGRES_DB=gymdb
POSTGRES_USER=gymuser
POSTGRES_PASSWORD=gympassword

DATABASE_URL=postgresql+psycopg://gymuser:gympassword@db:5432/gymdb

API_KEY=gym-secret-key

The .env file is ignored by Git and must not be committed to the repository.

## Start the Backend

From the project root, run:

docker compose up -d

Check the containers:

docker compose ps

The FastAPI backend is available at:

http://localhost:8000

The Swagger API documentation is available at:

http://localhost:8000/docs

## Frontend

The frontend is packaged as a Debian package.

Install it with:

sudo dpkg -i packaging/gym-management-frontend.deb

The frontend files are installed in:

/usr/share/gym-management

For local testing, start a web server:

cd /usr/share/gym-management
python3 -m http.server 8080

Then open:

http://localhost:8080

## API Security

Write operations such as POST, PUT and DELETE are protected using the
X-API-Key HTTP header.

Read operations can be performed without the API key.

## Main Functions

### Members

Members can be created, displayed, updated and deleted.

### Courses

Courses can be created, displayed, updated and deleted.

### Registrations

Members can be registered for courses. Registrations connect members and
courses using their database IDs.

### Payments

Payments are associated with members and contain an amount and payment date.

## Tests

API tests are located in:

tests/test_api.py

## Documentation

The project documentation is written in LaTeX and located in:

docs/

To build the documentation:

cd docs
make

The GitHub Actions workflow automatically builds the documentation. Tagged
versions can be published as GitHub Releases with the generated PDF.

## Author

DBMS_10 Term Project  
THGA Bochum
