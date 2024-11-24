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

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/image-frame-processing-api.git
    cd image-frame-processing-api
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up MongoDB:
    - Install and run MongoDB locally, or create a free MongoDB Atlas cluster and configure the connection string in the environment variables.

5. Run the server:
    ```bash
    python app.py
    ```

## API Endpoints

### 1. **Upload Image Data**

- **Endpoint**: `POST /upload`
- **Description**: Upload a valid CSV file to be processed and stored in MongoDB.
- **Request**:
    - `file`: CSV file containing image data with pixel values from 0 to 255.
- **Response**:
    - Success message confirming upload.

### 2. **Fetch Image Frame by Depth Range**

- **Endpoint**: `GET /frames`
- **Description**: Fetch an image frame by specifying a `depth_min` and `depth_max`.
- **Request**:
    - `depth_min`: The minimum depth value (integer).
    - `depth_max`: The maximum depth value (integer).
- **Response**:
    - A PNG/JPEG image of the resized frame with a custom color map applied.
    - Status code 200 on success.

### 3. **Validate Request/Response Format**

Both request and response validation is handled using Pydantic data models. The request and response are validated against predefined schemas to ensure proper data formats and avoid errors.

## Custom Color Map

A custom color map is applied to the frames before returning the response. The color map is applied using `matplotlib` to give visual structure to the raw pixel values, improving the interpretability of the images.

## Cloud Deployment (Optional)

The solution can be deployed on a cloud platform for scalability. If using Docker, you can create a containerized version of the app and deploy it to cloud platforms like AWS, Google Cloud, or Heroku.

To deploy:

1. Build the Docker image:
    ```bash
    docker build -t image-frame-api .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 image-frame-api
    ```

3. Deploy the app to your preferred cloud service (AWS, GCP, Azure, or Heroku).

## Data Structure

The CSV file contains pixel values with the following format:

| depth | pixel_1 | pixel_2 | ... | pixel_200 |
|-------|---------|---------|-----|-----------|
| 1     | 255     | 128     | ... | 64        |
| 2     | 245     | 130     | ... | 75        |
| ...   | ...     | ...     | ... | ...       |

- `depth`: The depth level of the image frame.
- `pixel_1` to `pixel_200`: The pixel values (0-255) for the corresponding depth.

## Technologies Used

- **Python**: The main programming language used.
- **Flask** (or FastAPI): Web framework for building the API.
- **MongoDB**: Database for storing image data.
- **NumPy**: For numerical operations and image manipulation.
- **Matplotlib**: For color mapping.
- **Pydantic**: For request and response validation.
