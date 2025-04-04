from flask import Flask, request, render_template
import requests

app = Flask(__name__)
LAMBDA_API_URL = "https://1pimxen8r9.execute-api.ap-south-1.amazonaws.com/prod/text_to_speech"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        voice_id = request.form["voice"]

        try:
            response = requests.post(
                LAMBDA_API_URL,
                json={"text": text, "voice_id": voice_id}
            )
            print("Lambda response:", response.text)

            if response.status_code == 200:
                audio_base64 = response.json().get("audio")
                return render_template("index.html", audio_base64=audio_base64)
            else:
                return f"Error: {response.status_code} - {response.text}", 500

        except Exception as e:
            return f"Exception occurred: {e}", 500

    return render_template("index.html", audio_base64=None)


if __name__ == "__main__":
    app.run(debug=True)
