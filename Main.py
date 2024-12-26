import csv

# 入力ファイルのパス (CLI出力)
input_file = r'C:\Users\L1003613honbu048\Documents\業務\メモ\ピクチャー\2024\Real Pythonバージョン更新\04.テスト\単体テスト\lambda関数テスト\テスト前洗い出し\lambda_functions.txt'
# 出力ファイルのパス (Excel用CSVファイル)
output_file = r'C:\Users\L1003613honbu048\Documents\業務\メモ\ピクチャー\2024\Real Pythonバージョン更新\04.テスト\単体テスト\lambda関数テスト\テスト前洗い出し\lambda_functions.csv'

# テキストファイルを読み込んでCSVファイルに変換
with open(input_file, 'r') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter='\t')  # タブ区切りで読み込む
    writer = csv.writer(outfile)  # CSV書き込み

    # ヘッダーを追加
    writer.writerow(["FunctionName", "Runtime"])
    # データを変換
    for row in reader:
        writer.writerow(row)

print(f"CSVファイルに保存されました: {output_file}")
