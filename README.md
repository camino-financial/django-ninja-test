# Django Ninja API Test Project

This is a lightweight Django application built with Django Ninja, a framework for building REST APIs with Django. The project demonstrates how to build a simple API with Django Ninja, and includes test coverage measurement with pytest and coverage.

## Features

- Django REST API using Django Ninja
- API documentation with Swagger UI
- Comprehensive test coverage
- Dockerized development environment

## Requirements

- Docker and Docker Compose
- Git

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/camino-financial/django-ninja-test
cd django-ninja-test
```

### 2. Start the application with Docker

This will:
- Build the Docker image
- Install all dependencies
- Start the Django development server on port 8000

```bash
docker-compose up -d
```

### 3. Access the API

Once the server is running, you can access:
- API endpoints at http://localhost:8000/
- API documentation at http://localhost:8000/docs

## Available API Endpoints

- `/hello_world` - Returns a greeting message
- `/ping` - Simple health check endpoint (returns "pong")

## Running Tests

The project uses pytest with pytest-django for testing. To run the tests inside the Docker container:

```bash
# First, make sure your Docker container is running
docker-compose up -d

# Then execute the tests inside the container
docker-compose exec -it api pytest
```

For more detailed test information with coverage reports:

```bash
docker-compose exec -it api pytest -s -x --cov --cov-report=term
```

This will display:
- Test results
- Code coverage statistics

## Project Structure

```
django-ninja-test/
├── app/                    # Main application
│   ├── api.py              # API endpoints definitions
│   ├── schemas.py          # Pydantic schemas for API
│   └── tests.py            # Test cases
├── base_app/               # Django project settings
│   ├── api.py              # Main Ninja API instance
│   ├── settings.py         # Django settings
│   └── urls.py             # URL routing
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker build instructions
├── manage.py               # Django management script
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
└── .coveragerc             # Coverage configuration
```

## Development

To develop locally with Docker:

1. Start the Docker container: `docker-compose up -d`
2. Make changes to the code (the changes will be reflected automatically due to volume mounting)
3. Run tests to verify: `docker compose exec -it api pytest`

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality and consistency before committing changes.

### Installation

1. Install pre-commit locally:
```bash
pip install pre-commit
```

2. Install the git hooks:
```bash
pre-commit install
```

### Usage

After installation, pre-commit hooks will run automatically on every commit. To run them manually on all files:

```bash
pre-commit run --all-files
```

Always run pre-commit hooks before pushing your changes to ensure your code meets the project's quality standards.

## License

MIT License
