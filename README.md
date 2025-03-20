🎤 Text-to-Speech with AWS Polly

📌 Description

This project is a cloud-based application that converts text from a book, article, or newsletter into speech using AWS Polly and stores the MP3 file in Amazon S3. The application uses AWS Lambda functions for serverless processing and a simple Flask web interface for user interaction.

✨ Features

📄 Upload text or provide direct input.

🔊 Convert text into speech using Amazon Polly.

☁️ Store the generated MP3 file in an Amazon S3 bucket.

🎶 Retrieve and play/download the generated MP3 file via a web interface.

🛠️ AWS Services Used

🖥 AWS Lambda - Serverless compute function to handle text processing and Polly API calls.

🗣 Amazon Polly - Text-to-Speech conversion.

📦 Amazon S3 - Storage for the generated MP3 files.

🌐 API Gateway - (Optional) To expose Lambda functions as APIs.

📂 Project Structure

🚀 Setup Instructions

📌 Prerequisites

🐍 Python 3.x installed.

☁️ AWS account with IAM permissions for Lambda, Polly, and S3.

📦 Install required Python packages:

🏗 Steps to Run Locally

1️⃣ Clone the repository:

2️⃣ Set up AWS credentials in config/aws-config.json (ensure it is ignored in .gitignore).
3️⃣ Deploy AWS Lambda functions for text processing and Polly.
4️⃣ Run the Flask app locally:

5️⃣ Open the web interface and enter text to convert into speech.

🌍 Deployment on AWS

🚀 Deploy Lambda functions and configure them to trigger via API Gateway.

☁️ Set up an S3 bucket for storing MP3 files.

🔗 Use pre-signed URLs for secure access to audio files.

🎧 Usage

📜 Open the Flask web interface.

✍️ Input text manually or upload a text file.

🎙 Select a voice model and language.

🔄 Click 'Convert' to generate and play the MP3 file.

🔮 Future Enhancements

🌍 Support multiple languages.

🎛 Add real-time voice customization.

🧠 Integrate with Amazon Comprehend for sentiment analysis.

👨‍💻 Author

Your Name🎓 Third-Year CSE Student🔗 GitHub Profile
