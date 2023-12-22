from SPMMT.transcriber import transcribe
import argparse
import json


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Transcribe information from educational module manual to pandas dataframe (and xlxs) with SPMMT.'
    )
    parser.add_argument('file', type=str, help='Path to the input DOCX or PDF file.')
    parser.add_argument('module_start', type=str,
                        help='Regex pattern identifying the beginning of a module description'
                             '(will search only in the most-left cells of table).')
    parser.add_argument('--output_xlsx', type=str, default=None,
                        help='Path to xlsx file where the results should be stored in.')
    parser.add_argument('--columns', type=json.loads, default={},
                        help='Mapping left-most cell values to column names.')
    parser.add_argument('--start_page', type=int, default=0,
                        help='Starting page number for PDF to DOCX conversion.')
    parser.add_argument('--end_page', type=int, default=None,
                        help='Ending page number for PDF to DOCX conversion.')
    parser.add_argument('--pages', type=json.loads, default=None,
                        help='List of page indices for PDF to DOCX conversion.'
                             'Has priority over --start_page/--end_page!')
    args = parser.parse_args()

    transcribe(
        file=args.file,
        module_start=args.module_start,
        output_xlsx=args.output_xlsx,
        columns=args.columns,
        start_page=args.start_page,
        end_page=args.end_page,
        pages=args.pages
    )
