# SPMMT
Study Program Module Manual Transcription 

# Installation
Run the following command in order to install the package:
> pip install git+https://github.com/khoffschlag/SPMMT.git

# Notes

1. If a PDF file is supplied, then an internal conversion to docx will take place. The integrated converter is generally good, but sometimes produces poor results.
In this event, try to convert the PDF file with the corresponding Adobe tool (or some other tool)
and pass the resulting docx to SPMMT.

2. SPMMT does not deal well with situations in which there are several sub-cells next to one key-cell
(i.e., multiple cells underneath each other in the column next to a key-cell, belonging to the key-cell).
In these cases, it makes sense to preprocess the files manually before transferring them to SPMMT.

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