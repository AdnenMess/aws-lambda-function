import json
import boto3
import datetime

'''
This function reads all the Buckets in my S3
'''

s3 = boto3.client('s3')


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


def lambda_handler(event, context):
    response = s3.list_buckets()

    # Print the bucket names
    print('The names of My Backers are : ')
    for bucket in response.get('Buckets', []):
        print(f' {bucket["Name"]}')

    # Return the list of bucket names
    return {
        'statusCode': 200,
        'body': json.dumps(response['Buckets'], cls=DateTimeEncoder)
    }
