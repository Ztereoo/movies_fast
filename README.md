
# Movies FastAPI Project

This is a **FastAPI-based API** that allows users to submit and retrieve **movie reviews**, including ratings and comments. 

## **Features**
- **User Authentication**: Custom JWT authentication system.
- **Async Operations**: Efficient asynchronous functions using FastAPI.
- **Database**: SQLite with asynchronous support, managed using Alembic for migrations.
- **Caching**: Redis used for caching frequently accessed data.
- **Task Management**: Celery for background tasks, visualized with Flower.
- **Admin Panel**: Web-based admin panel powered by SQLAdmin.
- **Logging tools**: python-json-logger with Sentry visualisation.
- **Containerization**: Docker and Docker Compose for easy deployment.
- **Testing**: Unit tests using Pytest.

## **Installation**

### **Requirements**
- Python 3.9+
- Docker (optional, for containerization)

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/Ztereoo/movies_fast.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

4. For Docker setup, use:
   ```bash
   docker-compose up --build
   ```

## **Endpoints**

1. **POST /login**
   - **Description**: Login for users.
   - **Body**: JSON with username and password.
   - **Returns**: JWT token.

2. **POST /movies**
   - **Description**: Submit a movie review (rating and comment).
   - **Body**: JSON with movie_name, rating, and comment.

3. **GET /movies/{movie_id}**
   - **Description**: Retrieve a movie's review.
   - **Returns**: JSON with the movie's rating and comments.

## **Testing**
Run the tests using **Pytest**:
```bash
pytest
```

## **Docker**
To build and run the app in Docker containers:
```bash
docker-compose up --build
```

## **License**
This project is licensed under the **Apache-2.0 License** - see the LICENSE.txt file for details.

## **Acknowledgments**
- **FastAPI** for the base framework.
- **Redis** and **Celery** for caching and background task management.
- **SQLAlchemy** for database interactions.







