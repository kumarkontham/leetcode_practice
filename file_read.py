from pypdf import PdfReader
path = r"C:\Users\USER\Downloads\sample-invoice.pdf"
reader = PdfReader(path)
page = reader.pages[0]
print(page.extract_text())