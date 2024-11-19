# Django REST API with Docker for Machine Test

## Project Description
This project implements a Django-based REST API system with Docker to manage three entities: `User`, `Client`, and `Project`. The system allows for client and project management, user assignments to projects, and querying the assigned projects for a logged-in user. This project showcases the ability to manage large-scale data and interactions between clients, projects, and users.

## Features
- **Register a client**: Create and manage clients in the system.
- **Fetch client information**: Retrieve details of clients, including associated projects.
- **Edit/Delete client information**: Modify or remove clients from the system.
- **Add new projects for a client**: Create projects and assign users to those projects.
- **Retrieve assigned projects for logged-in users**: Fetch the list of projects assigned to the currently authenticated user.

## Tech Stack
- **Django**: Backend framework for the API.
- **PostgreSQL**: Database for storing data related to users, clients, and projects.
- **Docker**: Containerization tool for creating a consistent development environment.
- **Docker Compose**: Used for orchestrating multiple containers, including the Django app and database.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-machine-test.git
cd django-machine-test

<h2>Running the Project with Docker</h2>
    <p>This project is containerized using Docker. To run the project in a containerized environment, follow these steps:</p>
    <ul>
        <li>Ensure you have Docker and Docker Compose installed on your system.</li>
        <li>Build the containers using the command: <code>docker-compose build</code></li>
        <li>Start the application with: <code>docker-compose up</code></li>
        <li>The application will run at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>.</li>
    </ul>
