# User Management API with Flask

## Introduction

Welcome to the User Management API project. This professional-grade project is designed to provide a robust and scalable user management system using Flask. It includes comprehensive endpoints for creating, retrieving, updating, and deleting users, as well as a health check endpoint. The infrastructure is managed using Terraform, containers are orchestrated with Kubernetes, and a Makefile is used to streamline commands, testing, and linting.

## Features

- **API Endpoints**:
  - `POST /users`: Create a new user.
  - `GET /users`: Retrieve a list of users.
  - `PATCH /users/<id>`: Update an existing user.
  - `DELETE /users/<id>`: Delete a user.
  - `GET /healthcheck`: Check the health status of the API.

- **Infrastructure**:
  - Managed using Terraform for scalable and efficient resource provisioning.

- **Container Orchestration**:
  - Kubernetes for managing and orchestrating containers, ensuring high availability and scalability.

- **Development and Testing**:
  - A Makefile to organize and simplify commands.
  - Integrated testing framework.
  - Code linting with Flake8.
  - Docker for containerized application deployment.

## Getting Started

### Prerequisites

- Docker
- Kubernetes
- Terraform
- Make
- Python 3.x
- Pip

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/bacciotti/restapi-flask.git
    cd restapi-flask
    ```

2. **Set up virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application locally**:
    ```bash
    make deploy-dev
    ```

### Infrastructure Setup

1. **Initialize Terraform**:
    ```bash
    terraform init
    ```

2. **Apply Terraform configuration**:
    ```bash
    terraform apply
    ```

### Kubernetes Deployment

1. **Build Docker image**:
    ```bash
    make build
    ```

2. **Push Docker image to registry**:
    ```bash
    make push
    ```

3. **Deploy to Kubernetes**:
    ```bash
    make deploy
    ```

### Testing and Linting

- **Run tests**:
    ```bash
    make test
    ```


## Contributing

We welcome contributions from the community. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

---

Leverage this User Management API to efficiently manage users in your applications with a scalable and reliable infrastructure. As an experienced professional, you can appreciate the thoughtfulness and best practices integrated into this project.
