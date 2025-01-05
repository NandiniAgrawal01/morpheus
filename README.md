
# Form Builder Project

## Overview

This project is a web-based form builder application that allows users to create dynamic forms by adding various types of fields. The form builder has an admin interface to manage forms and their fields, and it stores submitted data for each created form. The project is built using Django for the backend and React for the frontend.

## Project Structure

- **Backend (Django)**: Handles API requests, form and field management, and stores form submissions.
- **Frontend (React)**: Provides a drag-and-drop interface for building forms and interacting with the Django API.

---

## Setup Instructions

### 1. Clone the repository

Clone the repository from GitHub:

```bash
git clone https://github.com/yourusername/formbuilder
```

### 2. Set up the backend (Django)

#### 2.1. Install Python dependencies

Navigate to the backend directory and install the necessary Python packages:

```bash
cd formbuilder
pip install -r requirements.txt
```

#### 2.2. Apply database migrations

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

#### 2.3. Collect static files (if needed)

To collect static files for the Django app:

```bash
python manage.py collectstatic
```

#### 2.4. Start the Django development server

Start the Django backend by running the following command:

```bash
python manage.py runserver
```

The backend server will run at `http://127.0.0.1:8000`.

---

### 3. Set up the frontend (React)

If your project uses a separate frontend built with React, follow these steps:

#### 3.1. Install Node.js dependencies

Navigate to the `frontend` directory and install the required dependencies:

```bash
cd frontend
npm install
```

#### 3.2. Start the React development server

Run the following command to start the React development server:

```bash
npm start
```

The frontend will run at `http://localhost:3000`.

---

## Usage Guide

- **Backend (Django)**: Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to interact with the Django API. You can use Postman or any API testing tool to make GET, POST, PATCH, and DELETE requests for managing forms and fields.
  
- **Frontend (React)**: Open your browser and go to [http://localhost:3000](http://localhost:3000). This will open the form builder UI where you can create and manage forms using a drag-and-drop interface.

---

## API Documentation

### API Endpoints

- **GET /api/forms/**: Retrieve all forms.
- **POST /api/forms/**: Create a new form.
- **GET /api/forms/{form_id}/fields/**: Retrieve fields for a specific form.
- **POST /api/fields/**: Add a new field to a form.
- **PATCH /api/fields/{field_id}/**: Update a field's properties (e.g., reordering fields).
- **DELETE /api/forms/{form_id}/**: Delete a form.

---

## Testing the Application

1. **Form Creation**: Use the frontend interface to drag and drop different types of fields (e.g., text, number, date) and create a form.
2. **Form Submission**: Once the form is created, submit it via the frontend. The data will be stored in the backend.
3. **API Testing**: You can use tools like Postman or CURL to test API endpoints like creating forms, retrieving fields, and submitting form data.

---

## Assumptions

- The project assumes you have Node.js and Python installed on your local system.
- The database is set up using Django's default database (SQLite, or configure a different DB if needed).
- The React frontend is independent of the Django server and can run on a different port (usually `3000`).
  
---

## Additional Notes

- The project uses a drag-and-drop interface on the frontend for adding fields to forms.
- The backend stores form data and field properties like type, order, and label.
- You can extend the form builder by adding additional field types (e.g., radio buttons, checkboxes) or customization options.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
