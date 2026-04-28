# File_Upload_Server

## Overview
This project is a simple file upload server built using Flask. It allows users to upload files through a web interface or via HTTP POST requests.

Uploaded files are stored on the server in a designated directory.

## Features
- Web-based file upload form
- REST-style API responses (JSON)
- File type validation using an allowlist
- Automatic upload directory creation
- Lightweight and easy to run

## Supported File Types
The server accepts the following file extensions:

- txt
- pdf
- png
- jpg / jpeg
- gif
- zip
- mp4
- json
- xlsx

## Project Structure

.
├── File_upload.py

├── uploads/

├── README.md


## Requirements
- Python 3.x


## Installation & Setup
Clone the repository:
```bash
git clone https://github.com/your-username/flask-file-upload.git
```
```bash
cd flask-file-upload
```

## Run the server:
```bash
python app.py
```
The server will start on:
http://192.168.60.193:8080/upload

## Usage
Web Interface
Open your browser and go to /upload
Choose a file
Click Upload

## API Usage (cURL example)
curl -X POST -F "file=@example.txt" http://192.168.60.193:8080/upload

### Responses

Success

{
"message": "File uploaded successfully",
"path": "uploads/example.txt"
}

Error Examples

{ "error": "No file part in the request" }

{ "error": "No file selected" }

{ "error": "File type not allowed" }

## Configuration

You can modify these variables in the code:


UPLOAD_FOLDER → Directory where files are stored

ALLOWED_EXTENSIONS → Allowed file types

host and port → Server binding settings

## ⚠️ Security Considerations

This project is a basic implementation and not production-ready. Consider the following improvements before deploying:


Add authentication and access control

Use secure filenames (werkzeug.utils.secure_filename)

Limit file size to prevent abuse

Enable proper HTTPS configuration

Disable debug=True in production

Validate and sanitize uploaded files

## Disclaimer
This project is intended for educational and development purposes only. Use responsibly and ensure proper security measures in real-world deployments.
