import boto3
import json

s3 = boto3.client('s3')

# Get a list of all the objects in the S3 bucket.
objects = s3.list_objects(Bucket='adnen.mess.bucket.demo')


def lambda_handler(event, context):
    """
    Reads all the files contained in the S3 bucket called `adnen.mess.bucket.demo`.
    And print the file names in the handler return body

    Args:
      event: The event that triggered the Lambda function.
      context: The Lambda function context.

    Returns:
      A JSON object containing the names of the files in the S3 bucket.
    """

    # Get the names of all the files in the S3 bucket.
    file_names = []
    for object in objects['Contents']:
        file_names.append(object['Key'])

    # Returns the names of the files in the body of the handler return.
    return {
        'statusCode': 200,
        'body': json.dumps(file_names)
    }
