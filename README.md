# Serverless Image Processing Pipeline

## Overview

A lightweight serverless pipeline for processing images using AWS services. Files are uploaded to one S3 bucket, processed by a Lambda function orchestrated through Step Functions, and saved to another S3 bucket. The pipeline is triggered through API Gateway.

---

## Architecture

```
API Gateway → Step Functions → Lambda → S3 (original / processed)
```

---

## AWS Services Used

* API Gateway – REST API endpoint
* Lambda – Python 3.9 image-processing function
* Step Functions – Workflow orchestration
* S3 – Stores original and processed images
* IAM – Roles and permissions

---

## Project Structure

```
Philip-Ngui/
├── README.md
├── lambda/
│   └── lambda_function.py
├── state_machine/
│   └── state_machine.json
├── .gitignore
└── LICENSE
```

---

## How to Run

### 1. Prerequisites

* AWS account
* (Optional) AWS CLI configured locally

---

### 2. Create S3 Buckets

```bash
aws s3 mb s3://yourname-original-images --region us-east-2
aws s3 mb s3://yourname-resized-images --region us-east-2
```

---

### 3. Create the Lambda Function

1. Open AWS Lambda Console
2. Create function: ImageResizeFunction
3. Runtime: Python 3.9
4. Upload `lambda/lambda_function.py`
5. Add S3 read/write permissions to the execution role

---

### 4. Create the Step Functions State Machine

1. Open AWS Step Functions Console
2. Create a state machine
3. Use JSON from `state_machine/state_machine.json`
4. Name it: ImageProcessingStateMachine

---

### 5. Create API Gateway Endpoint

1. Open AWS API Gateway Console
2. Create REST API: ImageProcessingAPI
3. Add a POST method integrated with Step Functions
4. Deploy to the prod stage

---

## Testing

### Method 1: Using curl

```bash
curl -X POST "https://your-api-id.execute-api.us-east-2.amazonaws.com/prod" \
-H "Content-Type: application/json" \
-d '{
  "sourceBucket": "yourname-original-images",
  "sourceKey": "test-image.jpg",
  "destinationBucket": "yourname-resized-images"
}'
```

### Method 2: Using AWS Console

1. Upload an image to your source bucket
2. Send a POST request to your API Gateway endpoint
3. Check the destination bucket for the processed file
