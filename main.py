import httpx


def handler(event, context):
    http = httpx.Client()
    print("hello world")

    return {
        'statusCode': 200,
        'body': 'hello world',
    }
