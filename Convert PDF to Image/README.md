# PDF to Image Conversion

This document provides instructions and code snippets for converting PDF files into images. This process is a crucial step in your project for extracting text from the first page of exam answer sheets.


## Requirements

Before proceeding with the PDF-to-image conversion, make sure you have the following requirements in place:

1. Python installed on your system.
2. The necessary Python libraries installed, including PyMuPDF or PyMuPDF (MuPDF) for PDF processing.

## Code for PDF to Image Conversion

The following Python code converts PDF files into high-quality images, specifically focusing on the first page of each PDF.

```python
import os
import fitz  # PyMuPDF

# Input and output directories
pdf_folder = "Your_PDF_Folder"
image_folder = "Output_Image_Folder"

# Create the output directory if it doesn't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# List all PDF files in the input directory
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Convert each PDF to an image with higher quality (600 DPI)
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # Get the first page of the PDF
    page = pdf_document[0]
    # Create an image from the page with 600 DPI
    pix = page.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72))
    # Define the image file path
    image_path = os.path.join(
        image_folder, os.path.splitext(pdf_file)[0] + '.png')
    # Save the image with high quality
    pix.save(image_path, "png")
    # Close the PDF document
    pdf_document.close()

print("PDF to image conversion with high quality completed.")
```

## Usage

1. Ensure you have Python installed on your system.

2. Install the required Python libraries, especially PyMuPDF or PyMuPDF (MuPDF).

3. Replace `"Your_PDF_Folder"` with the path to the folder containing your PDF files.

4. Replace `"Output_Image_Folder"` with the path where you want to save the converted images.

5. Run the Python script to convert the PDFs to images.

## Dependencies

- Python: [Download](https://www.python.org/downloads/)
- PyMuPDF: Install using `pip install PyMuPDF` or MuPDF: [MuPDF](https://github.com/pymupdf/PyMuPDF)

## License

This code is provided under the [MIT License](LICENSE).
