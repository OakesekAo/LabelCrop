import io


def crop_pdf(input_pdf_path, output_pdf_path, crop_box):
    from PyPDF2 import PdfReader, PdfWriter

    print(f"Cropping PDF: {input_pdf_path}")
    print(f"Output PDF: {output_pdf_path}")
    print(f"Crop box: {crop_box}")

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        # Get the original page dimensions
        original_width = page.mediabox.upper_right[0]
        original_height = page.mediabox.upper_right[1]

        # Adjust the crop box coordinates for the PDF coordinate system
        adjusted_crop_box = (
            crop_box[0],
            original_height - crop_box[3],
            crop_box[2],
            original_height - crop_box[1]
        )

        print(f"Original crop box: {page.cropbox.lower_left}, {page.cropbox.upper_right}")
        print(f"Adjusted crop box: {adjusted_crop_box}")

        page.cropbox.lower_left = (adjusted_crop_box[0], adjusted_crop_box[1])
        page.cropbox.upper_right = (adjusted_crop_box[2], adjusted_crop_box[3])
        print(f"New crop box: {page.cropbox.lower_left}, {page.cropbox.upper_right}")
        writer.add_page(page)

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)
    print(f"Cropped PDF saved as {output_pdf_path}")


def resize_pdf(input_pdf_path, output_pdf_path, width, height):
    from PyPDF2 import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=(width, height))
        # Draw the entire page onto the canvas
        can.setPageSize((width, height))
        can.drawInlineImage(page.extract_text(), 0, 0, width, height)
        can.save()

        packet.seek(0)
        new_pdf = PdfReader(packet)
        writer.add_page(new_pdf.pages[0])

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)


def rotate_pdf(input_pdf_path, output_pdf_path, rotation_angle):
    from PyPDF2 import PdfReader, PdfWriter

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(rotation_angle)
        writer.add_page(page)

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)