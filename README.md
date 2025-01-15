# Shipping Label Processor

This project is designed to process shipping label PDFs by cropping, resizing, and rotating them to ensure they can be printed in a 4x6 format with high quality.

## Project Structure

```

├── src
│ ├── main.py # Entry point for processing shipping labels
│ ├── utils
│ │ ├── pdf_processor.py # Utility functions for PDF manipulation
│ │ └── pdf_cropper.py # GUI for cropping and rotating PDFs
├── requirements.txt # List of dependencies
├── setup.py # Packaging information
└── README.md # Project documentation


```

### Create and Activate Virtual Environment

1. **Create a virtual environment**:
   - On Windows:
     ```
     python -m venv venv
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     ```

2. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

## Installation

To get started with this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

This will initiate the processing of shipping label PDFs.

## Functions

The utility functions for PDF processing are located in `src/utils/pdf_processor.py`. These include:

- `crop_pdf`: Crops the PDF to the desired dimensions.
- `resize_pdf`: Resizes the PDF to fit the 4x6 label format.
- `rotate_pdf`: Rotates the PDF to the correct orientation.

## Features

1. **Load PDF**: Use a file picker to select the PDF file to be processed.
2. **Crop PDF**: Draw a bounding box around the area to be cropped.
3. **Preview Cropped Area**: Preview the cropped area in a new window.
4. **Rotate Cropped Area**: Rotate the cropped area left or right by 90 degrees.
5. **Confirm Crop**: Confirm the cropped area and save the processed PDF in a 4x6 format.

## How to Use

1. **Run the Application**: Execute `python src/main.py` to start the application.
2. **Select PDF**: Use the file picker dialog to select the PDF file you want to process.
3. **Draw Bounding Box**: Click and drag to draw a bounding box around the area you want to crop.
4. **Preview and Rotate**: A new window will show the cropped area. Use the "Rotate Left" and "Rotate Right" buttons to adjust the orientation.
5. **Confirm Crop**: Click the "Confirm" button to save the processed PDF in a 4x6 format.

## Dependencies

- `tkinter`: For creating the GUI.
- `Pillow`: For image processing.
- `PyMuPDF`: For PDF manipulation.
- `PyPDF2`: For PDF manipulation.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
