import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# inputフォルダとoutputフォルダのパス
input_folder = "input"
output_folder = "output"
filename = os.environ['TARGET_FILE']
# inputフォルダ内のPDFファイルを読み込み
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        filepath = os.path.join(input_folder, filename)
        # PDFファイルを開く
        with open(filepath, 'rb') as infile:
            # PDFリーダーを作成
            reader = PdfFileReader(infile)
            # ページ数を取得
            num_pages = reader.getNumPages()
            # 各ドキュメントのページ数リスト
            str_val = "3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,11".split(',')

            # 例として、10ページ、15ページ、20ページのドキュメントとする
            page_counts = [int(x) for x in str_val]
            print(page_counts)
            # # ページ数リストとドキュメント名の対応
            # document_names = ["doc1", "doc2", "doc3"]  # 例として、3つのドキュメントを作成する
            # 出力ディレクトリを作成
            output_dir = os.path.join(
                output_folder, os.path.splitext(filename)[0])
            os.makedirs(output_dir, exist_ok=True)
            # ページをチャンクごとに分割して出力
            start = 0
            for i, count in enumerate(page_counts):
                # 出力ファイル名を生成
                output_filename = os.path.join(
                    output_dir, f"{os.path.splitext(filename)[0]}_{i+1}.pdf")
                # 出力ファイルを作成
                with open(output_filename, 'wb') as outfile:
                    # ファイルライターを作成
                    writer = PdfFileWriter()
                    # チャンクのページ範囲を計算
                    end = start + count
                    # ページを追加
                    for j in range(start, end):
                        if j < num_pages:  # 読み込んだPDFファイルのページ数を超えるページにアクセスしないようにする
                            writer.addPage(reader.getPage(j))
                    # 出力ファイルに書き込み
                    writer.write(outfile)
                # 次のドキュメントの開始ページを更新
                start = end
