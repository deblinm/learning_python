import pypdf

input_path =input("Please enter a pdf file with complete path: ")
modified_path=input_path.replace('/','\\')
reader=pypdf.PdfReader(modified_path)
writer=pypdf.PdfWriter()

for page in reader.pages:
    writer.add_page(page)

for page in writer.pages:
    page.compress_content_streams(level=9)

with open(f"{modified_path}_compressed", "wb") as output_file:
    writer.write(output_file)



