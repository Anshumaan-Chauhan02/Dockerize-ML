# Dockerize-ML

## Overview
This project focuses on containerizing a Machine Learning (ML) application, specifically addressing the tasks of both training and deploying a Machine Learning Model.

## Machine Learning Model
The ML application utilizes a Decision Tree for classification purposes. The model is trained on the well-known [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html). Subsequently, the trained model is employed to make predictions based on user-provided values for sepal and petal width and height, which are the four parameters present in the dataset.

## Installation
To run the Dockerized ML application, follow the steps below:

1. Install [Python](https://www.python.org/downloads/)
   - Recommended version: `3.11.4`
   
2. Install [Docker](https://docs.docker.com/engine/install/)

3. Clone the repository using the following command:
    - `git clone https://github.com/Anshumaan-Chauhan02/Dockerize-ML`

4. Navigate to the cloned local repository:
    - `cd Dockerize-ML`

5. Build the Docker image:
    - `docker build -t dockerize-ml .`

6. Start and run a Docker container:
    - `docker run -it --name docker_container dockerize-ml`

7. Enter the required parameters to receive predictions.

## Usage
Once the Docker container is up and running, input the relevant parameters for sepal and petal width and height. The application will provide predictions based on the trained Decision Tree model.

## Acknowledgments
- The ML model is trained on the [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).
- Special thanks to the contributors who made this project possible.

Feel free to explore, contribute, and use this Dockerized ML application for your Machine Learning endeavors!
