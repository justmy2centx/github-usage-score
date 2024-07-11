# GitHub Usage Score

This project calculates a GitHub usage score based on user events from the GitHub public user events API.

## Directory Structure
```
github-usage-score/
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
└── src/
    └── github_usage_score.py
```

## Prerequisites

- Docker installed on your machine.
- Python 3.x (if running the script locally).

## Setup and Usage

### Running with Docker

1. **Build the Docker image:**

   ```sh
   docker build -t github-usage-score .
   ```
    The default values in the docker-compose.yml file are:

    ```sh
    GITHUB_USERNAME=josevalim
    USE_SAMPLE_PAYLOAD=true
    ```

    To override these values, you can set environment variables in the docker-compose.yml file.

2. **Run the Docker container:**
    ```
    docker run --rm -e GITHUB_USERNAME=your-github-username github-usage-score 
    ```

    To run the Docker container and use the sample payload with `docker-compose`:

    ```sh
    docker-compose up --build
    ```


## Running Locally
    
    pip install -r requirements.txt
    GITHUB_USERNAME=your-github-username python src/github_usage_score.py
   