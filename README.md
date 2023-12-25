# SPMMT

---

Study Program Module Manual Transcription

---

SPMMT allows you to transcribe information from an educational module manual file into a pandas dataframe
(and xlsx if specified).

SPMMT can be used for transcription of educational module manuals if each module's details are
in tabular form. The expected table format is that the most-left column specifies the categories
(e.g., 'ECTS', 'Type of Exam') and the column on the right next contains the actual values
(e.g., '12 Credits', 'Oral exam').

# Installation
First you need to make sure that Git and Python 3.9 (or a newer Python 3 version) is installed.

Afterwards, run the following command in your terminal in order to install SPMMT:

> pip install git+https://github.com/khoffschlag/SPMMT.git

# Usage

You can use SPMMT via CLI or in your Python code.

For the CLI usage:

```
usage: spmmt.py [-h] [--output_xlsx OUTPUT_XLSX] [--columns COLUMNS]
                [--start_page START_PAGE] [--end_page END_PAGE]
                [--pages PAGES]
                file module_start

Transcribe information from educational module manual to pandas dataframe (and
xlxs) with SPMMT.

positional arguments:
  file                  Path to the input DOCX or PDF file.
  module_start          Regex pattern identifying the beginning of a module
                        description (will search only in the most-left cells of
                        table).

options:
  -h, --help            show this help message and exit
  --output_xlsx OUTPUT_XLSX
                        Path to xlsx file where the results should be stored
                        in.
  --columns COLUMNS     Mapping left-most cell values to column names.
  --start_page START_PAGE Starting page number for PDF to DOCX conversion.
  --end_page END_PAGE   Ending page number for PDF to DOCX conversion.
  --pages PAGES         List of page indices for PDF to DOCX conversion.
                        Has priority over --start_page/--end_page!
```

# CLI examples

1. > python spmmt.py PATH_TO_PDF "Module Number*" --start_page 11 --output_xlsx tuebingen_ML.xlsx

2. > python spmmt.py PATH_TO_DOCX "^1$" --output_xlsx darmstadt.xlsx

# Package examples

## Example 1

> from SPMMT.transcriber import transcribe
> 
> df = transcribe(file='mannheim.docx', module_start=r'[A-Z][A-Z]*\s\d{3}', pages=[7,8,9,10], output_xlsx='mannheim.xlsx')
> 
> print(df)

# Notes

1. If a PDF file is supplied, then an internal conversion to docx will take place. The integrated converter is generally good, but sometimes produces poor results.
In this event, try to convert the PDF file with the corresponding Adobe tool (or some other tool)
and pass the resulting docx to SPMMT.

2. SPMMT does not deal well with situations in which there are several sub-cells next to one key-cell
(i.e., multiple cells underneath each other in the column next to a key-cell, belonging to the key-cell).
In these cases, it makes sense to preprocess the files manually before transferring them to SPMMT.
