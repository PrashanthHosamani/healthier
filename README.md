# Healthcare Backend API

A Healthcare Management Backend built using **Django**, **Django REST Framework (DRF)**, **PostgreSQL**, and **JWT Authentication**.

## Project Overview

This project provides a secure backend system for managing:

- User Authentication
- Patient Records
- Doctor Records
- Patient-Doctor Assignments

The application follows RESTful API principles and uses JWT-based authentication for securing endpoints.

---

## Tech Stack

- Python 3.13.1
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Simple JWT
- Django ORM
- Postman (API Testing)

---

## Features

### Authentication
- User Registration
- User Login
- JWT Access Token
- JWT Refresh Token

### Patient Management
- Create Patient
- Retrieve Patients
- Retrieve Patient Details
- Update Patient
- Delete Patient

### Doctor Management
- Create Doctor
- Retrieve Doctors
- Retrieve Doctor Details
- Update Doctor
- Delete Doctor

### Patient-Doctor Mapping
- Assign Doctor to Patient
- Retrieve All Assignments
- Retrieve Doctors Assigned to a Patient
- Remove Assignment

### Security
- JWT Authentication
- Protected Endpoints
- User-Specific Patient Access

### Validation
- Age Validation
- Phone Number Validation
- Duplicate Mapping Prevention
- Email Uniqueness Validation

---

# Project Structure

```text
Healthier/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── patients/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── doctors/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── PatientDoctorMapping/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── Healthier/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

# Database Design

## User

| Field | Type |
|---------|---------|
| id | Integer |
| full_name | CharField |
| email | EmailField |
| password | Hashed Password |
| created_at | DateTime |
| updated_at | DateTime |

---

## Patient

| Field | Type |
|---------|---------|
| id | Integer |
| name | CharField |
| age | Integer |
| gender | CharField |
| phone | CharField |
| address | TextField |
| created_by | ForeignKey(User) |
| created_at | DateTime |
| updated_at | DateTime |

---

## Doctor

| Field | Type |
|---------|---------|
| id | Integer |
| name | CharField |
| specialization | CharField |
| email | EmailField |
| phone | CharField |
| created_at | DateTime |
| updated_at | DateTime |

---

## PatientDoctorMapping

| Field | Type |
|---------|---------|
| id | Integer |
| patient | ForeignKey(Patient) |
| doctor | ForeignKey(Doctor) |
| assigned_by | ForeignKey(User) |
| assigned_at | DateTime |

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Healthier
```

## Create Virtual Environment

```bash
python -m venv env
```

### Windows

```bash
env\Scripts\activate
```

### macOS/Linux

```bash
source env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DB_NAME=healthier_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

---

# Authentication APIs

## Register User

### Endpoint

```http
POST /api/auth/register/
```

### Request Body

```json
{
    "full_name": "Prashanth Hosamani",
    "email": "prashanth@gmail.com",
    "password": "Password"
}
```

### Response

```json
{
    "user": {
        "id": 1,
        "full_name": "Prashanth Hosamani",
        "email": "prashanth@gmail.com"
    },
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
}
```

---

## Login User

### Endpoint

```http
POST /api/auth/login/
```

### Request Body

```json
{
    "email": "prashanth@gmail.com",
    "password": "Password"
}
```

### Response

```json
{
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
}
```

---

## Refresh Access Token

### Endpoint

```http
POST /api/auth/refresh/
```

### Request Body

```json
{
    "refresh": "jwt_refresh_token"
}
```

---

# Patient APIs

## Create Patient

```http
POST /api/patients/
```

### Request Body

```json
{
    "name": "Manoj",
    "age": 30,
    "gender": "Male",
    "phone": "9876543210",
    "address": "Bangalore"
}
```

---

## Get All Patients

```http
GET /api/patients/
```

Returns all patients created by the authenticated user.

---

## Get Patient Details

```http
GET /api/patients/{id}/
```

---

## Update Patient

```http
PUT /api/patients/{id}/
```

---

## Delete Patient

```http
DELETE /api/patients/{id}/
```

---

# Doctor APIs

## Create Doctor

```http
POST /api/doctors/
```

### Request Body

```json
{
    "name": "Dr Sharma",
    "specialization": "Cardiology",
    "email": "drsharma@test.com",
    "phone": "9876543210"
}
```

---

## Get All Doctors

```http
GET /api/doctors/
```

---

## Get Doctor Details

```http
GET /api/doctors/{id}/
```

---

## Update Doctor

```http
PUT /api/doctors/{id}/
```

---

## Delete Doctor

```http
DELETE /api/doctors/{id}/
```

---

# Patient-Doctor Mapping APIs

## Assign Doctor to Patient

### Endpoint

```http
POST /api/mappings/
```

### Request Body

```json
{
    "patient": 1,
    "doctor": 1
}
```

---

## Get All Mappings

```http
GET /api/mappings/
```

---

## Get Doctors Assigned to a Patient

### Endpoint

```http
GET /api/mappings/?patient=1
```

---

## Remove Doctor Assignment

### Endpoint

```http
DELETE /api/mappings/{id}/
```

---

# Authentication

All protected endpoints require:

```http
Authorization: Bearer <access_token>
```

---

# Validation Rules

## Patient Validation

- Name must contain at least 2 characters
- Age must be greater than 0
- Age cannot exceed 120
- Phone number must contain exactly 10 digits
- Address cannot be empty

## Doctor Validation

- Name must contain at least 2 characters
- Specialization is required
- Email must be unique
- Phone number must contain exactly 10 digits

## Mapping Validation

- Duplicate patient-doctor assignments are not allowed

---

# Testing

All APIs were tested using Postman.

### Authentication

- User Registration
- User Login
- JWT Token Generation
- JWT Token Refresh

### Patient APIs

- Create Patient
- Retrieve Patient List
- Retrieve Patient Details
- Update Patient
- Delete Patient
- Validation Testing

### Doctor APIs

- Create Doctor
- Retrieve Doctor List
- Retrieve Doctor Details
- Update Doctor
- Delete Doctor
- Validation Testing

### Patient-Doctor Mapping

- Assign Doctor to Patient
- Retrieve Mappings
- Retrieve Doctors Assigned to a Patient
- Remove Mapping
- Duplicate Assignment Prevention

### Security Testing

- Unauthorized Access
- JWT Authentication
- User-Specific Patient Retrieval

---

# Future Improvements

- Swagger/OpenAPI Documentation
- Role-Based Access Control (Admin, Doctor, Receptionist)
- Pagination
- Search and Filtering
- Medical Records Module
- Appointment Scheduling
- Docker Support
- CI/CD Pipeline

