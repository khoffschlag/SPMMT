from SPMMT.utils import preprocess_cell, pdf_to_docx
import pandas as pd
import docx
import re


def transcribe(file, module_start, output_xlsx=None, columns={}, start_page=0, end_page=None, pages=None):
    """

    Transcribe information from educational module manual file into pandas dataframe (and xlsx if specified).

    This function can be used for processing educational module manuals if each module's details are
    in tabular form. The expected table format is that the most-left column specifies the categories
    (e.g., 'ECTS', 'Type of Exam') and the column on the right next contains the actual values
    (e.g., '12 Credits', 'Oral exam').

    The result can be saved in a xlsx file.

    Parameters:
        file (str): Path to the input DOCX or PDF file.
        module_start (str): Regex pattern that identifies the beginning of a module's description in the table.
                            For example, r'[A-Z]{2}\s+\d{3}' could be used to identify course IDs like 'CS 512'.
                            CAUTION: Only in the most-left cells will be searched! Also, the cell next to the matched
                                     will be included in the resulting dataframe.
        output_xlsx (str, optional): Path to save the DataFrame as a xlsx file. If None, the data is not saved.
        columns (dict, optional): A mapping of left-most cell values in the source document to column names in the
                                  output DataFrame.
                                  For example, if one of your left-most cells is called '1.1' and the corresponding
                                  value is the amount of credits, then you might not want to have the name '1.1' as
                                  a column in the dataframe but rather something like 'ECTS'.
                                  In this case specify columns parameter as {'1.1': 'ECTS'}.
        start_page (int, optional): The starting page number for PDF to DOCX conversion.
                                    Relevant only if the input file is a PDF.
        end_page (int, optional): The ending page number for PDF to DOCX conversion.
                                  Relevant only if the input file is a PDF.
        pages (list, optional): List of page indices for PDF to DOCX conversion.
                                Has priority over --start_page/--end_page!

        Returns:
            pandas.dataframe: A Pandas DataFrame containing the results of the conversion with one row per module.

    """

    if (output_xlsx is not None) and (not output_xlsx.endswith('.xlsx')):
        raise ValueError('output_xlsx must have the extension ".xlsx"!')

    if file.endswith('.pdf'):
        print('Starting conversion of PDF to DOCX...')
        docx_file = pdf_to_docx(pdf_path=file, docx_path=None, start_page=start_page, end_page=end_page, pages=pages)
        print('Finished conversion of PDF to DOCX...')
    elif file.endswith('.docx'):
        docx_file = file
    else:
        raise ValueError('Currently, only pdf and docx files are supported!')

    document = docx.Document(docx_file)
    module_start_pattern = re.compile(module_start)
    modules = []

    print('Starting transcription...')
    for table in document.tables:
        for row in table.rows:
            key_cell = row.cells[0].text  # left-most cell containing category (e.g., 'ECTS')
            value_cell = row.cells[1].text  # cell containing value for category (e.g., '12 Credits')
            # Remove special characters like arrows or other non-alphanumeric characters if needed
            key_cell = preprocess_cell(key_cell)
            value_cell = preprocess_cell(value_cell)

            if module_start_pattern.match(key_cell):  # Found start of new module
                modules.append({})
                modules[-1]['Module'] = value_cell
            else:
                if key_cell in columns:
                    column_name = columns[key_cell]
                else:
                    column_name = key_cell

                if len(modules) > 0:
                    modules[-1][column_name] = value_cell

    df = pd.DataFrame(modules)
    print('Finished transcription!')
    print(f'Found {len(modules)} modules and {len(df.columns)} categories!')
    print('-'*10)
    print('Found categories:')
    print(df.columns)
    print('-' * 10)

    if output_xlsx is not None:
        print(f'Saving transcription to {output_xlsx}')
        df.to_excel(output_xlsx)

    return df
