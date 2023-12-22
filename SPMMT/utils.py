from pdf2docx import Converter
import re


def preprocess_cell(cell_content):
    """

    Remove special characters like arrows or other non-alphanumeric characters if needed

    Parameters:
        cell_content (str): Text content of table cell

    Returns:
        str: Text content of table cell without any special characters

    """
    cell_content = re.sub(r'[^\w\s:/]', '', cell_content)
    cell_content = re.sub(r'\n', ' ', cell_content)
    cell_content = re.sub(r'\t', ' ', cell_content)
    cell_content = cell_content.strip()
    return cell_content


def pdf_to_docx(pdf_path, docx_path=None, start_page=0, end_page=None, pages=None):
    """

    Converts a PDF file to a DOCX (Microsoft Word) file.

    The user can specify the path for the output DOCX file, as well as the range
    of pages to be converted. If the DOCX path is not provided, the function
    automatically generates a file name based on the input PDF file name.
    Only the specified range of pages will be converted; if no range is specified,
    the entire PDF is converted.

    Parameters:
        pdf_path (str): The file path of the PDF to be converted.
        docx_path (str, optional): The file path for the output DOCX file.
                                   If not provided, a default name is created based on the input PDF file name.
        start_page (int, optional): The starting page number for conversion.
                                    Defaults to 0, which represents the first page of the PDF.
        end_page (int, optional): The ending page number for conversion.
                                  If not provided, conversion continues until the end of the PDF.
        pages (list, optional): List of page indices for PDF to DOCX conversion.
                                Has priority over --start_page/--end_page!

    Returns:
        str: The file path of the converted DOCX file.

    """
    if docx_path is None:
        docx_path = pdf_path.replace('.pdf', '_converted_by_pdf2docx.docx')
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=start_page, end=end_page, pages=pages)
    cv.close()
    return docx_path
