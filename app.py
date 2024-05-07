from flask import Flask, request, jsonify, send_file
import requests
from io import BytesIO
# Assuming ht.highlight_entire_text_on_page is defined elsewhere in your code
import ht

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/highlight', methods=['POST'])
def highlight_pdf_text():
    try:
        form = request.form 
        fileurl = form.get('fileurl')
        page_number = form.get('page_number')
        text = form.get('text')
        filename = form.get('filename')  
        file = request.files.get('file')
     
        if not fileurl and not file:
            return jsonify({'error': 'Missing required parameters fileurl or file'}), 400
        
        if not page_number or not text:
            return jsonify({'error': 'Missing required parameters (page_number, text)'}), 400

        if fileurl:
            response = requests.get(fileurl)
            if response.status_code!= 200:
                return jsonify({'error': f"Failed to fetch PDF: {response.status_code}"}), 400
            pdf_bytes = BytesIO(response.content)
        else:
            # Assuming the file is uploaded as 'file'
            pdf_bytes = file.read()

        image_data_base64, error = ht.highlight_entire_text_on_page(pdf_bytes, int(page_number), text)

        if error:
            return jsonify({'error': error}), 500
        elif image_data_base64:
            return jsonify({'image_data_base64': image_data_base64}), 200
    except Exception as e:
            return jsonify({'error': f"Error processing PDF: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

