# SPMMT
Study Program Module Manual Transcription 

# Installation
Run the following command in order to install the package:
> pip install git+https://github.com/khoffschlag/SPMMT.git

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