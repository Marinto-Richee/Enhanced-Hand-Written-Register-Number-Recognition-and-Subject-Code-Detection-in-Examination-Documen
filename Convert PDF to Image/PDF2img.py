import os
import fitz  # PyMuPDF
# Input and output directories
pdf_folder = "Paper_Sample_2"
image_folder = "Paper_Sample_Images_2"
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
    # Create an image from the page with 300 DPI
    pix = page.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72))
    # Define the image file path
    image_path = os.path.join(
        image_folder, os.path.splitext(pdf_file)[0] + '.png')
    # Save the image with high quality
    pix.save(image_path, "png")
    # Close the PDF document
    pdf_document.close()

print("PDF to image conversion with high quality completed.")
