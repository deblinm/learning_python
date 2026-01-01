import pypdf

input_path =input("Please enter a pdf file with complete path: ")
modified_path=input_path.replace('/','\\')
writer=pypdf.PdfWriter(clone_from=modified_path)

for page in writer.pages:
    page.compress_content_streams(level=9)

writer.write(f"{modified_path}_compressed.pdf")



