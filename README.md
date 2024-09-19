## Mem0 API

## Table of Contents

- Introduction
- Features
- Installation
- Usage
- Configuration
- [API Endpoints](#api-endpoints)
- Testing
- License
- Contributing

## Introduction

This project is a FastAPI-based application designed for managing memory-related operations. It leverages various technologies such as OpenAI, Qdrant, and Neo4j to provide a robust and scalable solution for memory management.

## Features

- **Add Memory**: Add new memory entries.
- **Search Memory**: Search through existing memory entries.
- **Fetch All Memory**: Retrieve all memory entries for a user.
- **Delete All Memory**: Delete all memory entries for a user.

## Installation

### Prerequisites

- Python 3.11
- Docker (optional, for containerized deployment)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/Aftar-Ahmad-Sami/mem0-api.git
    cd mem0-api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables by creating a [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Fmem0-api%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22c1230bea-106f-4b8e-82fc-474c6a37e84d%22%5D "/workspaces/mem0-api/.env") file:
    ```properties
    OPENAI_API_KEY=your_openai_api_key
    NEO4J_PASSWORD=your_neo4j_password
    NEO4J_URL=your_neo4j_url
    NEO4J_USERNAME=your_neo4j_username
    USER_ID=your_user_id
    QDRANT_API_KEY=your_qdrant_api_key
    QDRANT_COLLECTION=your_qdrant_collection
    QDRANT_URL=your_qdrant_url
    ```

## Usage

### Running the Application

To run the application locally:

```sh
uvicorn app.main:app --reload
```

To run the application using Docker:

1. Build the Docker image:
    ```sh
    docker build -t mem0-api .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8000:8000 --env-file .env mem0-api
    ```

### Accessing the Application

Once the application is running, you can access it at `http://localhost:8000`.

## Configuration

The application uses environment variables for configuration. These variables are loaded from a [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Fmem0-api%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22c1230bea-106f-4b8e-82fc-474c6a37e84d%22%5D "/workspaces/mem0-api/.env") file. Refer to the [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Fmem0-api%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22c1230bea-106f-4b8e-82fc-474c6a37e84d%22%5D "/workspaces/mem0-api/.env") example in the Installation section.

## API Endpoints

- **GET /**: Returns a welcome message.
- **POST /api/add**: Adds a new memory entry.
- **POST /api/search**: Searches for memory entries.
- **POST /api/get_all**: Fetches all memory entries for a user.
- **DELETE /api/delete_all**: Deletes all memory entries for a user.

## Testing

To run the tests, use the following command:

```sh
pytest
```

## License

This project is licensed under the Apache License 2.0. See the [`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Fmem0-api%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22c1230bea-106f-4b8e-82fc-474c6a37e84d%22%5D "/workspaces/mem0-api/LICENSE") file for details.

## Contributing

Contributions are welcome!