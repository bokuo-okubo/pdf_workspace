import PyPDF2
import copy
import os

# original: https://gammasoft.jp/blog/pdf-divide-by-python/

file_name = os.environ['TARGET_FILE']

if not file_name:
    exit('no file name')

input_file = f'./input/{file_name}.pdf'  # 見開き原稿
output_file = f"./output/{file_name}_splited.pdf"  # 分割したPDFの保存

pdf_reader = PyPDF2.PdfFileReader(input_file)
pdf_writer = PyPDF2.PdfFileWriter()

for i in range(pdf_reader.getNumPages()):
    # 同じページのオブジェクトを２つ用意
    p1 = pdf_reader.getPage(i)
    p2 = copy.copy(p1)
    # 原稿の左下と右上の座標を取得（用紙サイズ）
    x0 = p1.mediaBox.getLowerLeft_x()
    y0 = p1.mediaBox.getLowerLeft_y()
    x1 = p1.mediaBox.getUpperRight_x()
    y1 = p1.mediaBox.getUpperRight_y()
    # 左右に分割して切り抜く領域の座標を計算
    p1_lower_left = (x0, y0)
    p1_upper_right = ((x0 + x1) / 2, y1)
    p2_lower_left = ((x0 + x1) / 2, y0)
    p2_upper_right = (x1, y1)
    if abs(y1 - y0) > abs(x1 - x0):
        # 縦長の場合は上下で分割するように変える
        p1_upper_right = (x1, (y0 + y1) / 2)
        p2_lower_left = (x0, (y0 + y1) / 2)
    # 切り抜く領域（cropBox）の設定
    p1.cropBox.lowerLeft = p1_lower_left
    p1.cropBox.upperRight = p1_upper_right
    p2.cropBox.lowerLeft = p2_lower_left
    p2.cropBox.upperRight = p2_upper_right
    # 縦長の場合は上,下の順に並び替える（不要な場合はこの２行は削除）
    if abs(y1 - y0) > abs(x1 - x0):
        p1, p2 = p2, p1
    # 出力用のオブジェクトに２ページ分を追加
    pdf_writer.addPage(p1)
    pdf_writer.addPage(p2)

# ファイルに出力
with open(output_file, mode="wb") as f:
    pdf_writer.write(f)
