import os

# 1. 設定要掃描的資料夾（'.' 代表根目錄，若要掃描特定資料夾可以改成如 'my_folder'）
#TARGET_DIR = '.' 
TARGET_DIR = '202610' 

# 2. 定義產生的 index.html 樣式與結構
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>檔案目錄清單</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #333; }}
        h1 {{ border-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #eaecef; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ padding: 10px 0; border-bottom: 1px solid #f6f8fa; }}
        a {{ color: #0366d6; text-decoration: none; font-weight: 500; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>檔案目錄清單</h1>
    <ul>
        {list_items}
    </ul>
</body>
</html>
"""

def generate():
    # 3. 掃描目標資料夾中的所有檔案
    files = []
    for file in os.listdir(TARGET_DIR):
        # 只抓取 .html 檔案，並且排除 index.html 本身
        if file.endswith('.html') and file != 'index.html':
            files.append(file)
            
    # 4. 排序檔案名稱（讓列表更有序）
    files.sort()
    
    # 5. 組裝 <li> 連結
    list_items = ""
    for file in files:
        list_items += f'        <li><a href="{file}">{file}</a></li>\n'
        
    # 如果完全沒有檔案，給個提示
    if not files:
        list_items = "        <li>尚未有其他 HTML 檔案</li>"
        
    # 6. 將內容寫入到 index.html
    output_content = HTML_TEMPLATE.format(list_items=list_items.strip())
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output_content)
        
    print(f"成功生成 index.html！共連結了 {len(files)} 個檔案。")

if __name__ == '__main__':
    generate()
