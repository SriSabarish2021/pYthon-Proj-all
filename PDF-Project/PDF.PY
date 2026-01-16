from PyPDF2 import PdfReader
from PyPDF2 import PdfMerger as merger

read=PdfReader("./III BA PROJECT -SRI SABARISH.(21UENG017).pdf")


text=""

for page in read.pages:
    
    text+=page.extract_text
print(text)

merger.append