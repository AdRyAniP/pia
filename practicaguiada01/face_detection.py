#!/usr/bin/python3
import sys  # Import the sys module to access command-line arguments

import boto3
import os
from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

# Get env variables
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
bucket = os.environ.get('BUCKET_SOURCE')
region = os.environ.get('REGION')

rekognition_client = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey,
    region_name=region).client('rekognition')
print('Debug! yep client created successfully!')


def detect_faces(img):
    try:
        response = rekognition_client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': img}}, Attributes=['DEFAULT'])
        print('Image task recognition has been successfully run')
        return response
    except Exception as e:
        print('An unexpected error was raised recognizing an image:', str(e))
        raise e


# Run the app
if __name__ == "__main__":
    # Check if the user provided an image name as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <image_name>")
        sys.exit(1)
    image_name = sys.argv[1]  # Get the image name from the command-line argument
    image_data = detect_faces(image_name)  # Call the detect_faces function with the image name
    print(image_data)
