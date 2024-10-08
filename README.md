# AWS S3 Hands-On Practice

This project demonstrates how to interact with AWS S3 using Python and the `boto3` library. It covers how to:
- Create an S3 bucket
- Upload files to the bucket
- List files in the bucket
- Download files from the bucket
- Clean up resources (delete files and bucket)

## Prerequisites

- Python 3.6+
- AWS Account with access credentials (Make sure to use AWS Free Tier to avoid costs)
- AWS CLI configured (optional, but recommended for easier credential management)

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/martelosso/aws-s3-hands-on.git
    cd aws-s3-hands-on
    ```

2. **Install dependencies**
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. **SEt up AWS credentials**
    Ensure your AWS credentials are set up either via the AWS CLI (`aws configure`) or by setting environment variables:
    ```bash
    export AWS_ACCESS_KEY_ID=your-access-key-id
    export AWS_SECRET_ACCESS_KEY=your-secret-access-key
    export AWS_DEFAULT_REGION=your-region
    ```
4. **Run the script:**
    ```bash
    python s3_example.py
    ```

## Project Structure

- `s3_example.py`: Python script to interact with S3.
- `sample_data/sample_file.csv`: Sample file to test uploading to S3

## Disclaimer

This project uses AWS S3 Free Tier to avoid costs. Make sure to monitor your usage and delete resources after use to avoid charges.