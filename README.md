# Create the README.md content based on the project structure
readme_content = """# PSUSphere

This project is a Django-based application configured to run within a Docker container.

## Prerequisites
* Docker installed on your machine.

## Setup Instructions

### 1. Build the Docker Image
Navigate to the root directory of the project (where `Dockerfile` and `requirements.txt` are located) and run the following command to build the image:
```bash
docker build -t psusphere .
