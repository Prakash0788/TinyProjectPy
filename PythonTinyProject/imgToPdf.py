'''
We can turn multiple images into a single PDF file using Python with the
fpdf2 library, which is the modern replacement for older FPDF versions.
'''


from fpdf import FPDF
import os

# Create a PDF object
pdf = FPDF(unit="mm", format="A4")

# List of image file paths
imagelist = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg"
]

for image_path in imagelist:
    # Check if the image file exists
    if os.path.exists(image_path):
        pdf.add_page()
        pdf.image(image_path, x=10, y=10, w=190)
    else:
        print(f"File not found: {image_path}")

# Save the PDF file
pdf.output("yourFile.pdf")
