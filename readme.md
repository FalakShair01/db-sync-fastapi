
---

# FastAPI Database Synchronization

## Overview
This project demonstrates how to build a FastAPI microservice for synchronizing subscription status between two databases using SQLAlchemy for database interactions. The microservice periodically checks for inactive subscriptions in one database and updates them based on the status in another database.

This project targets scenarios where real-time or periodic synchronization of data between databases is necessary, such as maintaining consistency across distributed systems or updating secondary databases with information from a primary source.


## Project Structure
The project has the following directory structure:
```
project_directory/
│
├── database/
│   └── db.py
│
├── models/
│   ├── __init__.py
│   ├── subscription1.py
│   └── subscription2.py
│
├── tasks.py
├── __init__.py
├── main.py
└── requirements.txt
```

- **database/db.py**: Contains SQLAlchemy setup including database URL, engine, and session maker.
- **models/subscription1.py**: Contains the Subscription1 model representing the subscription table of database 1.
- **models/subscription2.py**: Contains the Subscription2 model representing the subscription table of database 2.
- **tasks.py**: Contains the logic for synchronizing subscription status between databases.
- **__init__.py**: Initializes the app module.
- **main.py**: Entry point of the FastAPI application.
- **requirements.txt**: Contains the project dependencies.

## Setup Instructions
1. Clone the repository:
    ```
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```
    cd project_directory
    ```
3. Create a virtual environment (optional but recommended):
    ```
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```
5. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Running the Application
1. Navigate to the app directory:
    ```
    cd app
    ```
2. Run the FastAPI application:
    ```
    uvicorn main:app --reload
    ```
3. Access the Swagger UI to interact with the API:
    ```
    http://127.0.0.1:8000/docs
    ```

## Workflow
1. The FastAPI application starts when the main module (`main.py`) is executed.
2. On startup, the application initializes the database and schedules the synchronization task using `tasks.schedule_sync_task()` defined in `tasks.py`.
3. The synchronization task (`tasks.sync_subscriptions()`) runs periodically based on the specified interval.
4. The task fetches inactive subscriptions from one database and checks their status in another database using SQLAlchemy queries.
5. If the status in the second database is active, the subscription status is updated accordingly.
6. The changes are committed to the database, and the session is closed.


### Key Features:

- **FastAPI Framework**: Utilizes FastAPI, a modern Python web framework known for its high performance and simplicity in building APIs.
  
- **SQLAlchemy Integration**: Integrates SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library for database interactions, allowing seamless communication with databases.
  
- **Database Synchronization**: Implements a background task to periodically synchronize subscription status between two databases, ensuring consistency across systems. This involves filtering inactive subscriptions from one database and updating their status in another database based on certain conditions.
  
- **Asynchronous Task Scheduling**: Utilizes APScheduler to schedule asynchronous tasks for periodic synchronization, enabling efficient and non-blocking execution without affecting API responsiveness.
  
- **Mock Data and Testing**: Provides mock data and endpoints for testing subscription status updates and synchronization functionality, ensuring reliability and robustness of the microservice.


## Contributors
- [Falak Shair](mailto:falakshair563@gmail.com)

---
