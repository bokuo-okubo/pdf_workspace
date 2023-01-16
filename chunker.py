import PyPDF2
from more_itertools import chunked

import os
import copy

file_name = os.environ['TARGET_FILE']
if not file_name:
    exit('no file name')
chunk_size = int(os.environ['CHUNK'])
if not chunk_size:
    exit('no chunk size')

input_file = f'./input/{file_name}.pdf'
output_dir = f"./output/{file_name}_chunked"

pdf_reader = PyPDF2.PdfFileReader(input_file)

isExist = os.path.exists(output_dir)
if not isExist:
    os.makedirs(output_dir)

chunk_count = 0
for itr in chunked(range(pdf_reader.getNumPages()), chunk_size):
    pdf_writer = PyPDF2.PdfFileWriter()

    for i in itr:
        p = pdf_reader.getPage(i)
        pdf_writer.addPage(p)

    output_file_name = f'{output_dir}/{file_name}_part_{chunk_count}.pdf'
    with open(output_file_name, mode="wb") as f:
        pdf_writer.write(f)
    chunk_count = chunk_count + 1
