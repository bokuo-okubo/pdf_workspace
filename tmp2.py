import os
from PyPDF2 import PdfFileReader

# outputフォルダのパス
output_folder = "output/After the sun goes down"

the_set = set()

# outputフォルダ内のPDFファイルを読み込み
for dirpath, dirnames, filenames in os.walk(output_folder):
    for filename in filenames:
        if filename.endswith(".pdf"):
            filepath = os.path.join(dirpath, filename)
            # PDFファイルを開く
            with open(filepath, 'rb') as infile:
                # PDFリーダーを作成
                reader = PdfFileReader(infile)
                # ページごとにテキストを抽出してフィルタリング
                for i in range(reader.getNumPages()):
                    page = reader.getPage(i)
                    text = page.extractText()
                    # "Saxophone"、"Trumpet"、"Trombone" を含む行だけにフィルタリング
                    lines = text.split('\n')
                    lines = [line.strip() for line in lines if any(
                        word in line for word in ["Saxophone", "Trumpet", "Trombone", "Guitar", "Drums", "Bass", "Piano"])]
                    # フィルタリングされた行を表示
                    the_set.add(lines[0])

sorted_set = sorted(the_set)  # setをソートしたリストを作成
sorted_str = "\n".join(str(x) for x in sorted_set)  # 改行で区切った文字列を作成
print(sorted_str)
