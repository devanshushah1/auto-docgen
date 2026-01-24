# API Documentation Generator

This project automatically generates API documentation in OpenAPI format from a Python Flask application. It uses static analysis to parse the source code and a large language model to generate descriptions and examples for each endpoint.

## Features

-   **Automatic Endpoint Discovery:** Parses Flask application code to find all API endpoints.
-   **OpenAPI Specification Generation:** Creates an `openapi.json` file with the documentation.
-   **AI-Powered Descriptions:** Uses a Hugging Face model to generate descriptions and `curl` examples for each endpoint.
-   **Extensible:** Can be adapted to support other web frameworks and documentation formats.

## How it Works

The documentation generation process works in three main steps:

1.  **Parsing:** The `parser.py` script reads the `app.py` file, which contains the Flask application. It uses Python's `ast` (Abstract Syntax Tree) and `inspect` modules to identify the routes, HTTP methods, and the source code of the functions that handle the endpoints.

2.  **Generation:** The `generate_docs.py` script takes the parsed endpoint information and, for each endpoint, sends a request to a Hugging Face Inference API. The prompt includes the endpoint's path, method, and source code. The language model then returns a JSON object containing a description and a `curl` example for the endpoint, formatted as an OpenAPI path fragment.

3.  **Output:** The generated OpenAPI fragments are combined into a single `docs/openapi.json` file. This file can then be used with tools like Swagger UI or Redoc to display the API documentation.

## Project Structure

```
.
├── .gitignore
├── app.py              # The example Flask application
├── generate_docs.py    # The main script to generate the documentation
├── parser.py           # The script that parses the Flask application
└── docs/
    ├── api.md          # (Optional) Markdown documentation
    ├── index.html      # (Optional) HTML documentation viewer
    └── openapi.json    # The generated OpenAPI specification
```

## Getting Started

### Prerequisites

-   Python 3.6+
-   A Hugging Face API token

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/api-docgen.git
    cd api-docgen
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set your Hugging Face API token as an environment variable:
    ```bash
    export HF_TOKEN="your-hugging-face-token"
    ```

### Usage

1.  Run the `generate_docs.py` script:
    ```bash
    python generate_docs.py
    ```

2.  The generated documentation will be saved in `docs/openapi.json`.

3.  You can view the documentation using a tool like [Swagger Editor](https://editor.swagger.io/) or by serving the `docs` directory with a local web server.