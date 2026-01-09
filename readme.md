# Enterprise Project – Authentication System

This project is a **FastAPI-based authentication system** with **role-based access control**. It provides secure user registration, login, JWT authentication, and admin functionalities.

---

## 1. Introduction
The system allows users to register, login, and access protected routes using JWT tokens. Admin users have additional privileges to access admin-specific APIs. The backend is built with **FastAPI** and uses **SQLite** for data storage.

---

## 2. Technology Stack
- **Backend Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT (JSON Web Token)  
- **Server:** Uvicorn  

---

## 3. Features
- **User Registration** – New users can sign up with email and password.  
- **Login** – Registered users can login to get access tokens.  
- **JWT Token Authentication** – Secure access to protected routes.  
- **Role-Based Access Control** – Users and admin roles with different permissions.  
- **Admin API** – Admin-specific endpoints to manage or monitor the system.  

---

## 4. System Flow
```text
User registers → User logs in → Receives JWT token → Accesses protected routes → Admin accesses admin APIs
