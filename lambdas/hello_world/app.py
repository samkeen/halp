import json

# import requests
from lambdas.hello_world.foo import foo


def lambda_handler(event, context):
    print(foo())
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
