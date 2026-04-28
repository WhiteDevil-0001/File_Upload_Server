from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# Directory where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'mp4', 'json', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload form and upload handling
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({'message': 'File uploaded successfully', 'path': filepath}), 200
        else:
            return jsonify({'error': 'File type not allowed'}), 400

    # GET request: show upload form
    return render_template_string('''
        <!doctype html>
        <title>Upload File</title>
        <h1>Upload a File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
    ''')

# Start the server
if __name__ == '__main__':
    # Replace 'path/to/fullchain.pem' and 'path/to/privkey.pem' with the actual paths to your SSL certificate files
    app.run(host='192.168.60.193', port=8080, debug=True)
