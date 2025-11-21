//Lambda Function
import json
import boto3
s3 = boto3.client('s3')
def lambda_handler(event, context):
    if 'body' in event:
        body = json.loads(event['body'])
        source_bucket = body['sourceBucket']
        source_key = body['sourceKey']
        dest_bucket = body['destinationBucket']
    else:
        source_bucket = event['sourceBucket']
        source_key = event['sourceKey']
        dest_bucket = event['destinationBucket']
    
    copy_source = {'Bucket': source_bucket, 'Key': source_key}
    new_key = f"processed-{source_key}"
    s3.copy_object(Bucket=dest_bucket, Key=new_key, CopySource=copy_source)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'File processed successfully!', 'processed_file': new_key})
    }
  //test Event
{
  "sourceBucket": "philipngui-original-images",
  "sourceKey": "Profile Picture.jpg",
  "destinationBucket": "philipngui-resized-images"
}
//Step Function
{
  "Comment": "Image Processing Workflow",
  "StartAt": "ProcessImage",
  "States": {
    "ProcessImage": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "arn:aws:lambda:us-east-2:554909494907:function:ImageResizeFunction",
        "Payload.$": "$"
      },
      "Next": "CheckResult"
    },
    "CheckResult": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.Payload.statusCode",
          "NumericEquals": 200,
          "Next": "SuccessState"
        }
      ],
      "Default": "FailState"
    },
    "SuccessState": {
      "Type": "Succeed"
    },
    "FailState": {
      "Type": "Fail"
    }
  }
}
//Curl Command
curl -X POST "https://k0kr0fhzg5.execute-api.us-east-2.amazonaws.com/prod" \
-H "Content-Type: application/json" \
-d '{
  "sourceBucket": "philipngui-original-images",
  "sourceKey": "Profile Picture.jpg",
  "destinationBucket": "philipngui-resized-images"
}'
