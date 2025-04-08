import boto3
import base64
import json

polly = boto3.client("polly")

def lambda_handler(event, context):
    try:
        # Parse body from API Gateway (Lambda Proxy Integration)
        body = json.loads(event.get("body", "{}"))

        text = body.get("text")
        voice_id = body.get("voice_id", "Joanna")

        # Validate input text
        if not text:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "No text provided."})
            }

        # Synthesize speech
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=voice_id
        )

        audio_stream = response["AudioStream"].read()
        audio_base64 = base64.b64encode(audio_stream).decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"audio": audio_base64})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
