# PDF Manipulator

This script adds an overlay to a PDF file.

## Prerequisites

- Python 3
- The following Python libraries: `reportlab`, `PyPDF2`

You can install the prerequisites with pip:

```bash
pip install reportlab PyPDF2
```

## Usage

```bash
python src/edicao_documento.py --input <path_to_input_pdf> --output <path_to_output_pdf>
```

### Arguments

- `--input`: The path to the input PDF file.
- `--output`: The path where the modified PDF file will be saved.

### Example

```bash
python src/edicao_documento.py --input my_document.pdf --output my_modified_document.pdf
```