import PyPDF2
import copy
file_name_1 = "omote_all"
file_name_2 = "ura_all"

input_file_1 = f'./input/{file_name_1}.pdf'
input_file_2 = f'./input/{file_name_2}.pdf'


output_file = f"./output/{file_name_1}_{file_name_2}_zipped.pdf"

pdf_reader_omote = PyPDF2.PdfFileReader(input_file_1)
pdf_reader_ura = PyPDF2.PdfFileReader(input_file_2)
pdf_writer = PyPDF2.PdfFileWriter()


if not (pdf_reader_omote.getNumPages() == pdf_reader_ura.getNumPages()):
    exit(f'file {file_name_1} and {file_name_2} is not same page count.')

for i in range(pdf_reader_omote.getNumPages()):
    p1 = pdf_reader_omote.getPage(i)
    p2 = pdf_reader_ura.getPage(i)
    pdf_writer.addPage(p1)
    pdf_writer.addPage(p2)

# ファイルに出力
with open(output_file, mode="wb") as f:
    pdf_writer.write(f)
