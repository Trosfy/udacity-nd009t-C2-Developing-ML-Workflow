import json
import ast

THRESHOLD = .8


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = ast.literal_eval(json.loads(event["body"])["body"]["inferences"])
    
    print(inferences)
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(float(inference) > THRESHOLD for inference in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        return {
            'statusCode': 403,
            'body': json.dumps(event)
        }

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }