import pypdf

writer=pypdf.PdfWriter()
num_of_pdfs_to_merge= int(input ("How many pdf files to merge? "))
num_variable=[]

for i in range(1,num_of_pdfs_to_merge+1):
   inp_path=input(f"Enter the file name with path for file {i}: ")
   file_path = inp_path.replace('/', '\\')
   num_variable.append(file_path)

for j in num_variable:
    input_pdf=pypdf.PdfReader(j)
    for page in input_pdf.pages:
        writer.add_page(page)
writer.write("C://Users//debli//python_practice//Files//new_merged_pdf.pdf")
print("Your new pdf has been saved as C://Users//debli//python_practice//Files//new_merged_pdf.pdf")