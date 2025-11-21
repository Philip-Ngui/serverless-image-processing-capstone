# Serverless Image Processing Pipeline

## Project Overview
This project implements a serverless image processing pipeline using AWS services. The architecture processes files between S3 buckets via API Gateway and Lambda functions.

## Architecture
The application follows a serverless architecture:

1. **API Gateway** - Receives HTTP requests (front door)
2. **Lambda Function** - Processes the request (brain) 
3. **S3 Buckets** - Stores files before/after processing (storage)

**Flow:** API Request → Lambda Processing → S3 Storage

## 🛠️ AWS Services Used
- **API Gateway** - REST API endpoint
- **Lambda** - Serverless compute (Python 3.9)
- **S3** - File storage (original + processed)
- **IAM** - Permissions and roles
