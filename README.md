# 📢 Text-to-Speech Converter (AWS Lambda + Polly + API Gateway)

## 🚀 Overview
This project converts text into speech using **AWS Lambda**, **Amazon Polly**, and **API Gateway**. Users can enter text, upload a file, select a voice, and listen to or download the generated speech in real-time without needing cloud storage.

## 🔥 Features
✅ Convert text into speech using **Amazon Polly**  
✅ Supports multiple voices & languages  
✅ File uploader for future PDF integration  
✅ No storage required—MP3 is processed and returned in real-time  
✅ Fully serverless using **AWS Lambda + API Gateway**  
✅ Simple **Flask Web Interface** for easy interaction  

## 🛠️ Tech Stack
- **Frontend:** Flask (Python), HTML, CSS, JavaScript
- **Backend:** AWS Lambda (Python), API Gateway
- **AWS Services:** Amazon Polly (Text-to-Speech), API Gateway (REST API)

---

## 📌 Architecture Diagram

User -> [Flask Web App] -> [API Gateway] -> [AWS Lambda]
        -> [Polly Generates Speech] -> [Lambda Returns MP3]
   -> [Frontend Plays/Downloads Audio]




## 🏗️ Setup & Installation

### **1️⃣Clone the Repository**

git clone https://github.com/yourusername/text-to-speech.git
cd text-to-speech

### **2️⃣ Install Dependencies**
bash
pip install flask requests


### **3️⃣ Deploy AWS Lambda Function**
1. Go to **AWS Lambda** and create a new function.
2. Select **Python 3.9** as the runtime.
3. Add the following policy to the IAM role:
   - `AmazonPollyFullAccess`
4. Copy and paste this code into the function:
```python
import boto3
import base64
import json

polly = boto3.client("polly")

def lambda_handler(event, context):
    text = event.get("text", "Hello, this is a test.")
    voice_id = event.get("voice_id", "Joanna")

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice_id
    )

    audio_stream = response["AudioStream"].read()
    audio_base64 = base64.b64encode(audio_stream).decode("utf-8")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"audio": audio_base64})
    }
```
5. Click **Deploy**

### **4️⃣ Set Up API Gateway**
1. Go to **API Gateway** → **Create API** → **HTTP API**
2. Choose **AWS Lambda Integration** and select the deployed function
3. Create a **POST method** with the path `/convert`
4. Deploy API and copy the **Invoke URL**

### **5️⃣ Update Flask App with API Gateway URL**
Modify `app.py` to use the API Gateway URL:
```python
LAMBDA_API_URL = "https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/convert"
```

### **6️⃣ Run Flask App**
```bash
python app.py
```
Go to `http://127.0.0.1:5000/` in your browser and test the app!

---

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/convert` | Converts text to speech and returns MP3 in Base64 |

### **Example API Request (Using cURL)**
```bash
curl -X POST "https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/convert" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, world!", "voice_id": "Joanna"}'
```

---

## 🎨 Web Interface (Flask Frontend)
### **index.html (Attractive UI with Upload Option)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Text-to-Speech Converter</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9f9fb;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
            width: 500px;
            text-align: center;
        }
        textarea {
            width: 100%;
            height: 120px;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 8px;
            border: 1px solid #ccc;
            resize: vertical;
        }
        select, button, input[type="file"] {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        audio {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🔊 Text-to-Speech Converter</h2>
        <form method="POST" enctype="multipart/form-data">
            <textarea name="text" placeholder="Enter or paste text here..."></textarea>
            <select name="voice">
                <option value="Joanna">Joanna (English)</option>
                <option value="Matthew">Matthew (English)</option>
            </select>
            <input type="file" name="file">
            <button type="submit">Convert to Speech</button>
        </form>
        {% if audio_base64 %}
            <h3>Audio Output:</h3>
            <audio controls>
                <source src="data:audio/mp3;base64,{{ audio_base64 }}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
        {% endif %}
    </div>
</body>
</html>
```

---

## 🛠️ Troubleshooting & Common Issues
### ❌ **API Gateway Not Responding?**
- Check if your **Lambda function permissions** allow API Gateway access.
- Verify the **Invoke URL** in `app.py`.

### ❌ **MP3 Not Playing?**
- Ensure the response from Lambda contains **valid Base64 audio**.
- Debug by printing the Base64 string in Flask.

---

## 🌟 Future Enhancements
✅ Add **more voice options** (French, Spanish, etc.)  
✅ Allow **file uploads** (Convert PDFs or DOCX to speech)  
✅ Deploy Flask app on **AWS EC2 or Heroku**

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## ⭐ Acknowledgments
🔹 Built with **AWS Lambda, Polly, API Gateway, Flask**  
🔹 Special thanks to [Amazon Polly Documentation](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)  

🚀 **Star this repo if you found it helpful!** 😊

