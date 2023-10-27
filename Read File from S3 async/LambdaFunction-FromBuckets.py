import csv
import boto3
import io


def lambda_handler(event, context):
    # Initialize the s3 resource using the boto3
    s3 = boto3.client('s3')

    # Extract the Bucket name and the CSV file name from the 'event' input
    billing_bucket = event['Records'][0]['s3']['bucket']['name']
    billing_file = event['Records'][0]['s3']['object']['key']

    # Open the billing file
    response = s3.get_object(Bucket=billing_bucket, Key=billing_file)

    # Read the contents of the file
    csv_reader = csv.reader(io.StringIO(response['Body'].read().decode('utf-8')))

    # Iterate over the rows of the CSV file and process the data as needed
    for row in csv_reader:
        print(row)

    return {'The status Code': 200}


""" EXECUTION RESULTS
Test Event Name
InsertFile

Response
{
  "The status Code": 200
}

Function Logs START RequestId: f9b1d2bd-8854-4b54-835e-3c84f2387ea8 Version: $LATEST adnen.mess.bucket.demo 
dct-billing/billing_data_meat_may_2023.csv END RequestId: f9b1d2bd-8854-4b54-835e-3c84f2387ea8 REPORT RequestId: 
f9b1d2bd-8854-4b54-835e-3c84f2387ea8	Duration: 1807.96 ms	Billed Duration: 1808 ms	Memory Size: 128 MB	Max 
Memory Used: 79 MB	Init Duration: 249.20 ms

Request ID
f9b1d2bd-8854-4b54-835e-3c84f2387ea8
"""
