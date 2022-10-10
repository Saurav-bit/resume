# import PyPDF2
# import re
# # Open The File in the Command
# file = open("resume.pdf", 'rb')
# readPDF = PyPDF2.PdfFileReader(file)
# def find_url(string):
#    #Find all the String that matches with the pattern
#    regex = r"(https?://\S+)"
#    url = re.findall(regex,string)
#    for url in url:
#       return url
# # Iterating over all the pages of File
# for page_no in range(readPDF.numPages):
#    page=readPDF.getPage(page_no)
#    #Extract the text from the page
#    text = page.extractText()
#    # Print all URL
#    print(find_url(text))
# # CLost the file
# file.close()

# import PyPDF2
# import re
 
# # Enter File Name
# file = "London-Resume-Template-Professional.pdf"
 
# # Open File file
# pdfFileObject = open(file, 'rb')
  
# pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
# # Regular Expression (Get URL from String)
# def Find(string):
   
#     # findall() has been used
#     # with valid conditions for urls in string
#     regex = r"(https?://\S+)"
#     url = re.findall(regex,string)
#     return [x for x in url]
   
# # Iterate through all pages
# for page_number in range(pdfReader.numPages):
     
#     pageObject = pdfReader.getPage(page_number)
     
#     # Extract text from page
#     pdf_text = pageObject.extractText()
     
#     # Print all URL
#     print(Find(pdf_text))
     
# # CLose the PDF
# pdfFileObject.close()


import PyPDF2
PDFFile = open("London-Resume-Template-Professional.pdf",'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

for page in range(pages):
    print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                print(u[ank][uri])