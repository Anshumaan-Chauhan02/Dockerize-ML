# Use Python base image from Docker Hub
FROM python:3.11

# Create and move to a new working space directory 
WORKDIR /ml-app

# Copy contents
COPY . .

# Install all the necessary libraries required
RUN pip install -r requirements.txt

# Train the model 
RUN python iris-classification.py 

# Use the trained model for prediction
CMD ["python", "model_prediction.py"]