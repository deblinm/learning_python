import pypdf

input_path =input("Please enter a pdf file with complete path: ")
modified_path=input_path.replace('/','\\')
reader=pypdf.PdfReader(modified_path)

##Number of Pages
num_pages = len(reader.pages)
print(f"Total number of pages in the pdf : {num_pages}\n\n")

##Extract Data
for i in range(num_pages):
    print (f"\nExtracting text from Page {i+1}\n\n")
    page=reader.pages[i]
    text = page.extract_text()
    print(text)