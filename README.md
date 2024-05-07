# pypdfht

## Overview
`pypdfht` is a Python library designed to highlight text within PDF files. It provides a simple API for identifying and highlighting specific strings of text on any given page of a PDF.

## Features
- **Text Highlighting**: Utilize the `highlight_entire_text_on_page` function to programmatically highlight text on a PDF page.

## API Example
To use the API to highlight text, you can send a POST request with the PDF file, the page number, and the text to be highlighted. Below is an example using `curl`:

```bash
curl -X POST -F "file=@path_to_your_file.pdf" -F "page_number=1" -F "text='your text here'" http://your-server-address/highlight
```

## Usage
To use the highlighting feature, ensure you have a running instance of the server that includes the `highlight` route as defined in `app.py`. Then, use the curl command above to send a request to the server.

## Installation
Clone the repository and install the required Python packages:
```bash
git clone https://github.com/nagendra-y/pypdfht.git
cd pypdfht
pip install -r requirements.txt
```

## Running the Server
To start the server, run:
```bash
python app.py
```

This will start a Flask server that listens for requests to highlight text in PDF files.

