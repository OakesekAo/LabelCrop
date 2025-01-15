from tkinter import Canvas, PhotoImage, NW, Button, Toplevel
from PIL import Image, ImageTk
import fitz  # PyMuPDF
from utils.pdf_processor import resize_pdf, rotate_pdf, crop_pdf

class PDFCropper:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Cropper")
        self.canvas = Canvas(root)
        self.canvas.pack(fill="both", expand=True)
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.image = None
        self.photo_image = None
        self.pdf_path = None
        self.cropped_image = None
        self.rotation_angle = 0

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def load_pdf(self, pdf_path):
        self.pdf_path = pdf_path
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # Load the first page
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.image = img
        self.photo_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo_image)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.root.geometry(f"{pix.width}x{pix.height}")

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")
        print(f"Start coordinates: ({self.start_x}, {self.start_y})")

    def on_mouse_drag(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        print(f"End coordinates: ({self.end_x}, {self.end_y})")
        self.show_cropped_image()

    def show_cropped_image(self):
        if self.image:
            # Convert canvas coordinates to image coordinates
            canvas_bbox = self.canvas.bbox(self.rect)
            print(f"Canvas bounding box: {canvas_bbox}")
            self.cropped_image = self.image.crop(canvas_bbox)
            self.update_cropped_image()

    def update_cropped_image(self):
        self.cropped_photo_image = ImageTk.PhotoImage(self.cropped_image)

        # Create a new window to show the cropped image
        self.cropped_window = Toplevel(self.root)
        self.cropped_window.title("Cropped Image")
        cropped_canvas = Canvas(self.cropped_window, width=self.cropped_image.width, height=self.cropped_image.height)
        cropped_canvas.pack()
        cropped_canvas.create_image(0, 0, anchor=NW, image=self.cropped_photo_image)

        # Add rotation and confirm/cancel buttons
        rotate_left_button = Button(self.cropped_window, text="Rotate Left", command=self.rotate_left)
        rotate_left_button.pack(side="left")
        rotate_right_button = Button(self.cropped_window, text="Rotate Right", command=self.rotate_right)
        rotate_right_button.pack(side="left")
        confirm_button = Button(self.cropped_window, text="Confirm", command=self.confirm_crop)
        confirm_button.pack(side="left")
        cancel_button = Button(self.cropped_window, text="Cancel", command=self.cropped_window.destroy)
        cancel_button.pack(side="right")

    def rotate_left(self):
        self.rotation_angle -= 90
        self.cropped_image = self.cropped_image.rotate(90, expand=True)
        self.update_cropped_image()

    def rotate_right(self):
        self.rotation_angle += 90
        self.cropped_image = self.cropped_image.rotate(-90, expand=True)
        self.update_cropped_image()

    def confirm_crop(self):
        self.cropped_window.destroy()
        self.crop_pdf()
        self.root.destroy()

    def crop_pdf(self):
        if self.pdf_path and self.start_x and self.start_y and self.end_x and self.end_y:
            # Convert canvas coordinates to PDF coordinates
            canvas_bbox = self.canvas.bbox(self.rect)
            crop_box = (canvas_bbox[0], canvas_bbox[1], canvas_bbox[2], canvas_bbox[3])
            print(f"Crop box: {crop_box}")
            output_pdf_path = "output_label.pdf"
            crop_pdf(self.pdf_path, output_pdf_path, crop_box)
            if self.rotation_angle != 0:
                rotate_pdf(output_pdf_path, output_pdf_path, self.rotation_angle)
            #resize_pdf(output_pdf_path, output_pdf_path, 288, 432)
            print(f"Processed PDF saved as {output_pdf_path}")