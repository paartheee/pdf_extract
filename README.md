# PDF Text and Table Extractor

This repository contains a **Streamlit** web application that allows users to upload a **PDF** file and extract text and tables. The extracted tables are converted to **Markdown** format for better readability, and both the text and tables are displayed in the browser.

## Features

- Extract text and tables from **PDF** files.
- Tables are automatically converted into **Markdown** format.
- User-friendly **Streamlit** interface for easy file uploads.
- Displays extracted content (text and tables) directly in the app.

## Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed. 


Installation - Clone this repository:

```bash
git clone https://github.com/paartheee/pdf-text-table-extractor.git
```
Navigate into the project directory:
```bash
cd pdf-text-table-extractor
```
Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Running the Application
To run the Streamlit app, execute the following command in your terminal:

```bash
streamlit run app.py
```
Once the app is running, you can access it by navigating to http://localhost:8501 in your browser.
### Screenshots
Here are some screenshots of the app in action:
### Input pdf (attached in repo)
![test_page-0001](https://github.com/user-attachments/assets/05e98d86-5ee3-4eb2-bdf0-9f9d15a272e1)


### Upload PDF Interface
![image](https://github.com/user-attachments/assets/86641fc5-9458-4fd3-84e2-28167847539c)


### Extracted Text and Tables
![image](https://github.com/user-attachments/assets/945100b7-e7cb-4bd9-acc7-b7c12baef218)
![image](https://github.com/user-attachments/assets/60a497dc-db64-48a9-aa79-aa0b7a2573e6)

## How to Use
- Upload a PDF file using the file uploader in the app.
- The app will automatically extract the text and tables from the PDF.
- Extracted tables are converted to Markdown and displayed along with the text.
## Code Explanation
### **process_pdf(pdf_file)**
- This function uses pdfplumber to open and read the uploaded PDF file.
- It extracts both the text and tables from the PDF.
- The tables are detected and extracted using pdfplumber's table detection capabilities, then converted into Markdown format.
- The extracted content is concatenated into a single output, which is then returned as a string.

### **main()**

- The main() function defines the Streamlit app interface.
- It allows users to upload PDF files.
- Once a file is uploaded, it processes the PDF using the process_pdf() function.
- The extracted text and tables are displayed in the Streamlit interface.
