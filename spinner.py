import PyPDF2
import copy
import os

# original: https://gammasoft.jp/blog/pdf-divide-by-python/

angle = int(os.environ['ANGLE'])
file_name = os.environ['TARGET_FILE']

if not file_name:
    exit('no file name')

input_file = f'./input/{file_name}.pdf'
output_file = f"./output/{file_name}_spinned.pdf"

pdf_reader = PyPDF2.PdfFileReader(input_file)
pdf_writer = PyPDF2.PdfFileWriter()

for i in range(pdf_reader.getNumPages()):
    p = pdf_reader.getPage(i)
    p.rotateClockwise(angle)
    pdf_writer.addPage(p)

with open(output_file, mode="wb") as f:
    pdf_writer.write(f)
