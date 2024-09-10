import boto3

# Initialize S3 client
s3 = boto3.client('s3')


# Function to create a bucket
def create_bucket(bucket_name, region):
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    print(f"Bucket {bucket_name} created successfully")

# Function to upload a file to s3
def upload_file_to_s3(bucket_name, file_path, object_name):
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"File {file_path} uploaded to {bucket_name}/{object_name}")

# Function to list all files in the bucket
def list_files_in_bucket(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print("Files in bucket:")
        for obj in response['Contents']:
            print(f"- {obj['Key']}")
    else:
        print("Bucket is empty")

# Function to download a file from S3
def download_file_from_s3(bucket_name, object_name, download_path):
    s3.download_file(bucket_name, object_name, download_path)

# Function to delete a file from S3
def delete_file_from_s3(bucket_name):
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    print(f"File {object_name} deleted from bucket {bucket_name}")

# Function to delete bucket
def delete_bucket(bucket_name):
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted successfully")


if __name__ == "__main__":
    # Variables
    bucket_name = 'my_unique_bucket_name-123456' # Replace with your unique bucket name
    region = 'us-wes-2'
    file_path ='sample_data/sample_file.csv'
    object_name = 'data/uploaded_file.csv'
    download_path = 'downloaded_file.csv'

    # Create bucket
    create_bucket(bucket_name, region)

    # Upload file to bucket
    upload_file_to_s3(bucket_name, file_path, object_name)

    # List files in the bucket
    list_files_in_bucket(bucket_name)

    # Download file from bucket
    download_file_from_s3(bucket_name, object_name, download_path)

    # Clean up: Delete the uploaded file and the bucket
    delete_file_from_s3(bucket_name, object_name)
    delete_bucket(bucket_name)