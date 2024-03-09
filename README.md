
# Docker Ecosystem Setup for Airflow 

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Docker Desktop
- Git (optional, for version control)
- dbeaver (Optional, for connecting to postgres DWH)

## Overview

Our ecosystem consists of:
- **Apache Airflow**: An open-source platform to programmatically author, schedule, and monitor workflows.
- **PostgreSQL**: An open-source relational database system for data storage.

## Structure

- `Dockerfile-airflow`: Defines the Airflow service container.
- `docker-compose.yaml`: Orchestrates the setup, linking Airflow (Scheduler, Webserver) and PostgreSQL databases.
- `requirements.txt`: Lists Python dependencies.

## Setup Instructions

### 1. Clone the Repository

(Optional) If you're using Git, clone this repository to get the latest version of the setup files.

```
git clone git@github.com:krshillman/tut_docker_setup.git
cd tut_docker_setup
```

### 2. Build and Run with Docker Compose

Navigate to the project directory where `docker-compose.yaml` is located and run:

```
docker-compose build
docker-compose up --build
```

This command builds the Docker images for Airflow, and sets up PostgreSQL databases, and starts the services.

### 3. Accessing the Services

- **Airflow**: Visit `http://localhost:8080` in your browser to access the Airflow web interface.

### 4. Shutting Down

To stop and remove the containers, networks, and volumes created by `docker-compose`, run:

```
docker-compose down
```

## Additional Resources

For more information on Docker, Docker Compose, Airflow, Flask, and PostgreSQL, please refer to their official documentation:

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Flask Documentation](http://flask.pocoo.org/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## Troubleshooting

- Ensure Docker and Docker Compose are correctly installed and up to date.
- Check container logs for errors if a service fails to start.


