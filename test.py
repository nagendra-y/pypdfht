import requests
import base64

def test_highlight_pdf_text():
    # Define sample JSON data
    data = {
        'page_number': 3,
        'text': 'void function(int a, int b, int c) { char buffer1[5]; char buffer2[10]; }'
    }
    
    # Files to be uploaded (if any)
    files = {
        'file': open('example.pdf', 'rb')  # Replace 'example.pdf' with the actual file path
    }    
    # Make a POST request to the Flask route
    response = requests.post('http://localhost:5000/highlight', data=data, files=files)
    # Decode the JSON response
    response_data = response.json()
    
    if 'error' in response_data:
        print(response_data)
        return

    with open('highlighted_image.png', 'wb') as f:
        # Decode the base64 string to bytes directly
        decoded_image_data = base64.b64decode(response_data['image_data_base64'])
        f.write(decoded_image_data)

if __name__ == '__main__':
    test_highlight_pdf_text()

