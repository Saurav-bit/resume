import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import sys
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)



def pdf_remove (length):
 for i in range(length): 
        os.remove("../PDFs-TextExtract/split/{}".format(fname[i])) #Remove existed pdf documents in folder.
        print("Deleted: ../PDFs-TextExtract/split/{}".format(fname[i]))

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '../PDFs-TextExtract/split/{}.pdf'.format(page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format(output_filename))
        

def clear_text():
   open("../PDFs-TextExtract/output/Output.txt", "w").close()
   
#writelines function
def writelines(self, lines):
    self._checkClosed()
    for line in lines:
       self.write(line)

#PDF to text Function. 
def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    filepath.close()
    device.close()
    retstr.close()
    return text
 
if __name__ == '__main__':
    paths = glob.glob('../PDFs-TextExtract/samples/*.pdf')
    paths.sort()
    merger('../PDFs-TextExtract/pdf_merged.pdf', paths)
    print("Done, PDF Merged successfully..")
    path = '../PDFs-TextExtract/pdf_merged.pdf' #specifiy your main pdf document path.
    fname = os.listdir('../PDFs-TextExtract/split/') #fname: List contain pdf documents names in folder
    length = len(fname) #Retrieve List fname Length.

    #call pdf remove function
    pdf_remove(length) 
    #call pdf splitter function
    pdf_splitter(path) 
    clear_text()
    fname = os.listdir('../PDFs-TextExtract/split/') #fname : List contain pdf documents names.
    #fname: must be sorted.
    fname.sort(key=lambda f: int(re.sub('\D', '', f)))
    length = len(fname) 


    for i in range(length): #Repeat each operation for each document.

        text_output = pdf_to_text(('../PDFs-TextExtract/split/{}').format(fname[i])) #Extract text with PDF_to_text Function call
        text1_output = text_output.decode("utf-8")     #Decode result from bytes to text
        print(text1_output)

        
        #Save extracted text to TEXT_FILE    
        with open("../PDFs-TextExtract/output/Output.txt", "a", encoding="utf-8") as text_file:
            text_file.writelines(text1_output)


 





   

