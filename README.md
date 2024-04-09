# FastAPI Library Management System

This project implements a Library Management System API using FastAPI and MongoDB. It provides endpoints for creating, reading, updating, and deleting student records in the system.

## Installation


1. If you want to learn locally then Clone the repository:

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   
2. Install the Dependencies mentioned in requirements.txt
   ```pip install -r requirements.txt```
   
## Usage
- The API will be available at https://library-management-api-yqg9.onrender.com/
- Or you can run locally by following these steps : 
- Start the FastAPI server:

```uvicorn main:app --reload```
- The API will be available at http://127.0.0.1:8000/students.

Use an API testing tool like Thunder Client or Postman to interact with the API.

## API Endpoints
- POST /students: Create a new student record.
- GET /students: Get a list of students with optional filters for country and minimum age.
- GET /students/{id}: Get a student record by ID.
- PATCH /students/{id}: Update a student record.
- DELETE /students/{id}: Delete a student record.

  
