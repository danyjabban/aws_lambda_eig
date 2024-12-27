import json
import numpy as np
import boto3

def lambda_handler(event, context):

    for record in event['Records']:
        message_body = record['body']
        message_body = json.loads(message_body)
        message_id = record['messageId']

        dynamodb = boto3.resource('dynamodb')
        table_name = 'matrix_data'
        table = dynamodb.Table(table_name)
        
        matrix_list = message_body['matrix']
        matrix = np.asarray(matrix_list, dtype=np.float32)
        eigen_values, eigen_vectors = np.linalg.eig(matrix)
        eigen_values_list = eigen_values.tolist()
        eigen_vectors_list = eigen_vectors.tolist()

        table.put_item(Item = {'messageId':f"{matrix_list}", 'eigen_values':eigen_values_list})

    return {
        'statusCode': 200,
        'body': f'successfully uploaded to db, {eigen_values_list}'
    }
