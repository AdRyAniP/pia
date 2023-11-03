#!/usr/bin/python3
import os

from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()
# Get env variables
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
bucket = os.environ.get('BUCKET_SOURCE')
bucket_dest = os.environ.get('BUCKET_DESTINATION')
region = os.environ.get('REGION')

# Run the app
if __name__ == "__main__":
    # Printing all .env data
    print(accessKeyId, secretKey, bucket, bucket_dest, region)
