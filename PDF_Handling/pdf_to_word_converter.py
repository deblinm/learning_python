from pdf2docx import parse

pdf_file = "C://Users//debli//Downloads//CV//Deblin_Moitra_Oracle_PLSQL_Developer_CV.pdf"
docx_file = "C://Users//debli//Downloads//CV//Deblin_Moitra_Oracle_PLSQL_Developer_CV_word_version.docx"

# Convert PDF to DOCX
parse(pdf_file, docx_file, start=0, end=None)
print(f"Successfully converted {pdf_file} to {docx_file}")
