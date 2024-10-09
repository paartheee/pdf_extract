import streamlit as st
import pdfplumber
import pandas as pd
from pdfplumber.utils import extract_text, get_bbox_overlap, obj_to_bbox

def process_pdf(pdf_file):
    """Processes a PDF file and returns the extracted text with tables converted to Markdown."""

    pdf = pdfplumber.open(pdf_file)
    all_text = []

    for page in pdf.pages:
        filtered_page = page
        chars = filtered_page.chars

        for table in page.find_tables():
            first_table_char = page.crop(table.bbox).chars[0]

            filtered_page = filtered_page.filter(lambda obj:
                get_bbox_overlap(obj_to_bbox(obj), table.bbox) is None
            )

            chars = filtered_page.chars
            df = pd.DataFrame(table.extract())
            df.columns = df.iloc[0]
            markdown = df.drop(0).to_markdown(index=False)

            chars.append(first_table_char | {"text": markdown})

        page_text = extract_text(chars, layout=True)
        all_text.append(page_text)

    pdf.close()
    return "\n".join(all_text)

def main():
    """Streamlit app to upload image or PDF and display extracted text."""

    st.title("Text and Table Extractor From PDF File")

    file_type = st.selectbox("Select file type:", ("PDF"))
    uploaded_file = None

    if file_type == "PDF":
        uploaded_file = st.file_uploader("Upload PDF file:", type="pdf")
    else:
        # Add image support using a suitable library (e.g., pytesseract)
        st.error("The Uploaded file_type OCR processing is not currently implemented. Stay tuned for updates!")

    if uploaded_file is not None:
        try:
            extracted_text = process_pdf(uploaded_file)
            st.write("Extracted Text:")
            st.code(extracted_text, language="text")
        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()