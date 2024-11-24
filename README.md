# Image Frame Processing and API Service

This repository provides a solution for processing image data contained in a CSV file, resizing the images, storing them in a MongoDB database, and providing an API for fetching and uploading image frames based on a depth range. Additionally, custom color mapping is applied to the frames before serving them.

## Overview

The challenge involves the following:

- **Image Data**: The image data is provided in a CSV file, with each row representing pixel values for an image at a specific depth. The columns represent pixel values (0-255) at different depths.
- **Resizing**: The image width is resized from 200 pixels to 150 pixels.
- **Database**: The resized images are stored in MongoDB.
- **APIs**: 
  - An API to fetch image frames based on `depth_min` and `depth_max`.
  - An API for uploading image data from a valid CSV file into the MongoDB database.
- **Color Map**: A custom color map is applied to the image frames before returning them.
- **Bonus**: The solution can be deployed to a cloud service for scalability.

## Requirements

- Python 3.11.x
- Flask (or FastAPI, if preferred for deployment)
- MongoDB (locally or in a cloud service like MongoDB Atlas)
- NumPy
- Matplotlib
- Pydantic (for data validation)
- Docker (optional, for cloud deployment)


## Prerequisites


1. Clone the repository:
    ```bash
    git clone https://github.com/Alvi-Rahman/OpenInnovationAI.git
    cd OpenInnovationAI
    ```

2. Make sure MongoDB is up and running on PORT `27017`
3. Make Sure Python `3.11.x+` is installed locally
4. Create a Database named `OpenInnovationAIImageDB`
5. Rename the `.env.txt` to `.env`


## Installation (Locally with Docker)
To set up the project locally with Docker, follow these steps:


To set up the project locally, follow these steps:

1. Make sure you have Docker installed and running in your local
2. run
```bash
docker-compose up
```


## Installation (Locally without Docker)

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up MongoDB:
    - Install and run MongoDB locally, or create a free MongoDB Atlas cluster and configure the connection string in the environment variables.

4. Run the server:
    ```bash
    python app.py
    ```

## API Endpoints

### 1. **Upload Image Data**

- **Endpoint**: `POST /upload`

### 2. **Fetch Image Frame by Depth Range**

- **Endpoint**: `GET /frames`

## Deployment to the Cloud (AWS)

- Create a DocumentDB instance on AWS
- Test the connection and create the DB as mentioned earlier
- Then create a ELB application with necessary permissions and credentials
- Install `aws` CLI and use `aws configure` to set configurations (Can also use `SSO`)
- cd to project
- run the following
```bash
eb init -p docker <application-name>
eb create <environment-name>
```

## Tests

This project includes some tests which might be helpful in terms of showcasing
TDD lifecycle flow

RUN the following command to run the tests (after activating `virtualenv`)

```bash
 python3 -m pytest
```

`python3 -m` is used to make sure we use the active python interpreter

## Technologies Used

- **Python**: The main programming language used.
- **Flask** (or FastAPI): Web framework for building the API.
- **MongoDB**: Database for storing image data.
- **NumPy**: For numerical operations and image manipulation.
- **Matplotlib**: For color mapping.
- **Pydantic**: For request and response validation.
