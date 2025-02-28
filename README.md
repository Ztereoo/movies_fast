This is a FastAPI-based API that allows users to submit and retrieve movie reviews, including ratings and comments. 
The project incorporates several libraries and tools to enhance its functionality, including authentication, caching, 
task management, and containerization.

Features
User Authentication: Custom JWT authentication system.
Async Operations: Efficient asynchronous functions using FastAPI.
Database: SQLite with asynchronous support, managed using Alembic for migrations.
Caching: Redis used for caching frequently accessed data.
Task Management: Celery for background tasks, visualized with Flower.
Admin Panel: Web-based admin panel powered by SQLAdmin.
Logging tools: python-json-logger with Sentry visualisation.
Containerization: Docker and Docker Compose for easy deployment.
Testing: Unit tests using Pytest.


Installation
Requirements
Python 3.9+
Docker (optional, for containerization)
Setup
Clone the repository:
git clone https://github.com/Ztereoo/movies_fast.git

Install the dependencies:
pip install -r requirements.txt

Run the application:
uvicorn app.main:app --reload

For Docker setup, use:
docker-compose up --build

Endpoints
1. POST /login
Description: Login for users.
Body: JSON with username and password.
Returns: JWT token.
2. POST /movies
Description: Submit a movie review (rating and comment).
Body: JSON with movie_name, rating, and comment.
3. GET /movies/{movie_id}
Description: Retrieve a movie's review.
Returns: JSON with the movie's rating and comments.
Configuration
JWT Secret Key: Set in config.py for authentication.
Redis: Used for caching; configure in redis.py.
4. 
Testing
Run the tests using Pytest:
pytest

Docker
To build and run the app in Docker containers:
docker-compose up --build
Docker Compose File
Defines services for FastAPI app, Redis, and a SQlite database.
License
This project is licensed under the Apache-2.0 License - see the LICENSE.txt file for details.

Acknowledgments
FastAPI for the base framework.
Redis and Celery for caching and background task management.
SQLAlchemy for database interactions.








This is a FastApi test project.
API gives movies rating and comments,
with users authorisation and authentication.

While working on a project it was the idea to work and practice with several 
libraries and tools such as:
-fastapi async functions
-custom authentication based on JWT
-pydantic models
-alembic versions
-async sqlite
-testing with Pytest
-caching with Redis
-tasks creating and visualisation with Celery and Flower
-web admin creating with SQLadmin
-Docker and docker compose containerization
-Github working