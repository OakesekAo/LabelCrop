import os
from tkinter import Tk, filedialog
from utils.pdf_cropper import PDFCropper

def main():
    root = Tk()
    app = PDFCropper(root)

    # Open file picker dialog
    pdf_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    if pdf_path:
        app.load_pdf(pdf_path)
    else:
        print("No file selected!")
        root.destroy()

    root.mainloop()

if __name__ == "__main__":
    main()