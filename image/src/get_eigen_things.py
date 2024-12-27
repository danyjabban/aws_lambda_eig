import json
import numpy as np

def lambda_handler(event, context):
    matrix_list = json.loads(event)['matrix']
    matrix = npa = np.asarray(matrix_list, dtype=np.float32)
    eigen_values, eigen_vectors = np.linalg.eig(matrix)
    eigen_values_list = eigen_values.tolist()
    eigen_vectors_list = eigen_vectors.tolist()

    return {
        'statusCode': 200,
        'body': json.dumps([eigen_values_list, eigen_vectors_list])
    }


# if __name__ == "__main__":
#     mat = np.array([[2,0,0],
#                     [0,2,0],
#                     [0,0,2]])
    
#     d = {'message': 'Hello from Lambda! update made test CICD', 'matrix':mat.tolist()}
#     j = json.dumps(d)
#     out = lambda_handler(j, 'context')
#     print(out)
    