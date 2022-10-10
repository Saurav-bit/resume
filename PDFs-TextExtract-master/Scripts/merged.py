import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)
if __name__ == '__main__':
# def main():
    paths = glob.glob('../samples/*.pdf')
    paths.sort()
    merger('../pdf_merged.pdf', paths)
    print("Done, PDF Merged successfully..")

    
    # PDFs-TextExtract-master\PDFs-TextExtract-master\pdf_merged.pdf